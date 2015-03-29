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

def IsSet(var, configfile):
  try:
    type (eval(var))
  except:
    return 0
  else:
    return 1

def AddRelativePath(var, rPath, configfilePath):
  rVar = var
  absVar = var
  
#  if var[0] != '/':
#    absVar = configfilePath + "/" + var

#  if not os.path.exists(absVar):
#    assert 0, "%s is not exist" %(os.path.abspath(absVar))

  if var[0] != '/':
    rVar = rPath + "/" + var

  return rVar

def GetVarFromFile(var, rPath, configfilePath) :
  if isinstance(var, str):
    return AddRelativePath(var, rPath, configfilePath)
  elif isinstance(var, list):
    rvar = []
    for idx, ivar in enumerate(var):
      rvar.append(AddRelativePath(ivar, rPath, configfilePath))
    return rvar
  elif isinstance(var, int):
    return var
  else:
    assert 0, "unexpected type for value from configfile"


def SetConfigVar(configfileName):
  print "==================configure file: %s ========================="  %configfileName
  runScriptPath = os.path.abspath(os.getcwd())
  configfilePath = os.path.split(os.path.abspath(configfileName))[0]
  printDbg("runScriptPath: " + runScriptPath)
  printDbg("configfilePath: " + configfilePath)
  configfileImportName = os.path.split(configfileName)[1]

  rPath = os.path.relpath(configfilePath, runScriptPath)

  if not configfilePath in sys.path:
    sys.path.append(configfilePath)
  
  configfile = __import__(os.path.splitext(configfileImportName)[0])

  if IsSet("configfile.INPUT_DIR", configfile):
    config.INPUT_DIR = GetVarFromFile(configfile.INPUT_DIR, rPath, configfilePath)
  else:
    print "set INPUT_DIR from %s error" %(configfileName)
  print "config.INPUT_DIR: ", config.INPUT_DIR
  
  if IsSet("configfile.INPUT_DECL_PATHS", configfile):
    config.INPUT_DECL_PATHS = GetVarFromFile(configfile.INPUT_DECL_PATHS, rPath, configfilePath)
  else:
    print "set INPUT_DECL_PATHS from %s error" %(configfileName)
  print "config.INPUT_DECL_PATHS: ", config.INPUT_DECL_PATHS
  
  if IsSet("configfile.INPUT_LIB_PATH", configfile):
    config.INPUT_LIB_PATH = GetVarFromFile(configfile.INPUT_LIB_PATH, rPath, configfilePath)
  else:
    print "set INPUT_LIB_PATH from %s error" %(configfileName)
  print "config.INPUT_LIB_PATH: ", config.INPUT_LIB_PATH
  
  if IsSet("configfile.ATLAS_PATH", configfile):
    config.ATLAS_PATH = GetVarFromFile(configfile.ATLAS_PATH, rPath, configfilePath)
  else:
    print "ATLAS_PATH from %s error" %(configfileName)
  print "config.ATLAS_PATH:", config.ATLAS_PATH
  
  if IsSet("configfile.NODERED_PATH", configfile):
    config.NODERED_PATH = GetVarFromFile(configfile.NODERED_PATH, rPath, configfilePath)
  else:
    print "set NODERED_PATH from %s error" %(configfileName)
  print "config.NODERED_PATH: ", config.NODERED_PATH
  
  if IsSet("configfile.INSTALL_DIR", configfile):
    config.INSTALL_DIR = GetVarFromFile(configfile.INSTALL_DIR, rPath, configfilePath)
  else:
    print "set INSTALL_DIR from %s error" %(configfileName)
  print "config.INSTALL_DIR: ", config.INSTALL_DIR
  
  if IsSet("configfile.EXTRA_LIB", configfile):
    config.EXTRA_LIB = configfile.EXTRA_LIB
  else:
    print "set EXTRA_LIB from %s error" %(configfileName)
  print "config.EXTRA_LIB: ", config.EXTRA_LIB
  
  if IsSet("configfile.AUTOGEN_TEST",  configfile):
    config.AUTOGEN_TEST = configfile.AUTOGEN_TEST
  else:
    print "set AUTOGEN_TEST from %s error" %(configfileName)
  print "config.AUTOGEN_TEST:", config.AUTOGEN_TEST
  
  if IsSet("configfile.DEBUG", configfile):
    config.DEBUG = configfile.DEBUG
  else:
    print "set DEBUG from %s error" %(configfileName)
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

 # Set default config file 
  configfile = os.path.split(os.path.realpath(__file__))[0] + "/config.py"

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
      configfile = arg
#sys.exit(3)
    else:
      print 'unhandled option'
      sys.exit(3)

  SetConfigVar(configfile)
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
