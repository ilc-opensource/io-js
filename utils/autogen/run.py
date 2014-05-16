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
    globalVar.cppHeader = CppHeaderParser.CppHeader(name)

  except CppHeaderParser.CppParseError,  e:
    printDbg(e)
    sys.exit(1)

def HandleHeader(root, f):
  if f.find('.') == -1:
    return

  split = f.rsplit('.', 1)

  #only .h file is wanted
  if(split[1] != 'h'):
    printDbg(f + ' is not header file')
    return

  if f == "version_export.h":
    fcpp = root + "/version_export.cpp"
    os.system("cp " + fcpp + " " + OUTPUT_DEV_PATH)

  # init debug output
  SetPrintModule(f)

  ParseHeader(root + "/" + f);

  ParseTypedefs(globalVar.cppHeader.typedefs)
  ParseFuncPoint(globalVar.cppHeader)

  GenJsApiMap(split[0], globalVar.cppHeader)

  #to handle the override functions
  for c in globalVar.cppHeader.classes:
    FormalizeFunc(globalVar.cppHeader.classes[c]["methods"]["public"])
    GroupFunc(globalVar.cppHeader.classes[c]["methods"]["public"])

  FormalizeFunc(globalVar.cppHeader.functions)
  GroupFunc(globalVar.cppHeader.functions)

  #GenJsApiMap(split[0], cppHeader)
  GenJsApi(split[0], globalVar.cppHeader)
  GenC(split[0], globalVar.cppHeader)
  
  UnsetPrintModule()

if __name__ == "__main__":

  GenPreGlobalInit()
  GenPreFuncJsApi()
  GenPreFuncJsApiMap()

  for p in INPUT_DECL_PATHS:
    if os.path.isfile(p):
      root = os.path.dirname(p)
      f = os.path.basename(p)
      HandleHeader(root, f)
    else:
      printDbg("searching " + p)
      for root, dirs, files in os.walk(p):
        for f in files:
          HandleHeader(root, f)

  GenPostFuncJsApi();
  GenPostFuncJsApiMap();
  GenPostGlobalInit()
  GenCallback()
  GenGyp()
  DumpSummary()
