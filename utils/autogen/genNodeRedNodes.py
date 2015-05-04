import os
import globalVar
import config
from util import *

def GenLoopCnt(idx):
  return "idx%s" %(idx)
def GetNodeRedFuncName(funcName):
  return funcName.capitalize() + "_GEN"

def GetNodeRedNodeName(funcName):
  return funcName[0].lower() + funcName[1:] + "_GEN"

def GetNodeRedFileName(funcName):
  printDbg("funcName" + funcName)
  return GetNodeRedNodeName(funcName)

def GetUtilModuleFile():
  #return os.path.relpath(config.ATLAS_PATH + '/iot/lib/red-util.js', config.NODERED_PATH);
  return 'red-util'
  
def GetUtilModuleName():
  return "RedUtil"

def GetUtilModuleVarName():
  return "redUtil"

def GetVarType(needNewVar):
  if needNewVar:
    return "var "
  else:
    return ""

def GenNodeRedCommonArgTran(param, idx, argJSName, argJSONName, funcName):
  argJSType = GetJSType(param["type"])
  argConvFunc = ""
  if argJSType == "char":
    ch = argJSONName.strip()
    assert len(ch) == 1, \
           "%d param should be one character in function '%s'" %(idx, funcName)
    s += \
'''      var %s = %s.trim().charCodeAt(0);
''' %(argJSName, argJSONName)
  else:
    if argJSType == "int":
      argConvFunc = "parseInt"
    elif argJSType == "float":
      argConvFunc = "parseFloat"
    else:
      assert 0, "Invalid param type %s (%s) in func %s!" %(param["type"], argJSName, funcName)

    s += \
'''      %s = %s(%s);
''' %(argJSName, argConvFunc, argJSONName)
 
numString = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th",\
            "11"]

def GenNodeRedArrayArgTran(arg, idx, argJSName, argJSONName, needNewVar):
  argBasicType = GetNoQualifierType(GetBasicType(arg))
  argBasicJSType = GetJSType(argBasicType)
  
  argUniqType = GetIdenticalType(arg["type"])
  argUniqBasicType = GetIdenticalType(argBasicType)

  # Handle parameter type "void *" as "int *"
  if argUniqBasicType == "void":
    argUniqBasicType = "int"
    argBasicJSType = "int"
    argType = "int *"
  
  loopcnt = GenLoopCnt(idx)

  elementJSName = "%s[%s]" %(argJSName, loopcnt)
  elementJSONName = "%s[%s]" %(argJSONName, loopcnt)

  if IsStructArg(argUniqBasicType):
    elementTran = GenNodeRedStructArgTran(argUniqBasicType, \
        idx, elementJSName, elementJSONName, False)
  else:
    elementTran = GenNodeRedCommonArgTran(argBasicType, \
        elementJSName, elementJSONName, False)

  s = \
'''
%s%s = [];
for (var %s = 0; %s < %s.length; %s++) {
%s
}
'''%(GetVarType(needNewVar), argJSName, \
    loopcnt, loopcnt, argJSONName, loopcnt,
    AddIndent(elementTran, 2))

  return s

def GenNodeRedStringArgTran(arg, argJSName, argJSONName, needNewVar):
  s = \
'''%s%s = %s.%s(%s)
''' %(GetVarType(needNewVar), argJSName, GetUtilModuleVarName(), 
      "jsonStringArrayParse", argJSONName)
  return s

def GenNodeRedCommonArgTran(argType, argJSName, argJSONName, needNewVar):
  argJSType = GetJSType(argType)
  
  if argJSType == "char":
    convFunc = "jsonCharParse"
  elif argJSType == "int":
    convFunc = "jsonIntegerParse"
  elif argJSType == "float":
    convFunc = "jsonFloatPointerParse"
  else:
    assert(0)

  s = \
'''%s%s = %s.%s(%s);
''' %(GetVarType(needNewVar), argJSName, GetUtilModuleVarName(), convFunc, argJSONName)
  return s

def GenNodeRedEnumArgTran(argType, argJSName, argJSONName, needNewVar):
  argJSType = GetJSType(argType)
  
  convFunc = "jsonIntegerParse"

  s = \
'''%s%s = %s.%s(%s);
''' %(GetVarType(needNewVar), argJSName, GetUtilModuleVarName(), convFunc, argJSONName)
  return s

