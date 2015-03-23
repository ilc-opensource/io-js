import configSys
from util import *
import os
import globalVar

def GetJsDocType(var, isResult):
  varBasicType = GetBasicType(var)
  if IsStructArg(varBasicType) or IsClassArg(varBasicType):
    JsDocType = "Object"
  elif IsEnumArg(varBasicType):
    JsDocType = "Integer"
  elif (var["pointer"] == 1 or var["array"] == 1):
    if (GetIdenticalType(var["type"]) == "char*" \
      or (GetIdenticalType(var["type"]) == "char" and var["array"] == 1)):
      if isResult:
        JsDocType = "String"
      else:
        JsDocType = "Array|String|Object"
    elif isinstance(var["function_pointer"], dict) and var["function_pointer"] != {}:
      JsDocType = ""
      for key in globalVar.TypedefCallBackJsDocTypesHT:
        if key == var["type"]:
          JsDocType = globalVar.TypedefCallBackJsDocTypesHT[key][0]
          break;

      if JsDocType == "":
        JsDocType = "Callback_%d" %globalVar.CallBackJsDocTypesCnt
        globalVar.CallBackJsDocTypesCnt = globalVar.CallBackJsDocTypesCnt + 1
        globalVar.CallBackJsDocTypesHT[JsDocType] = var["function_pointer"]
    else:
      JsDocType = "Array"
  else:
    varType = GetIdenticalType(var["type"])

    if (varType == "") or (varType == "void"):
      JsDocType = "Void"

    if (varType == "bool") or (varType == "boolean"):
      JsDocType = "Boolean"

    if (varType == "unsigned int") or (varType == "int") or (varType == "char") \
      or (varType == "short") or (varType == "long long") or (varType == "long"):
      JsDocType = "Integer"

    if (varType == "double"):
      JsDocType = "Double"
    if (varType == "float"):
      JsDocType = "Float"

  return JsDocType

def GenCallBackJsDocType(FPName, FPTypes):
  paraTypes = FPTypes["paraTypes"]
  rtnType = FPTypes["rtnType"]
  s = \
'''
/**
 * @callback %s
''' %(FPName)
  for paraT in paraTypes:
    if GetNoQualifierType(paraT["type"]) == "void" \
       and paraT["pointer"] == 0 and paraT["array"] == 0:
      s += " * @param {Void}\n"
      continue
    s += " * @param {%s}\n" %(GetJsDocType(paraT, False))
  s += " * @returns {%s}\n" %(GetJsDocType(rtnType, True))
  s += " */\n"
  return s

def GenTypedefCallBackJsDocTypesHT():
  for f in globalVar.cppHeaders.keys():
    typedefs = globalVar.cppHeaders[f].typedefs
    for td in typedefs.keys():
      if typedefs[td]["function_pointer"] == 1:
        jsDocType = "Callback_%s" %(td)
        globalVar.TypedefCallBackJsDocTypesHT[td] = [ jsDocType, typedefs[td]["type"]]

def GenCallBackJsDocTypes():
  s = ""
  for key in globalVar.TypedefCallBackJsDocTypesHT.keys():
    jsDocType = globalVar.TypedefCallBackJsDocTypesHT[key][0]
    types = globalVar.TypedefCallBackJsDocTypesHT[key][1]
    s += GenCallBackJsDocType(jsDocType, types)

  for key in globalVar.CallBackJsDocTypesHT.keys():
    types = globalVar.CallBackJsDocTypesHT[key]
    s += GenCallBackJsDocType(key, types)
  return s

def GenParamJsDoc(param, paramName):
  jsDocType = GetJsDocType(param, False)
  if param.has_key("default"):
    return "\n * @param {%s} [%s=%s]" %(jsDocType, paramName, param["default"])
  else:
    return "\n * @param {%s} %s" %(jsDocType, paramName)

