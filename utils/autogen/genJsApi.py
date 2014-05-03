from config import *
from util import *
import os

def GenClassConstructor(className):
  return \
'''
%s = function() {
  return submit.classReq('%s', arguments, this);
};
''' % (className, className)

def GenClassConstructorMap(className):
  return \
'''
  '%s': function() {
    handle.classReq(io.%s, arguments, '%s');
  },
''' % (className, className, className)

def GenClassMethod(className, funcName):
  return \
'''
%s.prototype.%s = function() {
  return submit.classMethodReq('%s', '%s', arguments, this);
};
''' % (className, funcName, className, funcName)
 
def GenClassMethodMap(className, funcName):
  return \
'''
  '%s.%s': function() {
    handle.classMethodReq(arguments, '%s', '%s');
  },
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
    
  s += \
'''
Board.prototype.%s = %s;
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
Board.prototype.%s = %s;
''' % (macros[0], macros[1])
  return s

def GenPreFuncJsApi():
  f = OUTPUT_COMP_PATH + "/" + TARGET +".js"
  fp = open(f, "w")
  s = \
'''
(function(exports, global) {

/*********************************************
Generated with autogen tool
*********************************************/

var submit = undefined;

var Board = function(options) {
  var Submit;
  if(typeof require === 'function' && typeof module === 'object') {
    Submit = require(options.submitPath).Submit;
  } else {
    Submit = global.Submit;
  }

  submit = new Submit(options);

};

exports.Board = Board;

Board.prototype.config = function(options) {
  submit.config(options);
};

''' 
  fp.write(s)

def GenPostFuncJsApi():
  f = OUTPUT_COMP_PATH + "/" + TARGET +".js"
  fp = open(f, "a")
  s = \
'''
})(typeof exports === 'object'? exports: this, this);
'''
  fp.write(s)

def GenPreFuncJsApiMap():
  f = OUTPUT_SERVER_PATH + "/" + TARGET + ".js"
  fp = open(f, "w")
  s = \
'''

/*********************************************
Generated with autogen tool
*********************************************/

var io = undefined;
var handle = undefined;

var methods = function(options) {
  io = require(options.ioPath);
  handle = require(options.handleReqPath);
};

// Generate method map for rpc server
methods.prototype.map = {
''' 
  fp.write(s)

def GenPostFuncJsApiMap():
  f = OUTPUT_SERVER_PATH + "/" + TARGET + ".js"
  fp = open(f, "a")
  s = \
'''
};

module.exports =  methods;
'''
  fp.write(s)

def GenFuncJsApi(module, func):
  funcName = func["name"]
  return \
'''
Board.prototype.%s = function() {
  return submit.funcReq('%s', arguments);
};
''' % (funcName, funcName)

def GenFuncJsApiMap(module, func):
  funcName = func["name"]
  return \
'''
  '%s': function() {
    handle.funcReq(io.%s, arguments, '%s');
  },
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

