import os
import globalVar
from config import *
from util import *

def GetV8ClassName(className):
  return className + "V8"

def GenArgName(idx, args):
  return "arg%d"%idx

def GenArgArrayName(idx):
  return "args[%d]"%idx

def GetV8FuncName(func):
  name = func["name"]
  if re.match(r"operator.*", name):
    return name[0:8] + " " + name[8:]
  else:
    return name + "V8"

def GenExport(module):
  s = \
'''
void InitV8(Handle<Object> exports) {

    Local<Function> constructFn = FunctionTemplate::New(%s)->GetFunction();
    exports->Set(v8::String::NewSymbol("%s"), constructFn);
}

NODE_MODULE(%s, Init);
'''%(module, module, module)
  return s

def GenSetFunc(obj, func):
  s = \
'''
    %s->Set(v8::String::NewSymbol("%s"),
           FunctionTemplate::New(%s)->GetFunction());
'''%(obj, func["name"], GetV8FuncName(func))
  return s

def GetFuncDesc(func):
  if func.has_key("override") and func["override"]:
    s = "// %s" % func["name"]
  else:
    s = "// %d: %s"% (func["line_number"], func["debug"])

  return s

def GenSetMemberFunc(funcs):
  s = "\nstatic void SetMemberFunc(Handle<Object> obj) {"
  for func in funcs:
    flag = IsV8FuncGen(func)
    if flag:
      s += GenSetFunc("obj", func)
  s += "}\n"
  return s

def GenArgList(func, withType):
  s =""
  args = func["parameters"]
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue

    argName = GenArgName(idx, args)

    if withType: 
      if (arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0):
        s += GenFuncPointArgDef(arg, idx, argName)
      else:
        s += "%s %s" % (arg["type"], argName)
    else:
      s += "%s" % (argName)

    if idx != (len(args) - 1):
      s += ", "

  return s

def GenCallArgList(func):
  s =""
  args = func["parameters"]
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue

    s += "%s" % (GenArgName(idx, args))

    if idx != (len(args) - 1):
      s += ", "

  return s

def GenArgCheck(arg, argName):
  argBasicType = GetBasicType(arg)
  if (arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0) :
    typeCheck = "IsFunction"
  elif IsStructArg(argBasicType) or IsClassArg(argBasicType):
    typeCheck = "IsObject"
  elif IsEnumArg(argBasicType):
    typeCheck = "IsInt32"
  elif (arg["pointer"] == 1 or arg["array"] == 1):
    if (GetIdenticalType(arg["type"]) == "char*"):
      return "(%s->IsString() || %s->IsObject())" %(argName, argName)
    else:
      typeCheck = "IsArray"
  else:
    typeCheck = GetV8TypeCheck(arg["type"]);

  s = "%s->%s()" % (argName, typeCheck)
  return s

def GenArgsCheckExpress(func) :
  s =""
  args = func["parameters"]
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    s += GenArgCheck(arg, GenArgArrayName(idx))

    if idx != (len(args) - 1):
      s += " && "

  return s

def GenFuncPointArgDef(arg, idx, argCName):
  if (len(arg["function_pointer"]) > 0) :
    type_t = GetNoQualifierType(arg["type"])
    if type_t.find("(") == -1:           # typedef
      return "%s arg%d;" %(type_t, idx)
    else:
      FPType = arg["function_pointer"]   # no typedef
      s = GetNoQualifierType(FPType["rtnType"]["type"])
      s += '''(*%s) (''' %(argCName)
      for idx, para in enumerate(FPType["paraTypes"]):
        s += para["type"]
        if idx != (len(FPType["paraTypes"]) - 1):
          s += ","
        else:
          s += ")"
      return s
  else:
    raise "GenFuncPointArgDef: unexpected arg type."

def GenLoopCnt(idx):
  return "index%s" %(idx)

def GenArrayLen(idx):
  return "len%s" %(idx)

def GenStringArgReturn(arg, idx, argCName, argV8Name, argMiddleName):
  s = ""
  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  argUniqType = "char *"
  argUniqBasicType = "char"

  loopcnt = GenLoopCnt(idx)
  arrayLen = GenArrayLen(idx)

  s = \
'''
if (%s->IsString()) {
    v8::String::AsciiValue %s(%s->ToString());
    const char *oldStr = *%s;
    for (%s = 0; %s < %s; %s++) {
        if (oldStr[%s] != %s[%s])
            V8_ASSERT(false, "String %s is Changed in C function, \\
Please Use Buffer or Integer Array to map 'char *' in JS");
    }
} else {
    Local<Array> %s = Local<Array>::Cast(%s);
    for (%s = 0; %s < %s; %s++) {
        %s->Set(%s, %s);
    }
}
'''%( \
    argV8Name, \
    argMiddleName, argV8Name, \
    argMiddleName, \

    loopcnt, loopcnt, arrayLen, loopcnt, \
    loopcnt, argCName, loopcnt, \
    argCName, \
#else
    argMiddleName, argV8Name,\
    loopcnt, loopcnt, arrayLen, loopcnt, \
    argMiddleName, loopcnt, GetV8Value("%s[%s]" %(argCName, loopcnt), argUniqBasicType))

  return s

def GenArrayArgReturn(arg, idx, argCName, argMiddleName):
  s = ""

  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  argUniqType = GetIdenticalType(argType)
  argUniqBasicType = GetIdenticalType(argBasicType)

  # Handle parameter type "void *" as "int *"
  if argUniqBasicType == "void":
    argUniqBasicType = "int"

  loopcnt = GenLoopCnt(idx)
  s += \
'''for (%s = 0; %s < %s; %s ++)
  %s->Set(%s, %s);
'''%(loopcnt, loopcnt, GenArrayLen(idx), loopcnt, \
   argMiddleName, loopcnt, GetV8Value("%s[%s]" %(argCName, loopcnt), argUniqBasicType))
  return s

def GenStructArgReturn(arg, idx, argCName, argV8Name, argMiddleName):
  s = ""
#  if arg["pointer"] != 1:
#    return s

  if (arg["function_pointer"] != {} and \
      arg["function_pointer"] != 0) :
    return s

  argType = GetNoQualifierType(arg["type"])
  argBasicType = GetNoQualifierType(GetBasicType(arg))

  if (not IsStructArg(argBasicType)):
    return s

  if argType == argBasicType:
    join = "."
  else:
    join = "->"

  argStructName = re.sub(r'^struct ', '', argBasicType)

  cls = GetClass(argStructName)

  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldType = prop["type"]
    fldBasicType = GetBasicType(prop)
    if (IsStructArg(fldBasicType)):
      objName = "%s_%d" %(argMiddleName, idxs)
      newObjName = objName + "t"
      s += GenStructArgReturn(prop, "%s%d" %(idx, idxs), \
             argCName + join + fldName, objName, newObjName)
    elif (prop["pointer"] == 1 or prop["array"] == 1):
      objName = "%s_%d" %(argMiddleName, idxs)
      newObjName = "%s_%dt" %(argMiddleName, idxs)
      if (GetIdenticalType(fldBasicType) == "char"):
        s += GenStringArgReturn(prop, "%s%d" %(idx, idxs), \
               argCName + join + fldName, objName, newObjName)
      else:
        s += GenArrayArgReturn(prop, "%s%d" %(idx, idxs), \
               argCName + join + fldName, newObjName)
    elif (IsEnumArg(fldType)):
      objName = GetV8Value(argCName + join + fldName, "int")
    else:
      objName = GetV8Value(argCName + join + fldName, GetIdenticalType(fldType))

    s += \