def GenNodeRedStructArgTran(argType, idx, argJSName, argJSONName, needNewVar):
  argType = GetNoQualifierType(argType)

  if (not IsStructArg(argType)):
    return s

  argStructName = re.sub(r'^struct ', '', argType)
  cls = GetClass(argStructName)

  s = \
'''%s%s = {}
''' %(GetVarType(needNewVar), argJSName)

  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldJSName = argJSName + "[\"" + fldName + "\"]"
    fldJSONName = argJSONName + "[\"" + fldName + "\"]"

    if (prop["function_pointer"] != 0 and len(prop["function_pointer"]) > 0) :
      s +=""
    else:
      s += GenNodeRedArgTran(prop, "%s_%s"%(idx, idxs), fldJSName, fldJSONName, False)

  return s;

def GenNodeRedFPArgTran(arg, idx, argJSName, argFPStr):
  s = \
'''
// Get function argument
var arg%d = %s.normalCallbackArg(msg, %d, %s)
''' % (idx, GetUtilModuleVarName(), idx, argFPStr)

  return s

def GenNodeRedArgTran(arg, idx, argJSName, argJSONName, needNewVar):
  argType = GetNoQualifierType(arg["type"])
  argBasicType = GetNoQualifierType(GetBasicType(arg))

  if argType == "void":
    return ""
  
  if (arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0) :
    s = GenNodeRedFPArgTran(arg, idx, argJSName, argJSONName)
  elif IsClassArg(argBasicType):
    s = GenNodeRedClassArgTran(arg, argJSName, argJSONName)
  elif IsEnumArg(argType):
    s = GenNodeRedEnumArgTran(argType, argJSName, argJSONName, needNewVar)
  elif (arg["pointer"] == 1 or arg["array"] == 1):
    if GetIdenticalType(argBasicType) == "char":
      s = GenNodeRedStringArgTran(argType, argJSName, argJSONName, needNewVar)
    else:
      s = GenNodeRedArrayArgTran(arg, idx, argJSName, argJSONName, needNewVar)
  elif IsStructArg(argType):
    s = GenNodeRedStructArgTran(argType, idx, argJSName, argJSONName, needNewVar)
  else:
    s = GenNodeRedCommonArgTran(argType, argJSName, argJSONName, needNewVar)

  return s

def GenNodeRedArgTrans(func):
  funcName = func["name"]
  params = func["parameters"] 
  
  if len(params) == 0:
    return ""
  
  s = \
'''
// extract arguments from msg
var args = redUtil.msgToArgs(msg);
'''
  
  for idx, param in enumerate(params):
    if param["type"] == "void":
      return ""

    argJSType = GetJSType(param["type"])
    argJSName = GenArgName(idx, "arg")
    argJSONName = GenArgArrayName(idx)
    if (idx < len(numString)):
      idxStr = numString[idx]
    else:
      idxStr = idx
    s += \
'''
//if (!args.hasOwnProperty("%d"))
  //throw Error("Input string should have '%d' properties as the %s parameter of function '%s'.");
''' %(idx, \
      idx, idxStr, funcName)
 
    s += GenNodeRedArgTran(param, idx, argJSName, argJSONName, True);
      
  return s  

def GenNodeRedCall(func):
  msgCnt = 0
  retIdenticalType = GetIdenticalType(func["rtnType"]["type"])
  if retIdenticalType == "" or retIdenticalType == "void":
    s = "\n"
  else:
    s = "\nvar res = "
  s += "%s.%s;" % (GetIOInstanceName(), GenCall(func))
  
  return s

def GenNodeRedCallAndSendMsg(func):
  msgCnt = 0
  retIdenticalType = GetIdenticalType(func["rtnType"]["type"])
  if retIdenticalType == "" or retIdenticalType == "void":
    s = \
'''
%s.%s;
''' % (GetIOInstanceName(), GenCall(func))
  else:
#     msgCnt += 1
#     s = \
# '''
# var res = %s.%s;
# msg.payload = JSON.stringify(res);
# ''' % (GetIOInstanceName(), GenCall(func))
 
#   # Send other message (pointer relation)
#   for idx, param in enumerate(func["parameters"]):
#     if param["pointer"] + param["array"] >= 1:
#       argJSName = GenArgName(idx, "arg")
#       s += \
# '''
# %s = {}
# %s.payload = JSON.stringify(%s);
# ''' %(GetMsgName(msgCnt), \
#       GetMsgName(msgCnt), argJSName)
#       msgCnt += 1
  