def GenFuncParamsJsDoc(func):
  s = ""
  if func.has_key("override") and func["override"]:
    idx = 0
    while (1):
      paramJsDocType = []
      defaultValues = []
      defaultValueNum = 0
      requiredParamNum = 0
      funcNum = len(func["funcs"])
      for f in func["funcs"]:
        params = f["parameters"]
        if f["destructor"] or not CheckSanity(f):
          funcNum = funcNum - 1
          continue

        if len(params) <= idx or \
            (GetIdenticalType(params[idx]["type"]) == "void" \
              and params[idx]["pointer"] == 0 and params[idx]["array"] == 0):
          paramJsDocType.append("None")
          defaultValues.append("None")
          continue

        jsDocType = GetJsDocType(params[idx], False)
        paramJsDocType.append(jsDocType)

        if params[idx].has_key("default"):
          defaultValues.append(params[idx]["default"])
          defaultValueNum += 1
        else:
          defaultValues.append("None")
          requiredParamNum += 1

      if requiredParamNum == 0 and defaultValueNum == 0:
          break

      s += "\n * @param {"
      for i, p in enumerate(paramJsDocType):
        s += p
        if i != len(paramJsDocType) - 1:
          s += "|"
      s += "}"
      if requiredParamNum != funcNum:
        if defaultValueNum == 0:
          s += " [arg%d]" %(idx)
        else:
          s += " [arg%d=" %(idx)
          for j, val in enumerate(defaultValues):
            s += val
            if j != len(defaultValues) - 1:
              s += "|"
          s += "]"
      else:
        s += " arg%d" %(idx)
      idx = idx + 1
  else:
    if len(func["parameters"]) == 0:
      s += "\n * @param {Void}"

    for idx, param in enumerate(func["parameters"]):
      if GetIdenticalType(param["type"]) == "void":
        s += "\n * @param {Void}"
        continue

      paramName = param["name"]
      if paramName == "":
         paramName = "arg%d" %(idx)

      s += GenParamJsDoc(param, paramName)
  return s

def GenReturnJsDoc(rtnType):
  return "\n * @returns {%s}" %(GetJsDocType(rtnType, True))

def GenFuncReturnJsDoc(func):
  if func.has_key("override") and func["override"]:
    s = ""
    retJsDocType = []
    for f in func["funcs"]:
      jsDocType = GetJsDocType(f["rtnType"], True)
      if jsDocType not in retJsDocType:
        retJsDocType.append(jsDocType)
    s += "\n * @returns {"
    for i, p in enumerate(retJsDocType):
      s += p
      if i != len(retJsDocType) - 1:
        s += "|"
    s += "}"
    return s
  else:
    return GenReturnJsDoc(func["rtnType"])

def GenClassConstructor(className, func):
  return \
'''
/**
 * @constructor
 * @name IO#%s%s
 */
%s = function() {
  return self.submit.classReq('%s', arguments, this);
};
''' % (className, GenFuncParamsJsDoc(func), className, className)

def GenClassConstructorMap(className):
  return \
'''
  map['%s'] = function() {
    self.handle.classReq(self.io.%s, arguments, '%s');
  };
''' % (className, className, className)

def GenClassMethod(className, func):
  funcName = func["name"]
  return \
'''
/**
 * @function IO#%s#%s
 * @type function%s%s
 * @instance
 */
%s.prototype.%s = function() {
  return self.submit.classMethodReq('%s', '%s', arguments, this);
};
''' % (className, funcName, \
    GenFuncParamsJsDoc(func), \
    GenFuncReturnJsDoc(func), \
    className, funcName, className, funcName)
 
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
    if not IsV8FuncGen(m):
      continue
    if m["name"] == className:
      s += GenClassConstructor(className, m)
    else:
      s += GenClassMethod(className, m)

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
  /**
   * @constant IO#%s
   * @desc %s
   */
  self.%s = %s;
''' % (macros[0], macros[1], macros[0], macros[1])
  return s


def GenJsEnumConst(enums):
  s = ''
  for enum in enums:
    for v in enum["values"]:
      s += \
'''
  /**
   * @constant IO#%s
   * @desc %s
   */
  self.%s = %s;