'''%s->ToObject()->Set(String::New("%s"), %s);

'''% (argV8Name, fldName, objName)
  return s

def GenArgReturn(idx, arg):
  if arg["pointer"] != 1 and arg["array"] != 1:
    return

  argBasicType = GetBasicType(arg)
  argCName = GenArgName(idx, arg)
  argV8Name = GenArgArrayName(idx)
  argMiddleName = "argV8_%s" %(idx)

  if (IsStructArg(argBasicType)):
    s = GenStructArgReturn(arg, idx, argCName, argV8Name, argMiddleName)
  elif (GetIdenticalType(argBasicType) == "char"):
    s = GenStringArgReturn(arg, idx, argCName, argV8Name, argMiddleName)
    globalVar.mallocObj.append(argCName)
  elif (IsClassArg(argBasicType)):
    s = ""
  else:
    s = GenArrayArgReturn(arg, idx, argCName, argMiddleName)
    globalVar.mallocObj.append(argCName)
  return s

def GenRetLoopCnt(idx):
  return "retIdx%s" %(idx)

def GenRetArrayLen(idx):
  return "retLen%s" %(idx)

def GenArrayReturn(rtn, idx, rtnCName, rtnArrayV8Name):
  s = ""
#  if rtn["pointer"] != 1:
#    return s

  rtnType = rtn["type"]
  rtnBasicType = GetBasicType(rtn)

  rtnUniqBasicType = GetIdenticalType(rtnBasicType)

  # Handle return type "void *" as "int *"
  if rtnUniqBasicType == "void":
    rtnUniqBasicType = "int"

  loopcnt = GenRetLoopCnt(idx)
  arrayLen = GenRetArrayLen(idx)
  arrayName = rtnArrayV8Name
  s = \
'''Local<Array> %s = Array::New();
int %s;
for (%s = 0; *(%s + %s) != 0; %s ++)
  %s->Set(%s, %s);
'''%(arrayName, \
    loopcnt,
    loopcnt, rtnCName, loopcnt, loopcnt, \
    arrayName, loopcnt, GetV8Value("%s[%s]" %(rtnCName, loopcnt), rtnUniqBasicType))
  return s

def GenCommonReturn(rtnType, rtnCName, rtnV8Name):
  rtnType = GetIdenticalType(rtnType)
  s = \
'''Handle<Value> %s = %s;
''' %(rtnV8Name, GetV8Value(rtnCName, rtnType))
  return s

def GenEnumReturn(rtnCName, rtnV8Name):
  s = \
'''Handle<Value> %s = %s;
''' %(rtnV8Name, GetV8Value(rtnCName, "int"))
  return s

def GenStringReturn(rtn, idx, rtnCName, rtnV8Name):
  s = \
'''Handle<Value> %s = v8::String::New((char*)%s);
''' %(rtnV8Name, rtnCName)
  return s

def GenStructReturn(rtn, idx, rtnCName, rtnV8Name):
  s = ""

  rtnType = GetIdenticalType(rtn["type"])
  rtnBasicType = GetIdenticalType(GetBasicType(rtn))

  if (not IsStructArg(rtnBasicType)):
    return ""

  if rtnType == rtnBasicType:
    join = "."
  else:
    join = "->"

  s += \
'''Local<Object> %s = Object::New();
''' % (rtnV8Name)

  rtnStructName = re.sub(r'^struct ', '', rtnBasicType)

  cls = GetClass(rtnStructName)
  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    objName = "%s_%d" %(rtnV8Name, idxs)
    s += GenFuncReturn(prop, "%s%d" %(idx, idxs), \
           rtnCName + join + fldName, objName)
    s += \
'''%s->Set(String::New("%s"), %s);

'''% (rtnV8Name, fldName, objName)
  return s

def GenFuncReturn(rtn, idx, rtnCName, rtnV8Name):
  rtnBasicType = GetBasicType(rtn)
  rtnUniqType = GetIdenticalType(rtn["type"])

  if (IsStructArg(rtnBasicType)):
    s = GenStructReturn(rtn, idx, rtnCName, rtnV8Name)
  elif (IsEnumArg(rtnUniqType)):
    s = GenEnumReturn(rtnCName, rtnV8Name)
  elif (rtnUniqType == "char*"):
    s = GenStringReturn(rtn, idx, rtnCName, rtnV8Name)
  elif (rtn["pointer"] == 1 or rtn["array"] == 1):
    s = GenArrayReturn(rtn, idx, rtnCName, rtnV8Name)
  else:
    s = GenCommonReturn(rtnUniqType, rtnCName, rtnV8Name)
  return s

def GenArgsReturn(func):
  args = func["parameters"]
  s = ""

  for idx, arg in enumerate(args):
    if arg["pointer"] != 1 and arg["array"] != 1:
      continue

    if (arg["function_pointer"] != {} and \
        arg["function_pointer"] != 0) :
      continue

    s += GenArgReturn(idx, arg)
  return s

def GenFPArgTran(arg, idx, argCName, argV8Name, needNewTargName):
  cnt = globalVar.FuncPointerCnt
  if needNewTargName:
    typeStr = GenFuncPointArgDef(arg, idx, argCName)
  else:
    typeStr = ""

  s = \
'''cbArray[%d] = Persistent<Function>::New(Local<Function>::Cast(%s));
%s;
%s = cbFunc%d;
''' %(cnt, argV8Name, \
  typeStr, \
  argCName, cnt)
  globalVar.FuncPointerHashtable[cnt] = arg["function_pointer"]
  globalVar.FuncPointerCnt += 1
  return s

def GenStringArgTran(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName):
  s = ""
  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  argUniqType = "char *"
  argUniqBasicType = "char"

  loopcnt = GenLoopCnt(idx)
  arrayLen = GenArrayLen(idx)

  if needNewTargName:
    s = \
'''%s *%s;''' %(argUniqBasicType, argCName)
  else:
    s = ""

  s += \