#   if msgCnt == 1:
#     s += \
# '''  
# node.send(msg);'''
#   elif msgCnt > 1:
#     msgSeq = ""
#     for idx in range(msgCnt):
#       msgSeq += GetMsgName(idx)
#       if idx != msgCnt - 1:
#         msgSeq += ","

#     s += \
# '''
# node.send([%s]);''' %(msgSeq)
    s = \
'''
var res = %s.%s;
%s.send({
  'payload': res,
  'iot': {
    'method': msg.iot.method,
    'return': res
  }
});
'''% (GetIOInstanceName(), GenCall(func), GetUtilModuleVarName())
  
  return s


def GetMsgName(msgCnt):
  if msgCnt == 0:
    msgName = "msg"
  else:
    msgName = "msg%d" %(msgCnt + 1)
  return msgName


def GetIOInstanceName():
  return "io"

def GenNodeRedFuncHtmlFile(className, func, funcRename):
  nodeName = GetNodeRedNodeName(funcRename)
  
  outputCnt = 1
  for arg in func["parameters"]:
    if (arg["pointer"] + arg["array"]) >= 1:
      if not(arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0) :
        outputCnt += 1

  s = \
'''
<!-- %s -->
<script type="text/javascript">
  RED.nodes.registerType('%s',{
    category: 'atlas',
    color: '#c7e9c0',
    defaults: {
      name: {value:"%s"}
    },
    inputs:1,
    outputs:%d,
    icon: "function.png",
    label: function() {
      return this.name;
    }
  });
</script>

<script type="text/x-red" data-template-name="%s">
  <div class="form-row">
  <label for="node-input-name"><i class="icon-tag"></i> Name</label>
  <input type="text" id="node-input-name" placeholder="Name">
  </div>
</script>

<script type="text/x-red" data-help-name="%s">
  <p>A function node: %s</p>
</script>
''' %(nodeName, nodeName, nodeName, outputCnt, nodeName, nodeName, func["debug"])

  return s

def GenNodeRedFuncJSFile(className, func, funcRename):
  s = \
'''
// C-Function: %s
function %s(config) {
  RED.nodes.createNode(this,config);
  var node = this;
  var %s = new %s(node, config);
  this.on('input', function(msg) {

    // Validate the msg 
    if(!%s.isValid(msg))
      return;
''' %( \
      func["debug"], \
      GetNodeRedFuncName(funcRename), \
      GetUtilModuleVarName(), GetUtilModuleName(), \
      GetUtilModuleVarName())

  s += AddIndent(GenNodeRedArgTrans(func), 4)
  
  # call JS-addon Code & send return value message 
  s += AddIndent(GenNodeRedCallAndSendMsg(func), 4)

  s += \
'''
  });
}
RED.nodes.registerType("%s", %s);
'''%(GetNodeRedNodeName(funcRename), GetNodeRedFuncName(funcRename))
  
  return s

def GenFuncRename(func):
  s = func["name"]
  for idx, param in enumerate(func["parameters"]):
    if param["type"] == "void":
      s += "_void"
      continue

    paramType = GetBasicType(param)
    newParamType = paramType.strip()
    newParamType = newParamType.replace(" ", "")
    if param["pointer"] >= 1:
      for i in range(param["pointer"]):
        newParamType += "Ptr"
    if param["array"] >= 1:
      newParamType += "Arr"
    s += "_"
    s += newParamType

  return s

def GenNodeRedHtmlFile(className, func):
  s = ""
  if func["override"]:
    for f in func["funcs"]:
      if CheckSanity(f) == True:
        funcRename = GenFuncRename(f)
        s += GenNodeRedFuncHtmlFile(className, f, funcRename)
  else:
    if CheckSanity(func):
      s = GenNodeRedFuncHtmlFile(className, func, func["name"])
  
  return s

def GenNodeRedJSFile(className, func):
  s = ""
  if func["override"]:
    for f in func["funcs"]:
      if CheckSanity(f) == True:
        funcRename = GenFuncRename(f)
        s += GenNodeRedFuncJSFile(className, f, funcRename)
  else:
    if CheckSanity(func):
      s = GenNodeRedFuncJSFile(className, func, func["name"])
  
  return s

