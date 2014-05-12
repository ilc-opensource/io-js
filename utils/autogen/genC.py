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
  if (arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0) :
    typeCheck = "IsFunction"
  elif IsStructArg(GetBasicType(arg)):
    typeCheck = "IsObject"
  elif (arg["pointer"] == 1):
    if (GetIdenticalType(arg["type"]) == "char*"):
      typeCheck = "IsObject"
    else:
      typeCheck = "IsArray"
  else:
    typeCheck = GetV8TypeCheck(arg["type"]);

  s = "%s->%s()" % (argName, typeCheck)
  return s

def GenArgsCheck(func) :
  s =""
  args = func["parameters"]
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    s += GenArgCheck(arg, GenArgArrayName(idx))

    if idx != (len(args) - 1):
      s += " && "

  return s

def GenFuncPointArgDef(arg, idx):
  if (len(arg["function_pointer"]) > 0) :
    type_t = arg["type"]
    if type_t.find("(") == -1:           # typedef
      return "%s arg%d" %(type_t, idx)
    else:
      FPType = arg["function_pointer"]   # no typedef
      s = FPType["rtnType"]["type"]
      s += '''(*arg%d) (''' %(idx)
      for idx, para in enumerate(FPType["paraTypes"]):
        s += para["type"]
        if idx != (len(FPType["paraTypes"]) - 1):
          s += ","
        else:
          s += ")"
      return s
  else:
    raise "GenFuncPointArgDef: unexpected arg type!"

def GenLoopCnt(idx):
  return "index%s" %(idx)

def GenArrayLen(idx):
  return "len%s" %(idx)

def GenArrayArgReturn(arg, idx, argCName, argMiddleName):
  s = ""
  if arg["pointer"] != 1:
    return s

  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  argUniqType = GetIdenticalType(argType)
  argUniqBasicType = GetIdenticalType(argBasicType)

  loopcnt = GenLoopCnt(idx)
  s += \
'''for (%s = 0; %s < %s; %s ++)
  %s->Set(%s, %s);
'''%(loopcnt, loopcnt, GenArrayLen(idx), loopcnt, \
   argMiddleName, loopcnt, GetV8Value("%s[%s]" %(argCName, loopcnt), argUniqBasicType))
  return s