'''
int %s;
int %s;
if (%s->IsString()) {
    v8::String::AsciiValue %s(%s->ToString());
    %s = strlen(*%s) + 1;
    %s = (%s)malloc(%s * sizeof(%s));
    strcpy(%s, *%s);
} else {
    Local<Array> %s = Local<Array>::Cast(%s);
    %s = %s->Length() + 1;
    %s = (%s)malloc(%s * sizeof(%s));
    for (%s = 0; %s < %s - 1; %s++) {
        Local<Value> %s_%s = %s->Get(%s);
        V8_ASSERT(%s_%s->%s(), "%s[%%d] parameter error", %s);
        %s[%s] = (%s)%s;
    }
    %s[%s] = 0;
}'''%( \
    loopcnt, \
    arrayLen, \
    argV8Name, \
    argMiddleName, argV8Name, \
    arrayLen, argMiddleName, \
    argCName, argUniqType, arrayLen, argUniqBasicType, \
    argCName, argMiddleName, \
#else
    argMiddleName, argV8Name,\
    arrayLen, argMiddleName, \
    argCName, argUniqType, arrayLen, argUniqBasicType,\
    loopcnt, loopcnt, arrayLen, loopcnt, \
    argMiddleName, loopcnt, argMiddleName, loopcnt,\
    argMiddleName, loopcnt, GetV8TypeCheck(argUniqBasicType), argCName, loopcnt, \
    argCName, loopcnt, GetNoQualifierType(argBasicType), \
      GetCValue("%s_%s" %(argMiddleName, loopcnt), argUniqBasicType), \
    argCName, loopcnt)

  return s

def GenArrayArgTran(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName):
  s = ""

  argType = arg["type"]
  if arg["array"] == 1 and arg["pointer"] == 0:
    argType = arg["type"] + " *"

  argBasicType = GetBasicType(arg)

  argUniqType = GetIdenticalType(argType)
  argUniqBasicType = GetIdenticalType(argBasicType)

  # Handle parameter type "void *" as "int *"
  if argUniqBasicType == "void":
    argUniqBasicType = "int"
    argBasicType = "int"
    argType = "int *"

  loopcnt = GenLoopCnt(idx)
  arrayLen = GenArrayLen(idx)

  if needNewTargName:
    typeStr = \
'''%s%s;''' %(GetNoQualifierType(argType), argCName)
  else:
    typeStr = ""

  s = \
'''int %s;
Local<Array> %s = Local<Array>::Cast(%s);
int %s = %s->Length();
%s
%s = (%s)malloc(%s * sizeof(%s));
for (%s = 0; %s < (int)%s->Length(); %s++) {
  Local<Value> %s_%s = %s->Get(%s);
  V8_ASSERT(%s_%s->%s(), "%s[%%d] parameter error", %s);
  %s[%s] = (%s)%s;
}'''%(loopcnt, \
    argMiddleName, argV8Name,\
    arrayLen, argMiddleName, \
    typeStr, \
    argCName, GetNoQualifierType(argType), arrayLen, GetNoQualifierType(argBasicType), \
    loopcnt, loopcnt, argMiddleName, loopcnt, \
    argMiddleName, loopcnt, argMiddleName, loopcnt,\
    argMiddleName, loopcnt, GetV8TypeCheck(argUniqBasicType), argCName, loopcnt, \
    argCName, loopcnt, GetNoQualifierType(argBasicType), \
      GetCValue("%s_%s" %(argMiddleName, loopcnt), argUniqBasicType))

  return s

def GenCommonArgTran(arg, idx, argCName, argV8Name, needNewTargName):
  argType = arg["type"]
  argUniqType = GetIdenticalType(argType)

  if needNewTargName:
    typeStr = GetNoQualifierType(argType) + " "
  else:
    typeStr = ""

  s = \
'''%s%s = (%s)%s;
'''% (typeStr, argCName, GetNoQualifierType(argType), GetCValue(argV8Name, argUniqType))
  return s

def GenEnumArgTran(arg, idx, argCName, argV8Name, needNewTargName):
  argType = GetIdenticalType(arg["type"])
  argUniqType = "int" # use integer value to map enum value

  if needNewTargName:
    typeStr = argType + " "
  else:
    typeStr = ""

  s = \
'''%s%s = (%s)%s;
'''% (typeStr, argCName, argType, GetCValue(argV8Name, argUniqType))
  return s

def GenClassArgTran(arg, idx, argCName, argV8Name, needNewTargName):
  argType = GetIdenticalType(arg["type"])
  argBasicType = GetBasicType(arg)

  if needNewTargName:
    typeStr = argType + " "
  else:
    typeStr = ""

  s = \
'''%s%s = ObjectWrap::Unwrap<%sV8>(%s->ToObject())->getCClass();
'''% (typeStr, argCName, argBasicType, argV8Name)
  return s