def GenNodeRedNodes(module, cppHeader):
  printDbg("GenNodeRedNodes:")
  printDbg("transfering " + module)

  mkdir(config.NODERED_PATH)

  for c in cppHeader.classes:
    printDbg("class function convertion is not support for current version.")
    break
    classT = cppHeader.classes[c]
    if (classT["abstract"] == False) and (classT['declaration_method'] == "class"):
      s += GenClass(c, cppHeader.classes[c])
  
  # Generate JS file
  jsFile =  GetNodeRedFileName(module) + ".js"
  printDbg("generate " + jsFile)
  f = config.NODERED_PATH + "/" + jsFile
  fp = open(f, "w")
  
  s = \
'''var IOLIB = require('./%s');

var %s = new IOLIB.IO({
  log: true,
  quickInit: false
});

var %s = require('%s')

module.exports = function(RED) {
''' %(os.path.relpath(config.INSTALL_DIR, config.NODERED_PATH), \
      GetIOInstanceName(), \
      GetUtilModuleName(), GetUtilModuleFile())

  for func in cppHeader.functions:
    s += AddIndent(GenNodeRedJSFile("", func), 2)

  s += '''
}'''
  fp.write(s)
  fp.close()
  
  # Generate html file
  htmlFile =  GetNodeRedFileName(module) + ".html"
  printDbg("generate " + htmlFile)
  f = config.NODERED_PATH + "/" + htmlFile
  fp = open(f, "w")
  
  s = ""
  for func in cppHeader.functions:
    s += GenNodeRedHtmlFile("", func)
  
  fp.write(s)
  fp.close()

def NodeInitFuncSuffix():
  return "Init"
def NodeOnDataFuncSuffix():
  return "OnData"
def NodeReleaseFuncSuffix():
  return "Release"
def NodeConfigStructSuffix():
  return "Config"

def SplitNodeComponentName(ComName):
  if ComName.endswith(NodeInitFuncSuffix()):
    return ComName.partition(NodeInitFuncSuffix())
  if ComName.endswith(NodeOnDataFuncSuffix()):
    return ComName.partition(NodeOnDataFuncSuffix())
  if ComName.endswith(NodeReleaseFuncSuffix()):
    return ComName.partition(NodeReleaseFuncSuffix())
  if ComName.endswith(NodeConfigStructSuffix()):
    return ComName.partition(NodeConfigStructSuffix())
  
  assert 0, "Unexpected Component name %s" %(ComName)
  return ComName

def IsMacroDefined(macroName, cppHeader):
  for define in cppHeader.defines:
    macros = IsValidMacro(define)
    if len(macros) != 0 and macroName == macros[0]:
      return True
  return False


def HaveDefaultValueForStructField(structType, cppHeader):
  s = ""
  structType = GetNoQualifierType(structType)

  if (not IsStructArg(structType)):
    return s

  argStructName = re.sub(r'^struct ', '', structType)
  cls = GetClass(argStructName)

  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldMacroName = argStructName + "_" + fldName
    if not IsMacroDefined(fldMacroName, cppHeader):
      printErr("macro %s is not defined, which is the default value of field %s:%s." \
               %(fldMacroName, argStructName, fldName))
      return False

  return True
    

def IsValidInitFunc(func, cppHeader):
  for idx, para in enumerate(func["parameters"]):
    if idx == 0:
      if not IsStructArg(para["type"]):
        printErr("First parameter type of %s must be struct." %func["name"])
        return False
      if not (HaveDefaultValueForStructField(para["type"], cppHeader)):
        printErr("First parameter of %s must have default value." %func["name"])
        return False
    continue

    if not (para["function_pointer"] != 0 and len(para["function_pointer"]) > 0):
      printErr("parameters of func %s shoule be (struct, cb, cb, cb, ...)." %func["name"])
      return False
  return True