''' %(v["name"], v["value"], v["name"], v["value"])
  return s

def GenPreFuncJsApi():
  mkdir(configSys.OUTPUT_COMP_PATH)
  f = configSys.OUTPUT_COMP_PATH + "/" + configSys.TARGET +".js"
  fp = open(f, "w")
  s = \
'''
(function(exports, global) {

%s
var Board = function(options) {

  submit = options.submit;
  
  var self = this;
  
  self.submit = options.submit;
  
  self.config  = function(options) {
    submit.config(options);
  };
  
''' %(GetComment())
  fp.write(s)

def GenPostFuncJsApi():
  f = configSys.OUTPUT_COMP_PATH + "/" + configSys.TARGET +".js"
  fp = open(f, "a")
  s = \
'''
%s
}; //end of Board class declare

exports.Board = Board;

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB);
''' % (GenCallBackJsDocTypes())
  fp.write(s)

def GenPreFuncJsApiMap():
  mkdir(configSys.OUTPUT_SERVER_PATH)
  f = configSys.OUTPUT_SERVER_PATH + "/" + configSys.TARGET + ".js"
  fp = open(f, "w")
  s = \
'''
%s
var methods = function(options) {
  var self = this;
  self.io = options.io;
  self.handle = options.handle;
  var map = {};

''' %(GetComment())
  fp.write(s)

def GenPostFuncJsApiMap():
  f = configSys.OUTPUT_SERVER_PATH + "/" + configSys.TARGET + ".js"
  fp = open(f, "a")
  s = \
'''
  self.map = map;
};

module.exports =  methods;
'''
  fp.write(s)

def GenJsApiGlobalVarSetterAndGetter(global_vars):

  s = ""

  for idx, var in enumerate(global_vars):
    varName = var["name"].capitalize() + "V8"
    getFuncName = "get" + varName

    s += \
'''
/**
 * @function IO#%s
 * @type function
 * @param {Void}%s
 * @instance
 */
  self.%s = function() {
    return self.submit.funcReq('%s', arguments);
  };
'''%(getFuncName, \
    GenReturnJsDoc(var), \
    getFuncName, \
    getFuncName)
    
    if var["constant"] == 1:
      continue

    setFuncName = "set" + varName
    s += \
'''
/**
 * @function IO#%s
 * @type function
%s
 * @return {Void}
 * @instance
 */
  self.%s = function() {
    return self.submit.funcReq('%s', arguments);
  };
'''%(setFuncName, GenParamJsDoc(var, var["name"]) ,setFuncName, setFuncName)

  return s

def GenJsApiMapGlobalVarSetterAndGetter(global_vars):

  s = ""

  for idx, var in enumerate(global_vars):
    varName = var["name"].capitalize() + "V8"

    getFuncName = 'get' + varName
    s += \
'''
  map['%s'] = function() {
    self.handle.funcReq(self.io.%s, '%s');
  };
'''%(getFuncName, getFuncName, getFuncName)

    if var["constant"] == 1:
      continue

    setFuncName = 'set' + varName
    s += \
'''
  map['%s'] = function() {
    self.handle.funcReq(self.io.%s, '%s');
  };
'''%(setFuncName, setFuncName, setFuncName)

  return s

def GenFuncJsApi(func):
  if not IsV8FuncGen(func):
    return ""
  funcName = func["name"]
  return \
'''
  /**
   * @function IO#%s
   * @type function%s%s
   * @instance
   */
  self.%s = function() {
    return self.submit.funcReq('%s', arguments);
  };
''' % (funcName, \
       AddIndent(GenFuncParamsJsDoc(func), 2),
       AddIndent(GenFuncReturnJsDoc(func), 2),\
       funcName, funcName)

def GenFuncJsApiMap(func):
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
''' % (module)

  servStr = \
'''
  /****************************************
             %s
  ****************************************/
''' % (module)

  GenTypedefCallBackJsDocTypesHT()
  for c in cppHeader.classes:
    if cppHeader.classes[c]["declaration_method"] == "class":
      clientStr += GenClassJsApi(c, cppHeader.classes[c])
      servStr += GenClassJsApiMap(c, cppHeader.classes[c])

  clientStr += GenJsConst(cppHeader.defines)
  clientStr += GenJsEnumConst(cppHeader.enums)

  clientStr += GenJsApiGlobalVarSetterAndGetter(cppHeader.global_vars)
  servStr += GenJsApiMapGlobalVarSetterAndGetter(cppHeader.global_vars)

  #generate map of functions
  for idx, func in enumerate(cppHeader.functions):
    clientStr += GenFuncJsApi(func)
    servStr += GenFuncJsApiMap(func)

  f = configSys.OUTPUT_COMP_PATH + "/" + configSys.TARGET +".js"
  fp = open(f, "a")
  fp.write(clientStr)
  printDbg( "generate " + f)

  f = configSys.OUTPUT_SERVER_PATH + "/" + configSys.TARGET +".js"
  fp = open(f, "a")
  fp.write(servStr)
  printDbg( "generate " + f)