def GenStructArgTran(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName):
  s = ""
  argType = GetNoQualifierType(arg["type"])
  argBasicType = GetNoQualifierType(GetBasicType(arg))

  if (not IsStructArg(argBasicType)):
    return s

  argStructName = re.sub(r'^struct ', '', argBasicType)
  cls = GetClass(argStructName)
  props = cls["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    objName = "%s_%d" %(argMiddleName, idxs)
    newObjName = "%s_%dt" %(argMiddleName, idxs)
    s += \
'''Local<Value> %s = %s->ToObject()->Get(String::New("%s"));
V8_ASSERT(%s, "%s.%s parameter error");
'''% (objName, argV8Name, fldName, \
      GenArgCheck(prop, objName), argCName, fldName)
    if (prop["function_pointer"] != 0 and len(prop["function_pointer"]) > 0) :
      s +=""
    else:
      s += GenArgTrans(prop, "%s%d"%(idx, idxs), "%s%d"%(argCName, idxs),\
          objName, newObjName, True)

    s += "\n"

  if argType == argBasicType:
    sName = argCName
  else:
    sName = argCName + "T"

  if needNewTargName:
    typeStr = GetNoQualifierType(argBasicType) + " "
  else:
    typeStr = ""

  s += \
'''%s%s = {''' %(typeStr, sName)
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fieldValue = "%s%d"%(argCName, idxs)
    if (prop["function_pointer"] != 0 and len(prop["function_pointer"]) > 0) :
      s +=""
    else:
      s += \
'''%s:%s''' %(fldName, fieldValue)
    if idxs != (len(props) -1):
      s += ", "
  s += "};\n"

  if argType != argBasicType:
    if needNewTargName:
      typeStr = GetNoQualifierType(argType)
    else:
      typeStr = ""

    s += \
'''%s%s = &%s;
''' %(typeStr, argCName, sName)

  return s

def GenArgTrans(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName):
  argType = GetNoQualifierType(arg["type"])
  argBasicType = GetNoQualifierType(GetBasicType(arg))

  if argType == "void":
    return ""

  if (arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0) :
    s = GenFPArgTran(arg, idx, argCName, argV8Name, needNewTargName)
  elif IsClassArg(argBasicType):
    s = GenClassArgTran(arg, idx, argCName, argV8Name, needNewTargName)
  elif IsStructArg(argBasicType):
    s = GenStructArgTran(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName)
  elif IsEnumArg(argType):
    s = GenEnumArgTran(arg, idx, argCName, argV8Name, needNewTargName)
  elif (arg["pointer"] == 1 or arg["array"] == 1):
    if GetIdenticalType(argBasicType) == "char":
      s = GenStringArgTran(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName)
    else:
      s = GenArrayArgTran(arg, idx, argCName, argV8Name, argMiddleName, needNewTargName)
  else:
    s = GenCommonArgTran(arg, idx, argCName, argV8Name, needNewTargName)

  return s

def GenArgsCheck(func):
  s = ""
  t = GenArgsCheckExpress(func)
  if len(t) != 0:
    s += \
'''
V8_ASSERT(%s, "parameters error!");
''' %(t)
  return s


def GenArgsTrans(func):
  args = func["parameters"]
  s = ""

  for idx, arg in enumerate(args):

    if GetIdenticalType(arg["type"]) == "void":
      continue

    if idx == 0:
      s += \
'''
// Convert V8 parameters to C++
'''

    argCName = GenArgName(idx, arg)
    argV8Name = GenArgArrayName(idx)
    argMiddleName = "argV8_%d" %(idx)

    s += GenArgTrans(arg, idx, argCName, argV8Name, argMiddleName, True)
    s += "\n"

  return s

def GenCall(func):
  return "%s(%s)" % (func["name"], GenCallArgList(func))

def GetRetName(retType):
  if retType == "" or retType == "void":
    return ""
  else:
    return "ret"

def MangleFuncName(func):
  return func["name"]

def GenFunc(func):
  if func["override"]:
    s = GenOverride("", func)
  else:
    s = GenMethod("", func)
  return s

def GenEnumConst(enums):
  
  s = \
'''

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {
'''
  for enum in enums:
    s += "\n    // enum %s" %(enum["name"]);
    for v in enum["values"]:
      s += \
'''
    obj->Set(v8::String::NewSymbol("%s"), Int32::New((int)%s));
'''%(v["name"], v["name"])

  s += "\n}"

  return s


def GenConst(defines):
  
  s = \
'''

// Const defined by macros
static void SetConst(Handle<Object> obj) {
'''
  for define in defines:
    macros = IsValidMacro(define)
    if len(macros) == 0:
      continue

    s += \
'''
    obj->Set(v8::String::NewSymbol("%s"),
'''%macros[0]

    if IsInt(macros[1]):
      s += "             Int32::New(%s));\n"% macros[1]
    elif (IsString(macros[1])):
      s += "             v8::String::New(%s));\n"% macros[1]
    else:
      s += "             Number::New(%s));\n"% macros[1]

  s += "\n}"

  return s

def GetGlobalClassVarCGetterFuncName(var):
  return "Get%sV8" %(var["name"].capitalize())

def GetGlobalClassVarV8GetterFuncName(var):
  return "get%sV8E" %(var["name"].capitalize())

def GetGlobalClassVarJSGetterFuncName(var):
  return "get%sV8" %(var["name"].capitalize())

def GetGlobalClassVarCSetterFuncName(var):
  return "Set%sV8" %(var["name"].capitalize())

def GetGlobalClassVarV8SetterFuncName(var):
  return "set%sV8E" %(var["name"].capitalize())

def GetGlobalClassVarJSSetterFuncName(var):
  return "set%sV8" %(var["name"].capitalize())

# The definition of Setter/Getter func is in cxx file where var is defined.
def GenGlobalClassVarGetterSetter(var):
  global thisSummary
  classType = GetIdenticalType(var["type"])
  classBasicType = GetIdenticalType(GetBasicType(var))
  classBasicV8Type = classType + "V8"
  varName = var["name"]
  varNameV8 = varName.capitalize() + "V8"

  if classType == classBasicType:
    refStr = "&"
    ptnStr = "*"
  else:
    refStr = ""
    ptnStr = ""

  getFuncName = GetGlobalClassVarCGetterFuncName(var)
  s = \
'''
Handle<Value> %s::%s(const Arguments& args) {
    HandleScope scope;
    %s *%s = new %s(%s%s);

    %s->Wrap(args.This());
    return args.This();
}
'''%(classBasicV8Type, getFuncName, \
     classBasicV8Type, varNameV8, classBasicV8Type, refStr, varName, \
     varNameV8)

  thisSummary["succGlobalClassVar"][getFuncName] = var

  if var["constant"] == 1:
    return s

  setFuncName = GetGlobalClassVarCSetterFuncName(var)
  s += \
'''
Handle<Value> %s::%s(const Arguments& args) {
    HandleScope scope;
    %s* obj = ObjectWrap::Unwrap<%s>(args.This());

    %s = %s(obj->m_val);
    return scope.Close(Undefined());
}
'''%(classBasicV8Type, setFuncName, \
     classBasicV8Type, classBasicV8Type, \
     varName, ptnStr)

  thisSummary["succGlobalClassVar"][setFuncName] =  var
  return s

def GenGlobalVarSetFunc():
  global thisSummary
  s = "\nstatic void SetGlobalVarFunc(Handle<Object> obj) {\n"
  for v8FuncName in thisSummary["succGlobalVar"]:
    exportFuncName = re.sub("^Get", "get", v8FuncName);
    exportFuncName = re.sub("^Set", "set", exportFuncName);

    s += \
'''
    obj->Set(v8::String::NewSymbol("%s"),
           FunctionTemplate::New(%s)->GetFunction());
'''%(exportFuncName, v8FuncName)

  s += "}\n"
  return s

def GenGlobalVarSetterAndGetter(global_vars):

  s = ""

  for idx, var in enumerate(global_vars):
    if idx == 0:
      s += \
'''

// Setter and Getter function for global variable
'''

    varType = var["type"]
    varName = var["name"]
    varNameV8 = varName + "V8"
    if not CheckArgSanity(var, False, True):
      thisSummary["failGlobalVar"].append(varName)
      continue

    if IsClassArg(GetBasicType(var)):
      s += GenGlobalClassVarGetterSetter(var)
    else:
      getFuncName = "Get%sV8" %(varName.capitalize())
      setFuncName = "Set%sV8" %(varName.capitalize())
      s += \
'''Handle<Value> %s(const v8::Arguments &args) {
    HandleScope scope;

%s
    return scope.Close(%s);
}
'''%(getFuncName, \
     AddIndent(GenFuncReturn(var, "", varName, varNameV8), 4),\
     varNameV8)

      thisSummary["succGlobalVar"].append(getFuncName)
      if var["constant"] == 1:
        continue

      s += \
'''
Handle<Value> %s(const v8::Arguments &args) {
    HandleScope scope;

    V8_ASSERT(%s, "parameter for global var '%s' error");
%s
    return scope.Close(Undefined());
}

'''%(setFuncName, \
     GenArgCheck(var, "args[0]"), varName, \
     AddIndent(GenArgTrans(var, 0, varName, "args[0]", "argV8_0", False), 4))

      thisSummary["succGlobalVar"].append(setFuncName)

  s += GenGlobalVarSetFunc()

  return s


def GenConstructorDecl(func):
  s = "explicit %s"% GetV8ClassName(func["name"])
  s += "(%s);\n"%GenArgList(func, True)
  return s 

thisSummary = {}

def GenClassDecl(name, c):
  global thisSummary
  s = \
'''
class %s: public node::ObjectWrap {

private:
    %s *m_val;
    ~%s() { };
    static v8::Handle<v8::Value> New(const v8::Arguments& args);
    static v8::Persistent<v8::Function> constructor;

public:
    explicit %s(%s *val);
    explicit %s() {};
    %s *getCClass() {
      return m_val;
    }
    static void Init(v8::Handle<v8::Object> exports);
'''%(GetV8ClassName(name), \
     name, \
     GetV8ClassName(name), \
     GetV8ClassName(name), name, \
     GetV8ClassName(name), \
     name)

  for m in c["methods"]["public"]:
    if m["name"] == name:
      continue

    flag = IsV8FuncGen(m)
    if flag:
      s += \
'''
    static v8::Handle<v8::Value> %s(const v8::Arguments& args);''' \
    % GetV8FuncName(m)

  for f in globalVar.cppHeaders.keys():
    globalvars = globalVar.cppHeaders[f].global_vars
    for idx, var in enumerate(globalvars):
      if not CheckArgSanity(var, False, True):
        continue
      if GetIdenticalType(GetBasicType(var)) == name:
         getFuncName = GetGlobalClassVarCGetterFuncName(var)
         s += \
'''
    static v8::Handle<v8::Value> %s(const v8::Arguments& args);''' \
    % (getFuncName)

         if var["constant"] == 1:
           continue

         setFuncName = GetGlobalClassVarCSetterFuncName(var)
         s += \
'''
    static v8::Handle<v8::Value> %s(const v8::Arguments& args);''' \
    % (setFuncName)

  s += "\n};\n"
  return s

def GenConstructor(name):
  global thisSumamry

#  if CheckSanity(func) == False:
#    printErr("Can't transfer: " + GetFuncDesc(func))
#    thisSummary["failFuncs"].append(name + "." + func["name"])   
#    return ""

  s = \
'''
// constructor
%s::%s(%s * val) {
    m_val = val;
}
''' % (GetV8ClassName(name), GetV8ClassName(name), name)

  thisSummary["succFuncs"].append(name + "." + name)
  return s

def GenMethodHead(className, func):
  if className != "":
    v8ClassName = GetV8ClassName(className)
    
    return \
'''
%s
Handle<Value> %s::%s(const Arguments& args) {
    HandleScope scope;

    %s* obj = ObjectWrap::Unwrap<%s>(args.This());
''' % (GetFuncDesc(func), v8ClassName, GetV8FuncName(func), v8ClassName, v8ClassName)
  else:
    return \
'''
%s
Handle<Value> %s(const Arguments &args) {
    HandleScope scope;
'''%(GetFuncDesc(func), GetV8FuncName(func))

def GenMethodCall(func, className):
  if re.match(r"operator.*", func["name"]):
    return '''// TODO: operator %s override call''' %(func["name"][8:])

  sRetType = GetIdenticalType(func["rtnType"]["type"])
  sRetBasicType = GetBasicType(func["rtnType"])
  if className == "":
    objStr = ""
  else:
    objStr = '''obj->m_val->'''

  argsReturnStr = GenArgsReturn(func)
  if (argsReturnStr != ""):
    argsReturnStr = \
'''
// Convert C++ parameters passed by pointer to V8
%s''' %(argsReturnStr)

  s = \
'''
// Call C++ function'''
  
  if sRetType == "" or sRetType == "void":
    s += \
'''
%s%s;
%s
%s
return scope.Close(Undefined());
''' %(objStr, GenCall(func), \
    argsReturnStr,
    FreeMallocObj())

  else:
    retName = "ret"
    retNameV8 = retName + "V8"

    # handle return type "void *" as "int *"
    if sRetType == "void *":
      sRetType = "int *"

    s += \
'''
%s %s = (%s)%s%s;
%s
'''% (sRetType, retName, sRetType, objStr, GenCall(func),\
      argsReturnStr)

    if IsClassArg(sRetBasicType):
      s += \
'''
// Map C++ Object to V8 Object
iter = CClassToJsObjMap.find(ret);
%s
if (iter != CClassToJsObjMap.end()) {
    return iter->second;
} else {
    V8_ASSERT(false, "Don't find corresponding JSObj, \\
              Please define it first in JS code");
}
'''% (FreeMallocObj())

    else:

      s += \
'''
// Convert C++ return value to V8
%s
%s
return scope.Close(%s);
'''% (GenFuncReturn(func["rtnType"], "", retName, retNameV8), \
      FreeMallocObj(), \
      retNameV8)

  return s

def FreeMallocObj():
  s = ""
  for arg in globalVar.mallocObj:
    s += "free(%s);\n" %(arg)
  return s

def GenOverride(className, func):
  global thisSummary

  head = className
  if len(className) != 0:
    head += "."

  if IsV8FuncGen(func) == False:
    return ""

  s = GenMethodHead(className, func)

  for f in func["funcs"]:
    globalVar.mallocObj = []
    if not CheckSanity(f):
      thisSummary["failFuncs"].append(head + f["name"])
      printErr("Can't transfer: " + GetFuncDesc(func))
      continue;
    
    thisSummary["succFuncs"].append(head + f["name"])

    temp  =  GenArgsTrans(f)
    temp +=  GenMethodCall(f, className)
    argCheck = GenArgsCheckExpress(f);
    andStr = ""
    if (len(argCheck) > 0) :
      andStr = " && "
    s += \
'''
    %s
    if ((args.Length() == %d)%s%s) {
%s
    }
''' %(GetFuncDesc(f), \
      len(f["parameters"]), andStr, argCheck, \
      AddIndent(temp, 8))

  s += '''
    V8_ASSERT(false, "parameters error!");

    return scope.Close(Undefined());
}
'''

  return s

def GenMethod(className, func):
  global thisSummary

  globalVar.mallocObj = []
  head = className
  if len(className) != 0:
    head += "."

  if not CheckSanity(func):
    thisSummary["failFuncs"].append(head + func["name"])
    printErr("Can't transfer: " + GetFuncDesc(func))
    s = \
'''
%s
// Can not be transfered!
''' % GetFuncDesc(func)
    return s

  thisSummary["succFuncs"].append(head + func["name"])
  s = GenMethodHead(className, func)
  s += AddIndent(GenArgsCheck(func), 4)
  s += AddIndent(GenArgsTrans(func), 4)
  s += AddIndent(GenMethodCall(func, className), 4)
  s += "\n}"
  return s

def GenClassInit(className, funcs) :

  s = \
'''
void %s::Init(Handle<Object> exports) {
    // Prepare constructor template
    Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
    tpl->SetClassName(v8::String::NewSymbol("%s"));
    tpl->InstanceTemplate()->SetInternalFieldCount(1);

    // Prototype ''' % (GetV8ClassName(className), className)

  for func in funcs:
    if IsV8FuncGen(func) == False:
      continue
    if (func["name"] == className):
      continue
    s += \
'''
    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("%s"),
        FunctionTemplate::New(%s)->GetFunction());
''' % (func["name"],  GetV8FuncName(func))

  for f in globalVar.cppHeaders.keys():
    globalvars = globalVar.cppHeaders[f].global_vars
    for idx, var in enumerate(globalvars):
      if GetIdenticalType(GetBasicType(var)) == className:
         getFuncNameC = GetGlobalClassVarCGetterFuncName(var)
         getFuncNameV8 = GetGlobalClassVarV8GetterFuncName(var)

         s += \
'''
    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("%s"),
        FunctionTemplate::New(%s)->GetFunction());
'''% (getFuncNameV8, getFuncNameC)

         if var["constant"] == 1:
           continue

         setFuncNameC = GetGlobalClassVarCSetterFuncName(var)
         setFuncNameV8 = GetGlobalClassVarV8SetterFuncName(var)
         s += \
'''
    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("%s"),
        FunctionTemplate::New(%s)->GetFunction());
'''% (setFuncNameV8, setFuncNameC)

  s += \
'''
    constructor = Persistent<Function>::New(tpl->GetFunction());
    exports->Set(v8::String::NewSymbol("%s"), constructor);
}''' % (className)
  return s

def GenArgArrayList(func):
  s = ""
  for idx, arg in enumerate(func["parameters"]):
    s += GenArgArrayName(idx) + ','
  s = RemoveLastComma(s);
  return s;

def GenFuncNewContent(func):
  if not CheckSanity(func):
    return ""

  className = func["name"]
  classNameV8 = GetV8ClassName(func["name"])
  argCheck = GenArgsCheckExpress(func)
  andStr = ""
  if (len(argCheck) > 0) :
    andStr = " && "

  s ='''
if ((args.Length() == %d)%s%s) {
    if (args.IsConstructCall()) {
        // Invoked as constructor: `new %s(...)`
%s
        %s *obj = new %s(%s);

        JSObj = Persistent<Object>::New(Local<Object>::Cast(args.This()));
        CClassToJsObjMap.insert(std::pair<void *, Persistent<Object> >(obj, JSObj));

        %s *objV8 = new %s(obj);
        objV8->Wrap(JSObj);
        return JSObj;
    } else {
        // Invoked as plain function `%s(...)`, turn into construct call.
        const int argc = %d;
        Local<Value> argv[argc] = { %s };
        return scope.Close(constructor->NewInstance(argc, argv));
    }
}'''%(len(func["parameters"]), andStr, argCheck, \
        classNameV8, \
        AddIndent(GenArgsTrans(func), 8), \
        className, className, GenArgList(func, False), \
        classNameV8, classNameV8,
        classNameV8,\
        len(func["parameters"]),\
        GenArgArrayList(func))
  return s

def GenFuncNew(className, c):
  v8ClassName = GetV8ClassName(className);
  s = \
'''
Persistent<Function> %s::constructor;

Handle<Value> %s::New(const Arguments& args) {
    HandleScope scope;
'''%(v8ClassName, v8ClassName)
  
  funcs = c["methods"]["public"]
  for func in funcs:
    if func["override"] and (func["name"] == className):
      for f in func["funcs"]:
        if f["constructor"]:
          s += AddIndent(GenFuncNewContent(f), 4);
    elif (not func["override"]) and (func["constructor"] == True):
      s += AddIndent(GenFuncNewContent(func), 4);

  s += \
'''else if ((args.Length() == 1) && args[0]->IsString()) {
        v8::String::AsciiValue arg0(args[0]->ToString());
        if (strcmp(*arg0, "%s") == 0) {
            %s *objV8 = new %s();
            objV8->Wrap(args.This());
            return args.This();
        }
    }  
    V8_ASSERT(false, "parameters error!");
}
''' %(INSTANCE_V8CLASS_ARG, v8ClassName, v8ClassName)
  return s

def CheckVritualFunc(funcs):
  for func in funcs:
    if func.has_key("override") and func["override"]:
      for f in func["funcs"]:
        if f["pure_virtual"]:
          return True
    else:
      if func["pure_virtual"]:
        return True
  return False

def CheckAbstractClass(c):
  return CheckVritualFunc(c["methods"]["public"]) or CheckVritualFunc(c["methods"]["protected"]) or CheckVritualFunc(c["methods"]["private"])


def GenClass(className, c):
  s = GenFuncNew(className, c);

  s += GenConstructor(className)

  funcs = c["methods"]["public"]
  for func in funcs:
    if func["override"]:
      if func["name"] == className:
        continue
      else:
        s += GenOverride(className, func)
    else:
      if func["constructor"]:
        continue
      else:
        s += GenMethod(className, func)

  s += GenClassInit(className, funcs)
  return s

def GetInitName(module):
  return "Init%s" % module.replace("-", "_") #replace '-' with '_' in file name(ex:i2c-dev.cpp)

def GenInit(module, cppHeader):
  s = \
'''
void %s(Handle<Object> exports) {
''' % GetInitName(module)

  for c in cppHeader.classes:
    classT = cppHeader.classes[c]
    if (classT["abstract"] == False) and (classT['declaration_method'] == "class"):
      s += \
'''
    %s::Init(exports);
''' % GetV8ClassName(c)

  s += \
'''
    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
'''
  return s

def FindFunc(name, funcs):
  for idx, func in enumerate(funcs):
    if func["name"] == name:
      return idx

  return -1

def GroupFuncByName(name, funcs):
  group = []

  idx = FindFunc(name, funcs)
  while idx != -1:
    group.append(funcs.pop(idx))
    idx = FindFunc(name, funcs)

  return group

def GroupFunc(funcs):
  newFuncs = []
  groups = []

  while len(funcs) != 0:
    func = funcs[0]
    groups.append(GroupFuncByName(func["name"], funcs))

  for g in groups:
    if len(g) == 1:
      g[0]["override"] = False
      funcs.append(g[0])

    if len(g) > 1:
      funcs.append({ \
        "name": g[0]["name"], \
        "funcs": g, \
        "override": True \
        })

def GenModuleDecl(module, cppHeader):
  s = GetComment();
  s += \
'''
#ifndef %s_ADDON_H
#define %s_ADDON_H

#include <node.h>
#include <v8.h>
#include "%s.h"

#ifndef V8_EXCEPTION
#define V8_EXCEPTION(info) { \\
    v8::ThrowException(Exception::Error(v8::String::New(info))); \\
    }
#endif

#ifndef V8_ASSERT
#define V8_ASSERT(cond, ...) \\
    if(!(cond)) {  \\
        char buffer[512]; \\
        sprintf(buffer, __VA_ARGS__); \\
        V8_EXCEPTION(buffer); \\
        return scope.Close(Undefined()); \\
    }
#endif


''' % (module.upper(), module.upper(), module)

  for c in cppHeader.classes:
    classT = cppHeader.classes[c]
    if (classT["abstract"] == False) and (classT['declaration_method'] == "class"):
      s += GenClassDecl(c, cppHeader.classes[c])

  s += "\n#endif"
  return s

def GenExtraIncludeFiles():
  s = ""
  includeFiles = list(set(globalVar.includeFiles))
  for f in includeFiles:
    split = f.rsplit('.', 1)
    s += \
'''#include "%s_addon.h"
''' %(split[0])
  return s

def GenModule(module, cppHeader):
  s = \
'''#include "%s_addon.h"
#include "stdlib.h"
#include "string.h"
#include "%s"

using namespace v8;

''' % (module, GLOBAL_DEF)

  for c in cppHeader.classes:
    classT = cppHeader.classes[c]
    if (classT["abstract"] == False) and (classT['declaration_method'] == "class"):
      s += GenClass(c, cppHeader.classes[c])

  for func in cppHeader.functions:
    s += GenFunc(func)

  s += GenSetMemberFunc(cppHeader.functions)

  s += GenConst(cppHeader.defines)

  s += GenEnumConst(cppHeader.enums)

  s += GenGlobalVarSetterAndGetter(cppHeader.global_vars)

  s += GenInit(module, cppHeader)

  t = GetComment()

  t += GenExtraIncludeFiles()

  t += s

  return t

def GenFPArgsList(paraTypes):
  s = ""
  for idx, paraT in enumerate(paraTypes):
    if paraT["type"] == "void":
      continue
    s += '''%s arg%d'''%(GetNoQualifierType(paraT["type"]), idx)
    if idx != len(paraTypes) - 1:
      s += ", "
  return s

def GenFPArgsV8Value(paraTypes):
  s = ""
  for idx, paraT in enumerate(paraTypes):
    if paraT["type"] == "void":
      continue
    s += GetV8Value("arg%d"%idx, GetIdenticalType(paraT["type"]))
    if idx != len(paraTypes) - 1:
      s += ", "
  return s

def GenCallbackFuncsDecl():
  hashTab = globalVar.FuncPointerHashtable;
  s = ""
  for key in hashTab.keys():
    types = hashTab[key]
    paraTypes = types["paraTypes"]
    s += \
'''extern %s cbFunc%d(%s);
'''%(GetNoQualifierType(types["rtnType"]["type"]), key, GenFPArgsList(paraTypes))

  return s

def GenCallbackFuncs():
  hashTab = globalVar.FuncPointerHashtable;
  s = ""
  for key in hashTab.keys():
    types = hashTab[key]
    paraTypes = types["paraTypes"]
    rtnType = GetNoQualifierType(types["rtnType"]["type"])

    s += \
'''
%s cbFunc%d(%s) {
    const unsigned argc = %d;
    Local<Value> argv[argc] = { %s };

'''%(rtnType, key, GenFPArgsList(paraTypes), \
    len(paraTypes), GenFPArgsV8Value(paraTypes))

    if rtnType == "void":
      s += \
'''    cbArray[%d]->Call(Context::GetCurrent()->Global(), argc, argv);

    return;'''%(key)
    else:
      s += \
'''    Local<Value> ret = cbArray[%d]->Call(Context::GetCurrent()->Global(), argc, argv);

    return %s;''' %(key, GetCValue("ret", GetIdenticalType(rtnType)))

    s += \
'''
}
'''
  return s

def GenGlobalDecl(module):
  s = "extern void %s(Handle<Object> exports);\n" \
      % GetInitName(module)
  return s

def GenGlobalInit(module):
  s = "    %s(exports);\n" % GetInitName(module)
  return s

def GenPreGlobalInit():
  s = GetComment()
  s += \
'''
#include "%s"

void exportV8(Handle<Object> exports) {

''' % EXPORT_DEF
  mkdir(OUTPUT_DEV_PATH)
  f = OUTPUT_DEV_PATH + "/" + EXPORT_CPP
  printDbg("generateing " + f)
  fp = open(f, "w")
  fp.write(s)
  fp.close()  
  
  m = EXPORT_DEF.replace('.', '_').upper()
  s = GetComment()
  s += \
'''
#ifndef %s
#define %s

#include <node.h>
#include <v8.h>

using namespace v8;

''' % (m, m)
  f = OUTPUT_DEV_PATH + "/" + EXPORT_DEF
  printDbg("generateing " + f)
  fp = open(f, "w")
  fp.write(s)
  fp.close()  

def GenPostGlobalInit():
  s = \
'''
}

Handle<Value> IO(const Arguments& args) {

  exportV8(args.This());

  return args.This();
}

void Init(Handle<Object> exports) {
  exports->Set(String::NewSymbol("IO"),
               FunctionTemplate::New(IO)->GetFunction());
}


NODE_MODULE(%s, Init)
''' % EXPORT_MODULE
  f = OUTPUT_DEV_PATH + "/" + EXPORT_CPP
  printDbg("finished " + f)
  fp = open(f, "a+")
  fp.write(s)
  fp.close()  

  s = \
'''
#endif
''' 
  f = OUTPUT_DEV_PATH + "/" + EXPORT_DEF
  printDbg("finished " + f)
  fp = open(f, "a+")
  fp.write(s)
  fp.close()  

def GenCallback():
  s = GetComment();
  s += \
'''#include "%s"
#include <map>

Persistent<Function> cbArray[%d];

std::map <void *, Persistent<Object> > CClassToJsObjMap;
std::map <void *, Persistent<Object> >::iterator iter;
Persistent<Object> JSObj;

'''%(GLOBAL_DEF, globalVar.FuncPointerCnt)

  #Generate Wrapper call of Function Pointer
  s += GenCallbackFuncs()

  f = OUTPUT_DEV_PATH + "/" + GLOBAL_CPP
  printDbg("finished " + f)
  fp = open(f, "w+")
  fp.write(s)
  fp.close()

  # Generate global var decl and global func decl
  m = GLOBAL_DEF.replace('.', '_').upper()
  s = GetComment()
  s += \
'''#ifndef %s
#define %s

#include <map>
#include <node.h>
#include <v8.h>

using namespace v8;

''' % (m, m)
  s += \
'''extern Persistent<Function> cbArray[%d];

extern std::map <void *, Persistent<Object> > CClassToJsObjMap;
extern std::map <void *, Persistent<Object> >::iterator iter;
extern Persistent<Object> JSObj;

''' %(globalVar.FuncPointerCnt)

  #Generate Wrapper call definition of Function Pointer
  s += GenCallbackFuncsDecl()

  s += \
'''
#endif
'''

  f = OUTPUT_DEV_PATH + "/" + GLOBAL_DEF
  printDbg("finished " + f)
  fp = open(f, "w+")
  fp.write(s)
  fp.close()

def FormalizeFunc(funcs):
  for f in funcs:
    args = f["parameters"]
    if len(args) == 1 and args[0]["type"] == "void":
      f["parameters"] = []

    if f["rtnType"]["type"]  == "void":
      f["rtnType"]["type"] = ""

def GenC(module, cppHeader):

  global summary
  global thisSummary
  thisSummary = {"succFuncs":[], "failFuncs": [], \
                 "succGlobalVar": [], "failGlobalVar": [], \
                 "succGlobalClassVar": {}, "failGlobalClassVar": {}, \
                 "cpp":[], "h":[]}

  printDbg("transfering " + module)

  target =  module + "_addon.cpp"
  f = OUTPUT_DEV_PATH + "/" + target
  thisSummary["cpp"].append(target)
  fp = open(f, "w")
  fp.write(GenModule(module, cppHeader))
  fp.close()

  printDbg("generate " + f)

  target = module + "_addon.h"
  f = OUTPUT_DEV_PATH + "/" + target
  thisSummary["h"].append(target)
  fp = open(f, "w")
  fp.write(GenModuleDecl(module, cppHeader))
  fp.close()
  printDbg("generate " + f)

  f = OUTPUT_DEV_PATH + "/" + EXPORT_DEF
  fp = open(f, "a+")
  fp.write(GenGlobalDecl(module))
  fp.close()

  f = OUTPUT_DEV_PATH + "/" + EXPORT_CPP
  fp = open(f, "a+")
  fp.write(GenGlobalInit(module))
  fp.close()

  summary[module] = thisSummary
  printDbg("generate " + f)


def DumpFunctionSummary():
  global summary
  totalSucc = 0
  totalFail = 0
  fmt = "%-20s:   +%-4d -%-4d\n"
  s = "\nSummary of translated functions\n"
  s += "================================\n"
  for idx in summary:
    item = summary[idx]
    totalSucc += len(item["succFuncs"])
    totalFail += len(item["failFuncs"])
    s += fmt % (idx, len(item["succFuncs"]), len(item["failFuncs"]))    
  s += "================================\n"

  s += "\nSummary of global common var set/get functions\n"
  s += "================================\n"
  for idx in summary:
    item = summary[idx]
    totalSucc += len(item["succGlobalVar"])
    totalFail += len(item["failGlobalVar"])
    s += fmt % (idx, len(item["succGlobalVar"]), len(item["failGlobalVar"]))    
  s += "================================\n"

  s += "\nSummary of global class var set/get functions\n"
  s += "================================\n"
  for idx in summary:
    item = summary[idx]
    totalSucc += len(item["succGlobalClassVar"])
    totalFail += len(item["failGlobalClassVar"])
    s += fmt % (idx, len(item["succGlobalClassVar"]), len(item["failGlobalClassVar"]))    
  s += "================================\n"
  s += fmt % ("total", totalSucc, totalFail)
  printLog(s)

def DumpFileSummary():
  global summary
  totalC = 0
  totalH = 0

  for idx in summary:
    item = summary[idx]
    totalC += len(item["cpp"])
    totalH += len(item["h"])
  fmt = "%-8s:  %s\n"
  s = "\nSummary of created files\n"
  s += "================================\n"
  #dont forget EXPORT_DEF and EXPORT_CPP
  s += fmt % ("module", EXPORT_MODULE)
  s += fmt % ("path", OUTPUT_DEV_PATH)
  s += fmt % ("export", EXPORT_CPP)
  s += fmt % ("cpp", totalC)
  s += fmt % ("h", totalH)
  s += fmt % ("gyp", GYP_PATH + GYP_FILE)
  s += "================================\n"
  
  printLog(s)

def DumpSummary():
  DumpFileSummary()
  DumpFunctionSummary()

def GenGyp():
  f = GYP_PATH + GYP_FILE
  fp = open(f, "w")
  fp.write(BuildGyp())
  fp.close()

def BuildGyp():

  files = ""
  for idx in summary:
    item = summary[idx]
    for f in item["cpp"]:
      if f == "version_export_addon.cpp":
        files += "'" + GYP_SRC_PATH + "version_export.cpp',\n"
      files += "'" + GYP_SRC_PATH + f + "',\n"

  files += "'" + GYP_SRC_PATH + EXPORT_CPP + "',\n"
  files += "'" + GYP_SRC_PATH + GLOBAL_CPP + "'\n"
  files = AddIndent(files, 6)

  inc = ""
  for idx in INPUT_DECL_PATHS:
    if os.path.isfile(idx):
      inc += "'" + os.path.dirname(idx) + "',\n"
    else:
      inc += "'" + idx + "',\n"
  inc = AddIndent(inc, 6)

  gypContent = GetGypComment("ext.gypi")
  gypContent += \
'''

#skeleton of node-gyp file

{
  'targets' : [{

    'target_name' : '%s',

    'sources' : [
%s
    ],

    'include_dirs' : [
      '%s',
%s
    ],

    'libraries' : [
      #'-L/io/library/path/,
      #'-liolib'
    ],

    'includes': ['ext.gypi']

  }]
}
''' % (EXPORT_MODULE, files, GYP_SRC_PATH, inc)
  return gypContent

def GenGlobalClassVarJsExport():
  global summary
  f = GYP_PATH + Global_CLASS_VAR_FILE
  fp = open(f, "w")

  methodNames = []
  s = \
'''var IO = require('bindings')('galileo.node')
'''

  for idx in summary:
    thisS = summary[idx]
    for funcName in thisS["succGlobalClassVar"].keys():
      var = thisS["succGlobalClassVar"][funcName]
      varType = GetIdenticalType(GetBasicType(var))

      if re.match("^Get", funcName):
        funcNameJS = GetGlobalClassVarJSGetterFuncName(var)
        funcNameV8 = GetGlobalClassVarV8GetterFuncName(var)
        s += \
'''
IO.%s = function() {
  var tmp = new IO.%s("%s");
  tmp.%s();
  return tmp;
}
''' %(funcNameJS, \
      varType, INSTANCE_V8CLASS_ARG, \
      funcNameV8);

        methodNames.append("%s" %(funcNameJS))

      elif re.match("^Set", funcName):
        funcNameJS = GetGlobalClassVarJSSetterFuncName(var)
        funcNameV8 = GetGlobalClassVarV8SetterFuncName(var)
        s += \
'''
IO.%s = function(value) {
  value.%s();
}
''' % (funcNameJS, funcNameV8)
        methodNames.append("%s" %(funcNameJS))
      else:
        raise("Unexpected function %s\n", funcName)

  s += '''
module.exports = IO;
'''

  fp.write(s)
  fp.close()