def GatherNodeInfo(module, cppHeader):
  printDbg("GetherNodeInfo:")

  for c in cppHeader.classes:
    printDbg("class function convertion is not support for current version.")
    break
    classT = cppHeader.classes[c]
    if (classT["abstract"] == False) and (classT['declaration_method'] == "class"):
      s += GenClass(c, cppHeader.classes[c])
  
  NodeGroup = {}
  
  init = NodeInitFuncSuffix()
  onData = NodeOnDataFuncSuffix()
  release = NodeReleaseFuncSuffix()
  struct = NodeConfigStructSuffix()

  for func in cppHeader.functions:
    funcName = func["name"]
    funcNameSplits = SplitNodeComponentName(funcName)
    nodeName = funcNameSplits[0]
    funcNameSuffix = funcNameSplits[1]
    if (funcNameSuffix == init) and not IsValidInitFunc(func, cppHeader):
      continue
      
    if NodeGroup.has_key(nodeName):
      NodeInfo = NodeGroup[nodeName]
      if NodeInfo[funcNameSuffix] == 0:
        NodeInfo[funcNameSuffix] = func
      else:
        assert 0, "dumplicate definition of %s" %funcName
    else:
      NodeGroup[nodeName] = {init:0, onData:0, release:0, struct:0}
      NodeGroup[nodeName][funcNameSuffix] = func

  for node in NodeGroup.keys():
    funcs = NodeGroup[node]
    initFunc = funcs[NodeInitFuncSuffix()]
    onDataFunc = funcs[NodeOnDataFuncSuffix()]
    releaseFunc = funcs[NodeReleaseFuncSuffix()]
    if initFunc == 0:
      printErr("Function 'init' is not defined for node %s" %node) 
      del NodeGroup[node]
      continue
    if onDataFunc == 0:
      printErr("Function 'onData' is not defined for node %s" %node) 
      del NodeGroup[node]
      continue
    if releaseFunc == 0:
      printErr("Function 'release' is not defined for node %s" %node) 
      del NodeGroup[node]
      continue

  return NodeGroup

def GenGatheredNodeRedNodes(module, cppHeader):
  printDbg("GenGatheredNodeRedNodes:")
  printDbg("transfering " + module)
  
  mkdir(config.NODERED_PATH)

  NodeGroup = GatherNodeInfo(module, cppHeader)
  
  GenGatheredNodeRedJsFile(NodeGroup)
  GenGatheredNodeRedHtmlFile(NodeGroup, cppHeader)
  
def GenGatheredNodeRedHtmlFile(NodeGroup, cppHeader):
  for node in NodeGroup.keys():
    funcs = NodeGroup[node]
    initFunc = funcs[NodeInitFuncSuffix()]
    onDataFunc = funcs[NodeOnDataFuncSuffix()]
    releaseFunc = funcs[NodeReleaseFuncSuffix()]
    configType = initFunc["parameters"][0]["type"]

    # Generate HTML file
    htmlFile =  node + ".html"
    printDbg("generate " + htmlFile)
    f = config.NODERED_PATH + "/" + htmlFile
    fp = open(f, "w")
      
    s = \
'''
<!-- %s -->
<script type="text/javascript">
  RED.nodes.registerType('%s',{
    category: 'atlas',
    color: '#c7e9c0',
    defaults: {
      name:     {value: '%s'},
      %s
    },
    inputs:1,
    outputs: %d, // how many callbacks of cameraInit
    icon: "function.png",
    label: function() {
      return this.name;
    }
  });
</script>

<script type="text/x-red" data-template-name="%s">
  %s
</script>

<script type="text/x-red" data-help-name="%s">
  <p> %s help </p>
</script>
''' %(node, node, node, 
      AddIndent(configDefaultValueStr(node, configType, cppHeader), 6),
      initFuncOutputNums(initFunc), node, 
      configFieldStr(node, configType, cppHeader), 
      node, node)

    fp.write(s)
    fp.close()

  return

def initFuncOutputNums(initFunc):
  return len(initFunc["parameters"]) - 1

def configDefaultValueStr(node, configType, cppHeader):
  s = ""
  configType = GetNoQualifierType(configType)

  if (not IsStructArg(configType)):
    return s

  argStructName = re.sub(r'^struct ', '', configType)
  cls = GetClass(argStructName)

  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldMacroName = argStructName + "_" + fldName
    
    for define in cppHeader.defines:
      macros = IsValidMacro(define)
      if len(macros) != 0 and fldMacroName == macros[0]:
        fldMacroVal = macros[1]
        break;
    s += \
'''
%s : {value : %s}''' %(fldName, fldMacroVal)
    if idxs != len(props) - 1:
      s += ","

  return s

def configFieldStr(node, configType, cppHeader):
  configType = GetNoQualifierType(configType)

  if (not IsStructArg(configType)):
    return s

  argStructName = re.sub(r'^struct ', '', configType)
  cls = GetClass(argStructName)

  s = \
'''<div class="form-row">
<label for="node-input-name"><i class="icon-tag"></i> </label>
<input type="text" id="node-input-name" placeholder="Name">
</div>
'''

  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    
    s += \
'''
<div class="form-row">
<label for="node-input-%s"><i class="icon-tag"></i> %s</label>
<input type="text" id="node-input-%s">
</div>
''' %(fldName, fldName, fldName)

  return s

