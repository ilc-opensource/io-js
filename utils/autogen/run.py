#!/usr/bin/python
import os
import CppHeaderParser
import globalVar
import getopt
import sys
import config
import configSys

from genJsApi    import *
from genJsApiMap import *
from genC        import *
from genShell    import *
from genNodeRedNodes    import *
from installAll  import *
def ParseHeader(name):
  try:
    printDbg("parsing " + name)
    cppHeader = CppHeaderParser.CppHeader(name)
  except CppHeaderParser.CppParseError, e:
    printDbg(e)
    sys.exit(1)
  return cppHeader

def CollectHeader(root, f):
  if f.find('.') == -1:
    return

  split = f.rsplit('.', 1)

  #only .h file is wanted
  if(split[1] != 'h'):
    printDbg(f + ' is not header file')
    return

  cppHeader = ParseHeader(root + "/" + f);

  ParseTypedefs(cppHeader.typedefs)
  ParseFuncPoint(cppHeader)
  FixEnumPropType(cppHeader)
  globalVar.cppHeaders[f] = cppHeader


def HandleHeader(f):

  if f == "version_export.h":
    fcpp = root + "/version_export.cpp"
    os.system("cp " + fcpp + " " + configSys.OUTPUT_DEV_PATH)

  # init debug output
  SetPrintModule(f)

  globalVar.curCppHeader = globalVar.cppHeaders[f];
  globalVar.includeFiles = []

  split = f.rsplit('.', 1)

  GenJsApiMap(split[0], globalVar.curCppHeader)

  #to handle the override functions
  for c in globalVar.curCppHeader.classes:
    FormalizeFunc(globalVar.curCppHeader.classes[c]["methods"]["public"])
    GroupFunc(globalVar.curCppHeader.classes[c]["methods"]["public"])

  FormalizeFunc(globalVar.curCppHeader.functions)
  GroupFunc(globalVar.curCppHeader.functions)

  #GenJsApiMap(split[0], cppHeader)
  GenJsApi(split[0], globalVar.curCppHeader)
  GenC(split[0], globalVar.curCppHeader)
  GenNodeRedNodes(split[0], globalVar.curCppHeader)

  UnsetPrintModule()

def Usage():
  print 'run.py usage:'
  print '-h,--help: print help message.'
  print '-v, --version: print script version'
  print \
'''-c, --config: appointed configure file which should be like config.py;
              if no this option, config.py is the default configure-file.'''
  print '-t, --test: test option '

def SetConfigVar(configfileName):
  print "==================configure file: %s ========================="  %configfileName
  configfile = __import__(os.path.splitext(configfileName)[0])

  try:
    config.INPUT_DIR = configfile.INPUT_DIR
  except:
    print "config.INPUT_DIR: ", config.INPUT_DIR
  else:
    print "config.INPUT_DIR: ", config.INPUT_DIR
  
  try:
    config.INPUT_DECL_PATHS = configfile.INPUT_DECL_PATHS
  except:
    print "config.INPUT_DECL_PATHS: ", config.INPUT_DECL_PATHS
  else:
    print "config.INPUT_DECL_PATHS: ", config.INPUT_DECL_PATHS
  
  try:
    config.INPUT_LIB_PATH = configfile.INPUT_LIB_PATH
  except:
    print "config.INPUT_LIB_PATH: ", config.INPUT_LIB_PATH
  else:
    print "config.INPUT_LIB_PATH: ", config.INPUT_LIB_PATH
  
  try:
    config.ATLAS_PATH = configfile.ATLAS_PATH
  except:
    print "config.ATLAS_PATH:", config.ATLAS_PATH
  else:
    print "config.ATLAS_PATH:", config.ATLAS_PATH
  
  try:
    config.NODERED_PATH = configfile.NODERED_PATH
  except:
    print "config.NODERED_PATH: ", config.NODERED_PATH
  else:
    print "config.NODERED_PATH: ", config.NODERED_PATH
  
  try:
    config.INSTALL_DIR = configfile.INSTALL_DIR
  except:
    print "config.INSTALL_DIR: ", config.INSTALL_DIR
  else:
    print "config.INSTALL_DIR: ", config.INSTALL_DIR
  
  try:
    config.EXTRA_LIB = configfile.EXTRA_LIB
  except:
    print "config.EXTRA_LIB: ", config.EXTRA_LIB
  else:
    print "config.EXTRA_LIB: ", config.EXTRA_LIB
  
  try:
    config.GYP_LIB = configfile.GYP_LIB
  except:
    print "config.GYP_LIB: ", config.GYP_LIB
  else:
    print "config.GYP_LIB: ", config.GYP_LIB
  
  try:
    config.AUTOGEN_TEST = configfile.AUTOGEN_TEST
  except:
    print "config.AUTOGEN_TEST:", config.AUTOGEN_TEST
  else:
    print "config.AUTOGEN_TEST:", config.AUTOGEN_TEST
  
  try:
    config.DEBUG = configfile.DEBUG
  except:
    print "config.DEBUG:", config.DEBUG
  else:
    print "config.DEBUG:", config.DEBUG
  print "==================================================================="

def Version():
  print "run.py version: ", configSys.VERSION

if __name__ == "__main__":
  try:
    opts, args = getopt.getopt(sys.argv[1:], 'hvtc:', ['help', 'version', 'test', 'config='])
  except getopt.GetoptError, err:
    print str(err)
    Usage()
    sys.exit(2)
  
  autotest = 0

  for o, arg in opts:
    if o in ('-h', '--help'):
      Usage()
      sys.exit(1)
    elif o in ('-v', '--version'):
      Version()
      sys.exit(0)
    elif o in ('-t', '--test'):
      autotest = 1
      break
    elif o in ('-c', '--config'):
      SetConfigVar(arg)
#sys.exit(3)
    else:
      print 'unhandled option'
      sys.exit(3)

  print config.AUTOGEN_TEST

  if autotest == 1:
    config.AUTOGEN_TEST = 1

  if config.AUTOGEN_TEST == 1:
    config.INPUT_DECL_PATHS  = [
      "./testSuite/"
    ]
  
  for p in config.INPUT_DECL_PATHS:
    if os.path.isfile(p):
      root = os.path.dirname(p)
      f = os.path.basename(p)
      CollectHeader(root, f)
    else:
      printDbg("searching " + p)
      for root, dirs, files in os.walk(p):
        for f in files:
          CollectHeader(root, f)

  ExpandTypedef()

  GenPreGlobalInit()
  GenPreFuncJsApi()
  GenPreFuncJsApiMap()

  for f in globalVar.cppHeaders.keys():
    HandleHeader(f)

  GenPostFuncJsApi();
  GenPostFuncJsApiMap()
  GenPostGlobalInit()
  GenCallback()
  GenGyp()
  GenGlobalClassVarJsExport()
  GenShell()
  InstallAll()
  DumpSummary()
