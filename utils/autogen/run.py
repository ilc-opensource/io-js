#!/usr/bin/python
import sys
import os
import CppHeaderParser
import globalVar

from config      import *
from genJsApi    import *
from genJsApiMap import *
from genC        import *

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
    os.system("cp " + fcpp + " " + OUTPUT_DEV_PATH)

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

  UnsetPrintModule()

if __name__ == "__main__":

  for p in INPUT_DECL_PATHS:
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
  DumpSummary()
