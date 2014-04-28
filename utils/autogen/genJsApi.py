from config import *
from util import *
import os

def GenClassConstructor(className):
  print className
  return \
'''
%s = function() {
  var className = "%s";
  var funcName = "%s";
  bridge.dump(className, funcName, arguments);
};
''' % (className, className, className)

def GenClassMethod(className, funcName):
  return \
'''
%s.prototype.%s = function() {
  var className = "%s";
  var funcName = "%s";
  bridge.dump(className, funcName, arguments);
};
''' % (className, funcName, className, funcName,)
 
def GenClassJsApi(className, c):
  methods = c["methods"]["public"];
  s = ""

  for m in methods:
    methodName = m["name"]
    if m["name"] == className:
      s += GenClassConstructor(className)
    else:
      s += GenClassMethod(className, methodName)
    
  s += \
'''
module.exports.%s = %s;
''' % (className, className)
  
  return s

def GenJsConst(defines):
  s =''
  for define in defines:
    macros = IsValidMacro(define)
    if len(macros) == 0:
      continue
    s += \
'''
module.exports.%s = %s;
''' % (macros[0], macros[1])
  return s

def GenPreFuncJsApi():
  f = OUTPUT_COMP_PATH + "/" + "index.js"
  fp = open(f, "w")
  s = \
'''
var bridge = require("./bridge.js");

/*********************************************
Generated with autogen tool
*********************************************/
''' 
  fp.write(s)

def GenFuncJsApi(module, func):
  funcName = func["name"]
  return \
'''
module.exports.%s = function() {
  var className = undefined;
  var funcName = "%s";
  bridge.dump(className, funcName, arguments);
};
''' % (funcName, funcName)

def GenJsApi(module, cppHeader):
  s = \
'''
/****************************************
           %s
****************************************/
''' % module 
  for c in cppHeader.classes:
    s += GenClassJsApi(module, cppHeader.classes[c])

  s += GenJsConst(cppHeader.defines)

  #generate map of functions
  for idx, func in enumerate(cppHeader.functions):
    s += GenFuncJsApi(module, func)

  f = OUTPUT_COMP_PATH + "/" + "index.js"
  fp = open(f, "a")
  fp.write(s)
  printDbg( "generate " + f)
  