def GenStructArgReturn(arg, idx, argCName, argV8Name, argMiddleName):
  s = ""
  if arg["pointer"] != 1:
    return s

  if (arg["function_pointer"] != {} and \
      arg["function_pointer"] != 0) :
    return s

  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  if (not IsStructArg(argBasicType)):
    return s

  classes = globalVar.cppHeader.classes

  if argType == argBasicType:
    join = "."
  else:
    join = "->"

  props = classes[argBasicType]["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldType = prop["type"]
    fldBasicType = GetBasicType(prop)
    if (IsStructArg(fldBasicType)):
      objName = "%s_%d" %(argMiddleName, idxs)
      newObjName = objName + "t"
      s += GenStructArgReturn(prop, "%s%d" %(idx, idxs), \
             argCName + join + fldName, objName, newObjName)
    elif prop["pointer"] == 1:
      newObjName = "%s_%dt" %(argMiddleName, idxs)
      s += GenArrayArgReturn(prop, "%s%d" %(idx, idxs), \
             argCName + join + fldName, newObjName)
      objName = newObjName
    else:
      objName = GetV8Value(argCName + join + fldName, fldType)

    s += \
'''%s->ToObject()->Set(String::New("%s"), %s);

'''% (argV8Name, fldName, objName)
  return s

def GenArgReturn(idx, arg):
  argType = arg["type"]
  argBasicType = GetBasicType(arg)
  argCName = GenArgName(idx, arg)
  argV8Name = GenArgArrayName(idx)
  argMiddleName = "argV8_%s" %(idx)

  if (IsStructArg(argBasicType)):
    s = GenStructArgReturn(arg, idx, argCName, argV8Name, argMiddleName)
  else:
    s = GenArrayArgReturn(arg, idx, argCName, argMiddleName)
  return s

def GenRetLoopCnt(idx):
  return "retIdx%s" %(idx)

def GenRetArrayLen(idx):
  return "retLen%s" %(idx)

def GenArrayReturn(rtn, idx, rtnCName, rtnArrayV8Name):
  s = ""
  if rtn["pointer"] != 1:
    return s

  rtnType = rtn["type"]
  rtnBasicType = GetBasicType(rtn)

  rtnUniqType = GetIdenticalType(rtnType)
  rtnUniqBasicType = GetIdenticalType(rtnBasicType)

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
  s = \
'''Handle<Value> %s = %s;
''' %(rtnV8Name, GetV8Value(rtnCName, rtnType))
  return s

def GenStringReturn(rtn, idx, rtnCName, rtnV8Name):
  s = \
'''Handle<Value> %s = v8::String::New((char*)%s);
''' %(rtnV8Name, rtnCName)
  return s

def GenStructReturn(rtn, idx, rtnCName, rtnV8Name):
  s = ""

  rtnType = rtn["type"]
  rtnBasicType = GetBasicType(rtn)

  if (not IsStructArg(rtnBasicType)):
    return s

  classes = globalVar.cppHeader.classes

  if rtnType == rtnBasicType:
    join = "."
  else:
    join = "->"

  s += \
'''Local<Object> %s = Object::New();
''' % (rtnV8Name)

  props = classes[rtnBasicType]["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldType = prop["type"]
    fldBasicType = GetBasicType(prop)
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
  elif (rtnUniqType == "char*"):
    s = GenStringReturn(rtn, idx, rtnCName, rtnV8Name)
  elif rtn["pointer"] == 1:
    s = GenArrayReturn(rtn, idx, rtnCName, rtnV8Name)
  else:
    s = GenCommonReturn(rtnUniqType, rtnCName, rtnV8Name)
  return s

def GenArgsReturn(func):
  args = func["parameters"]
  s = ""

  for idx, arg in enumerate(args):
    if arg["pointer"] != 1:
      continue

    if (arg["function_pointer"] != {} and \
        arg["function_pointer"] != 0) :
      continue

    s += GenArgReturn(idx, arg)
  return s

def GenFPArgTran(arg, idx, argCName, argV8Name):
  cnt = globalVar.FuncPointerCnt
  s = \
'''cbArray[%d] = Persistent<Function>::New(Local<Function>::Cast(%s));
%s;
%s = cbFunc%d;
''' %(cnt, argV8Name, GenFuncPointArgDef(arg, idx), \
  argCName, cnt)
  globalVar.FuncPointerHashtable[cnt] = arg["function_pointer"]
  globalVar.FuncPointerCnt += 1
  return s

def GenArrayArgTran(arg, idx, argCName, argV8Name, argMiddleName):
  if arg["pointer"] != 1:
    return ""

  s = ""
  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  argUniqType = GetIdenticalType(argType)
  argUniqBasicType = GetIdenticalType(argBasicType)

  loopcnt = GenLoopCnt(idx)
  arrayLen = GenArrayLen(idx)

  if argUniqType == "char*":
    arrayLenStr = "%s->Length() + 1" %(argMiddleName)
  else:
    arrayLenStr = "%s->Length()" %(argMiddleName)

  s = \
'''int %s;
Local<Array> %s = Local<Array>::Cast(%s);
int %s = %s;
%s %s[%s];
for (%s = 0; %s < %s; %s ++)
  %s[%s] = (%s)%s;
'''%(loopcnt, \
    argMiddleName, argV8Name,\
    arrayLen, arrayLenStr, \
    argBasicType, argCName, arrayLen, \
    loopcnt, loopcnt, arrayLen, loopcnt, \
    argCName, loopcnt, GetNoQualifierType(argBasicType), \
      GetCValue("%s->Get(%s)" %(argMiddleName, loopcnt), argUniqBasicType))

  if argUniqType == "char*":
    s += \
'''%s[%s] = 0;
'''%(argCName, loopcnt)

  return s

def GenCommonArgTran(arg, idx, argCName, argV8Name):
  argType = arg["type"]
  argUniqType = GetIdenticalType(argType)

  s = \
'''%s %s = (%s)%s;
'''% (argType, argCName, GetNoQualifierType(argType), GetCValue(argV8Name, argUniqType))
  return s

def GenStructArgTran(arg, idx, argCName, argV8Name, argMiddleName):
  s = ""
  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  if (not IsStructArg(argBasicType)):
    return s

  classes = globalVar.cppHeader.classes
  props = classes[argBasicType]["properties"]["public"]
  for idxs, prop in enumerate(props):
    fldName = prop["name"]
    fldType = prop["type"]
    fldBasicType = GetBasicType(prop)
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
          objName, newObjName)

    s += "\n"

  if argType == argBasicType:
    sName = argCName
  else:
    sName = argCName + "T"
  s += \
'''%s %s = {''' %(argBasicType, sName)
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
      s += \
'''%s%s = &%s;
''' %(arg["type"], argCName, sName)

  return s

def GenArgTrans(arg, idx, argCName, argV8Name, argMiddleName):
  if arg["type"] == "void":
    return ""

  argBasicType = GetBasicType(arg)

  if (arg["function_pointer"] != 0 and len(arg["function_pointer"]) > 0) :
    s = GenFPArgTran(arg, idx, argCName, argV8Name)
  elif IsStructArg(argBasicType):
    s = GenStructArgTran(arg, idx, argCName, argV8Name, argMiddleName)
  elif arg["pointer"] == 1:
    s = GenArrayArgTran(arg, idx, argCName, argV8Name, argMiddleName)
  else:
    s = GenCommonArgTran(arg, idx, argCName, argV8Name)

  return s

def GenArgsTrans(func):
  args = func["parameters"]
  s = ""
  t = GenArgsCheck(func)
  if len(t) != 0:
    s += \
'''
V8_ASSERT(%s, "parameters error!");

// Convert V8 parameters to C++
''' % (t)

  for idx, arg in enumerate(args):

    if arg["type"] == "void":
      continue

    argBasicType = GetBasicType(arg)

    argCName = GenArgName(idx, arg)
    argV8Name = GenArgArrayName(idx)
    argMiddleName = "argV8_%d" %(idx)

    s += GenArgTrans(arg, idx, argCName, argV8Name, argMiddleName)
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

def GenConst(defines):
  
  s = \
'''
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
    static void Init(v8::Handle<v8::Object> exports);
'''%(GetV8ClassName(name), name, GetV8ClassName(name))

  for m in c["methods"]["public"]:
    if m["name"] == name:
      if m["override"]:
        for f in m["funcs"]:
          if CheckSanity(f) == False:
            s += ""
          else:
            s += "    " + GenConstructorDecl(f)
      else:
        if CheckSanity(m) == False:
          s += ""
        else:
          s += "    " + GenConstructorDecl(m)
      continue

    flag = IsV8FuncGen(m)
    if flag:
      s += \
'''
    static v8::Handle<v8::Value> %s(const v8::Arguments& args);''' \
    % GetV8FuncName(m)

  s += "\n};\n"
  return s

def GenConstructor(name, func):
  global thisSumamry

  if CheckSanity(func) == False:
    printErr("Can't transfer: " + GetFuncDesc(func))
    thisSummary["failFuncs"].append(name + "." + func["name"])   
    return ""
  s = \
'''
// constructor
%s::%s(%s) {
    m_val = new %s(%s);
}
''' % (GetV8ClassName(name), GetV8ClassName(name), GenArgList(func, True), name, GenArgList(func, False))
  thisSummary["succFuncs"].append(name + "." + func["name"])   
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
return scope.Close(Undefined());
''' %(objStr, GenCall(func), \
    argsReturnStr)

  else:
    retName = GetRetName(sRetType)
    retNameV8 = retName + "V8"
    s += \
'''
%s %s = %s%s;
%s
// Convert C++ return value to V8
%s
return scope.Close(%s);''' \
    % (sRetType, retName, objStr, GenCall(func),\
       argsReturnStr, \
       GenFuncReturn(func["rtnType"], "", retName, retNameV8), \
       retNameV8)

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
    if not CheckSanity(f):
      thisSummary["failFuncs"].append(head + f["name"])
      printErr("Can't transfer: " + GetFuncDesc(func))
      continue;
    
    thisSummary["succFuncs"].append(head + f["name"])

    temp  =  GenArgsTrans(f)
    temp +=  GenMethodCall(f, className)
    argCheck = GenArgsCheck(f);
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
      len(f["parameters"]), \
      andStr,\
      argCheck,\
      AddIndent(temp, 8))

  s += '''
    V8_ASSERT(false, "parameters error!");

    return scope.Close(Undefined());
}
'''

  return s

def GenMethod(className, func):
  global thisSummary

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

  s += \
'''
    constructor = Persistent<Function>::New(tpl->GetFunction());
    exports->Set(v8::String::NewSymbol("%s"), constructor);
}''' % (className)
  return s

def GenFuncNew1(className, c):
  v8ClassName = GetV8ClassName(className);
  return \
'''
Persistent<Function> %s::constructor;