def GenGatheredNodeRedJsFile(NodeGroup):
  init = NodeInitFuncSuffix()
  onData = NodeOnDataFuncSuffix()
  release = NodeReleaseFuncSuffix()
  struct = NodeConfigStructSuffix()
  for node in NodeGroup.keys():
    funcs = NodeGroup[node]
    initFunc = funcs[NodeInitFuncSuffix()]
    onDataFunc = funcs[NodeOnDataFuncSuffix()]
    releaseFunc = funcs[NodeReleaseFuncSuffix()]
    
    # Generate JS file
    jsFile =  node + ".js"
    printDbg("generate " + jsFile)
    f = config.NODERED_PATH + "/" + jsFile
    fp = open(f, "w")
  
    s = \
'''var IOLIB = require('./%s');

var %s = new IOLIB.IO({
  log: true,
  quickInit: false
});

module.exports = function(RED) {
  /**************************************************
                        %s
   **************************************************/

  function %s(config) {
  
    RED.nodes.createNode(this,config);
    var node = this;

    var %s = require('%s')
    var %s = new %s(node, config);
''' %(os.path.relpath(config.INSTALL_DIR, config.NODERED_PATH), \
      GetIOInstanceName(), \
      node, node, \
      GetUtilModuleName(), GetUtilModuleFile(), \
      GetUtilModuleVarName(), GetUtilModuleName())
  
  
    s += AddIndent(GenInitFuncConv(node, initFunc), 4)
    s += AddIndent(GenOnDataFuncConv(node, onDataFunc), 4)
    s += AddIndent(GenReleaseFuncConv(node, releaseFunc), 4)
    s += \
'''
  }
  RED.nodes.registerType("%s", %s);
}
''' %(node, node)
    fp.write(s)
    fp.close()

def GenCbFuncListBefore(idx):
  s = ""
  for index in range(1, idx):
    s += "null, " 
  return s

def GenCbFuncListAfter(idx, num):
  s = ""
  for index in range(idx + 1, num):
    s += ", null"
  return s

def GenerateConfigFunc(node, configType, configFuncName):
  
  configType = GetNoQualifierType(configType)

  if (not IsStructArg(configType)):
    return s

  argStructName = re.sub(r'^struct ', '', configType)
  cls = GetClass(argStructName)

  s = \
'''
// configure function
function %s(src) {
  var dst = {};
''' % (configFuncName)

  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldMacroName = argStructName + "_" + fldName
    s += AddIndent(GenNodeRedArgTran(prop, idxs, "dst%d" %(idxs), "src['%s']" %(fldName), True), 2)
    s += \
'''dst["%s"] = dst%s || %s.%s;
''' %(fldName, idxs, GetIOInstanceName(), fldMacroName)

  s += \
'''
  return dst;
}
'''
  return s

# func(struct, cb, cb, cb)
def GenOnDataFuncConv(node, func):
  s = \
'''
// call onData function
node.on('input', function(msg) {
  // Validate the msg 
  if(!%s.isValid(msg))
    return;
''' %(GetUtilModuleVarName())

  s += AddIndent(GenNodeRedArgTrans(func), 2)
  
  # call JS-addon Code & send return value message 
  s += AddIndent(GenNodeRedCall(func), 2)

  s += \
'''
});
'''
  return s

def GenReleaseFuncConv(node, func):
  s = \
'''
// call release function
node.on('close', function() {
  %s.%s()
})
''' %(GetIOInstanceName(), func["name"])
  return s

def GenInitFuncConv(node, func):
  configType = func["parameters"][0]["type"]
  configFuncName = re.sub(r'^struct ', '', configType) + "New"
  
  s = GenerateConfigFunc(node, configType, configFuncName)

  s += \
'''
// call initialize %sInit
var arg0 = %s(config);
console.log('init %s' + JSON.stringify(arg0));
''' % (node, configFuncName, node)
  
  paraNum = len(func["parameters"])
  for idx in range(paraNum):
    if idx == 0: continue
    s += \
'''var arg%d = function() {
  node.send([
    %s{'payload' : arguments[0]}%s
  ])
}
''' %(idx, \
      GenCbFuncListBefore(idx), \
      GenCbFuncListAfter(idx, paraNum))

  argList = ""
  for idx in range(paraNum):
    argList += "arg%d" %idx
    if idx != paraNum - 1:
      argList += " ,"
 
  s += \
'''
redUtil.checkInit(%s.%s(%s));
''' % (GetIOInstanceName(), func["name"], argList)
  return s
