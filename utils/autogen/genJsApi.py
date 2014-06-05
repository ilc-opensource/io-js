from config import *
from util import *
import os

def GenClassConstructor(className):
  return \
'''
%s = function() {
  return self.submit.classReq('%s', arguments, this);
};
''' % (className, className)

def GenClassConstructorMap(className):
  return \
'''
  map['%s'] = function() {
    self.handle.classReq(self.io.%s, arguments, '%s');
  };
''' % (className, className, className)

def GenClassMethod(className, funcName):
  return \
'''
%s.prototype.%s = function() {
  return self.submit.classMethodReq('%s', '%s', arguments, this);
};
''' % (className, funcName, className, funcName)
 
def GenClassMethodMap(className, funcName):
  return \
'''
  map['%s.%s'] = function() {
    self.handle.classMethodReq(arguments, '%s', '%s');
  };
''' % (className, funcName, className, funcName)


def GenClassJsApi(className, c):
  methods = c["methods"]["public"];
  s = ""

  for m in methods:
    methodName = m["name"]
    if m["name"] == className:
      s += GenClassConstructor(className)
    else:
      s += GenClassMethod(className, methodName)

  s = AddIndent(s, 2); 
  s += \
'''
  self.%s = %s;
''' % (className, className)
  return s

def GenClassJsApiMap(className, c):
  methods = c["methods"]["public"];
  s = ""

  for m in methods:
    methodName = m["name"]
    if m["name"] == className:
      s += GenClassConstructorMap(className)
    else:
      s += GenClassMethodMap(className, methodName)

  return s

def GenJsConst(defines):
  s =''
  for define in defines:
    macros = IsValidMacro(define)
    if len(macros) == 0:
      continue
    s += \
'''
  self.%s = %s;
''' % (macros[0], macros[1])
  return s

def GenPreFuncJsApi():
  mkdir(OUTPUT_COMP_PATH)
  f = OUTPUT_COMP_PATH + "/" + TARGET +".js"
  fp = open(f, "w")
  s = \
'''
(function(exports, global) {

/*********************************************
Generated with autogen tool
*********************************************/

var Board = function(options) {

  submit = options.submit;
  
  var self = this;
  
  self.submit = options.submit;
  
  self.config  = function(options) {
    submit.config(options);
  };
  
''' 
  fp.write(s)

def GenPostFuncJsApi():
  f = OUTPUT_COMP_PATH + "/" + TARGET +".js"
  fp = open(f, "a")
  s = \
'''

}; //end of Board class declare

exports.Board = Board;

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB);
'''
  fp.write(s)

def GenPreFuncJsApiMap():
  mkdir(OUTPUT_SERVER_PATH)
  f = OUTPUT_SERVER_PATH + "/" + TARGET + ".js"
  fp = open(f, "w")
  s = \
'''
/*********************************************
Generated with autogen tool
*********************************************/

var methods = function(options) {
  var self = this;
  self.io = options.io;
  self.handle = options.handle;
  var map = {};

''' 
  fp.write(s)

def GenPostFuncJsApiMap():
  f = OUTPUT_SERVER_PATH + "/" + TARGET + ".js"
  fp = open(f, "a")
  s = \
'''
  self.map = map;
};

module.exports =  methods;
'''
  fp.write(s)

def GenFuncJsApi(module, func):
  funcName = func["name"]
  return \
'''
  self.%s = function() {
    return self.submit.funcReq('%s', arguments);
  };
''' % (funcName, funcName)

def GenFuncJsApiMap(module, func):
  funcName = func["name"]
  return \
'''
  map['%s'] = function() {
    self.handle.funcReq(self.io.%s, arguments, '%s');
  };
''' % (funcName, funcName, funcName)

def GenJsApi(module, cppHeader):
  clientStr = \
'''
/****************************************
           %s
****************************************/
''' % module 

  servStr = \
'''
  /****************************************
             %s
  ****************************************/
''' % module 

  for c in cppHeader.classes:
    if cppHeader.classes[c]["declaration_method"] == "class":
      clientStr += GenClassJsApi(module, cppHeader.classes[c])
      servStr += GenClassJsApiMap(module, cppHeader.classes[c])

  clientStr += GenJsConst(cppHeader.defines)

  #generate map of functions
  for idx, func in enumerate(cppHeader.functions):
    clientStr += GenFuncJsApi(module, func)
    servStr += GenFuncJsApiMap(module, func)

  f = OUTPUT_COMP_PATH + "/" + TARGET +".js"
  fp = open(f, "a")
  fp.write(clientStr)
  printDbg( "generate " + f)
  
  f = OUTPUT_SERVER_PATH + "/" + TARGET +".js"
  fp = open(f, "a")
  fp.write(servStr)
  printDbg( "generate " + f)