Handle<Value> %s::New(const Arguments& args) {
    HandleScope scope;

    if (args.IsConstructCall()) {
      // Invoked as constructor: `new %s(...)`
      double value = args[0]->IsUndefined() ? 0 : args[0]->NumberValue();
      %s *obj = new %s(value);
      obj->Wrap(args.This());
      return args.This();
    } else {
      // Invoked as plain function `%s(...)`, turn into construct call.
      const int argc = 1;
      Local<Value> argv[argc] = { args[0] };
      return scope.Close(constructor->NewInstance(argc, argv));
    }
}
'''% (v8ClassName, v8ClassName, className, v8ClassName, v8ClassName, className)

def GenArgArrayList(func):
  s = ""
  for idx, arg in enumerate(func["parameters"]):
    s += GenArgArrayName(idx) + ','
  s = RemoveLastComma(s);
  return s;

def GenFuncNewContent(func):
  if not CheckSanity(func):
    return ""
  
  className = GetV8ClassName(func["name"]);
  argCheck = GenArgsCheck(func);
  andStr = ""
  if (len(argCheck) > 0) :
    andStr = " && "

  s =''' 
  if ((args.Length() == %d)%s%s) {
    if (args.IsConstructCall()) {
      // Invoked as constructor: `new %s(...)`
      %s
      %s *obj = new %s(%s);
      obj->Wrap(args.This());
      return args.This();
    } else {
      // Invoked as plain function `%s(...)`, turn into construct call.
      const int argc = %d;
      Local<Value> argv[argc] = { %s };
      return scope.Close(constructor->NewInstance(argc, argv));
    }
  }'''%(len(func["parameters"]),\
        andStr,\
        argCheck,\
        className,\
        AddIndent(GenArgsTrans(func), 6),\
        className,\
        className,\
        GenArgList(func, False),\
        className,\
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
        s += GenFuncNewContent(f);
    elif (not func["override"]) and (func["name"] == className):
      s += GenFuncNewContent(func);

  s += '''
}
'''
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

  funcs = c["methods"]["public"]
  for func in funcs:
    if func["override"]:
      if func["name"] == className:
        for f in func["funcs"]:
          s += GenConstructor(className, f)
      else:
        s += GenOverride(className, func)
    else:
      if func["name"] == className:
        s += GenConstructor(className, func)
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
  s = \
'''
#ifndef %s_ADDON_H
#define %s_ADDON_H

