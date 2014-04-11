#!/usr/bin/python
import sys
import os
import CppHeaderParser

from config      import *
from genJsApi    import *
from genJsApiMap import *
from genC        import *

def ParseHeader(name):
  try:
    printDbg("parsing " + name)
    cppHeader = CppHeaderParser.CppHeader(name)    
    return cppHeader

  except CppHeaderParser.CppParseError,  e:
    printDbg(e)
    sys.exit(1)

def HandleHeader(root, f):
  split = f.rsplit('.', 1)

  #only .h file is wanted
  if(split[1] != 'h'):
    printDbg(f + ' is not header file')
    return

  # init debug output
  SetPrintModule(f)

  cppHeader = ParseHeader(root + "/" + f);  

  GenJsApiMap(split[0], cppHeader)

  #to handle the override functions
  for c in cppHeader.classes:
    GroupFunc(cppHeader.classes[c]["methods"]["public"])
  GroupFunc(cppHeader.functions)

  GenJsApi(split[0], cppHeader)
  GenC(split[0], cppHeader)
  
  UnsetPrintModule()

if __name__ == "__main__":

  GenPreGlobalInit()

  for i in range (len(INPUT_DECL_PATHS)):
    printDbg("searching " +INPUT_DECL_PATHS[i])
    for root, dirs, files in os.walk(INPUT_DECL_PATHS[i]):
      for f in files:
        HandleHeader(root, f)
        print ""

  GenPostGlobalInit()
  GenGyp()
  DumpSummary()