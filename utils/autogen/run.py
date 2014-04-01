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
    print "parsing ", name
    cppHeader = CppHeaderParser.CppHeader(name)    
    return cppHeader

  except CppHeaderParser.CppParseError,  e:
    print e
    sys.exit(1)

def HandleHeader(root, f):
  split = f.rsplit('.', 1)

  #only .h file is wanted
  if(split[1] != 'h'):
    print f, ' is not header file'
    return

  cppHeader = ParseHeader(root + "/" + f);  

  GenJsApiMap(split[0], cppHeader)

  #to handle the override functions
  for c in cppHeader.classes:
    GroupFunc(cppHeader.classes[c]["methods"]["public"])
  GroupFunc(cppHeader.functions)

  GenJsApi(split[0], cppHeader)
  GenC(split[0], cppHeader)

if __name__ == "__main__":
  for i in range (len(INPUT_DECL_PATHS)):
    print "path: %s" %(INPUT_DECL_PATHS[i])
    for root, dirs, files in os.walk(INPUT_DECL_PATHS[i]):
      for f in files:
        HandleHeader(root, f)
        print ""