#include <node.h>
#include <v8.h>
#include "%s.h"

using namespace v8;

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

def GenModule(module, cppHeader):

  s = \
'''#include "%s_addon.h"
#include "%s"
''' % (module, CALLBACK_DEF)

  for c in cppHeader.classes:
    classT = cppHeader.classes[c]
    if (classT["abstract"] == False) and (classT['declaration_method'] == "class"):
      s += GenClass(c, cppHeader.classes[c])

  for func in cppHeader.functions:
    s += GenFunc(func)

  s += GenSetMemberFunc(cppHeader.functions)

  s += GenConst(cppHeader.defines)

  s += GenInit(module, cppHeader)

  return s

def GenFPArgsList(paraTypes):
  s = ""
  for idx, paraT in enumerate(paraTypes):
    if paraT["type"] == "void":
      continue
    s += '''%s arg%d'''%(paraT["type"], idx)
    if idx != len(paraTypes) - 1:
      s += ", "
  return s

def GenFPArgsV8Value(paraTypes):
  s = ""
  for idx, paraT in enumerate(paraTypes):
    if paraT["type"] == "void":
      continue
    s += GetV8Value("arg%d"%idx, paraT["type"])
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
'''%(types["rtnType"]["type"], key, GenFPArgsList(paraTypes))

  return s

def GenCallbackFuncs():
  hashTab = globalVar.FuncPointerHashtable;
  s = ""
  for key in hashTab.keys():
    types = hashTab[key]
    paraTypes = types["paraTypes"]

    s += \
'''
%s cbFunc%d(%s) {
    const unsigned argc = %d;
    Local<Value> argv[argc] = { %s };

'''%(types["rtnType"]["type"], key, GenFPArgsList(paraTypes), \
    len(paraTypes), GenFPArgsV8Value(paraTypes))

    if types["rtnType"]["type"] == "void":
      s += \
'''    cbArray[%d]->Call(Context::GetCurrent()->Global(), argc, argv);

    return;'''%(key)
    else:
      s += \
'''    Local<Value> ret = cbArray[%d]->Call(Context::GetCurrent()->Global(), argc, argv);

    return %s;''' %(key, GetCValue("ret", types["rtnType"]["type"]))

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
  s = \
'''
#include "%s"

void exportV8(Handle<Object> exports) {

''' % EXPORT_DEF
  f = OUTPUT_DEV_PATH + "/" + EXPORT_CPP
  printDbg("generateing " + f)
  fp = open(f, "w")
  fp.write(s)
  fp.close()  
  
  m = EXPORT_DEF.replace('.', '_').upper()
  s = \
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

NODE_MODULE(%s, exportV8)
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
#Generate Wrapper call of Function Pointer
  s = \
'''#include "%s"

Persistent<Function> cbArray[%d];
'''%(CALLBACK_DEF, globalVar.FuncPointerCnt)
  s += GenCallbackFuncs()

  f = OUTPUT_DEV_PATH + "/" + CALLBACK_CPP
  printDbg("finished " + f)
  fp = open(f, "w+")
  fp.write(s)
  fp.close()

#Generate Wrapper call definition of Function Pointer
  m = CALLBACK_DEF.replace('.', '_').upper()
  s = \
'''#ifndef %s
#define %s

#include <node.h>
#include <v8.h>

using namespace v8;

''' % (m, m)
  s += \
'''extern Persistent<Function> cbArray[%d];

''' %(globalVar.FuncPointerCnt)

  s += GenCallbackFuncsDecl()

  s += \
'''
#endif
'''

  f = OUTPUT_DEV_PATH + "/" + CALLBACK_DEF
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
  thisSummary = {"succFuncs":[], "failFuncs": [], "cpp":[], "h":[]}

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
  files += "'" + GYP_SRC_PATH + CALLBACK_CPP + "'\n"
  files = AddIndent(files, 6)

  inc = ""
  for idx in INPUT_DECL_PATHS:
    inc += "'" + idx + "',\n"
  inc = AddIndent(inc, 6)

  return \
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
