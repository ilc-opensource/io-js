import os
from config import *
from util import *

def GetV8ClassName(className):
  return className + "V8"

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
    s = "//%s" % func["name"]
  else:
    s = "//%d: %s"% (func["line_number"], func["debug"])

  return s

def GenSetMemberFunc(funcs):
  s = "\nvoid SetMemberFunc(Handle<Object> obj) {"
  for func in funcs:
    flag = IsV8FuncGen(func)
    if flag:
      s += GenSetFunc("obj", func)
  s += "}\n"
  return s

def GenArgName(idx, args):
  return "arg%d"%idx

def GenArgArrayName(idx):
  return "args[%d]"%idx

def GenArgList(func, withType):
  s =""
  args = func["parameters"]
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    
    #argName = arg["name"]
    #if len(argName) == 0:
    argName = GenArgName(idx, args)
   
    if withType: 
      s += "%s %s" % (arg["type"], argName)
    else:
      s += "%s" % argName

    if idx != (len(args) - 1):
      s += ", "

  return s

def GenArgCheck(func) :
  s =""
  args = func["parameters"]
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    
    #argName = arg["name"]
    #if len(argName) == 0:
    argName = GenArgArrayName(idx)
    
    s += "%s->%s()" % (argName, GetV8TypeCheck(arg["type"]))

    if idx != (len(args) - 1):
      s += " && "
  
  return s

def GenArgTrans(func):
  args = func["parameters"] 
  s = ""
  if len(args) != 0:
    s += \
'''
V8_ASSERT(%s, "parameters error!");

''' % (GenArgCheck(func))

  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    argName = GenArgName(idx, args)

    argType = GetIdenticalType(arg["type"])

    if argType == "char*":
      s += \
'''v8::String::AsciiValue strVal(%s->ToString());
char* %s = (char *)*strVal;
'''% (GenArgArrayName(idx), argName)
    else:
      s += \
'''%s %s = %s;
'''% (argType, argName, GetCValue(GenArgArrayName(idx), argType))
  return s

def GenCall(func):
  return "%s(%s)" % (func["name"], GenArgList(func, False))

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
void SetConst(Handle<Object> obj) {
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
//constructor
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

  s = ""
  sRetType = GetIdenticalType(func["rtnType"])
  if className == "":
    objStr = ""
  else:
    objStr = '''obj->m_val->'''

  if sRetType == "" or sRetType == "void":
    s += \
'''
%s%s;

return scope.Close(Undefined());
''' %(objStr, GenCall(func))

  else:
    s += \
'''
%s %s = %s%s;

return scope.Close(%s);''' \
    % (sRetType, GetRetName(sRetType), objStr, GenCall(func), GetV8Value(GetRetName(sRetType), sRetType))

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

    temp  =  GenArgTrans(f)
    temp +=  GenMethodCall(f, className)
    argCheck = GenArgCheck(f);
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
//Can not be transfered!
''' % GetFuncDesc(func)
    return s

  thisSummary["succFuncs"].append(head + func["name"])
  s = GenMethodHead(className, func)
  s += AddIndent(GenArgTrans(func), 4)
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
  argCheck = GenArgCheck(func);
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
        AddIndent(GenArgTrans(func), 6),\
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
        #print "[TODO]: override constructor function %s" %(className)
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
  return "Init%s" % module

def GenInit(module, cppHeader):
  s = \
'''
void %s(Handle<Object> exports, Handle<Object> module) {
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

#ifndef V8_ASSERT
#define V8_ASSERT(cond, ...) \
    if(!(cond)) {  \
        char buffer[512]; \
        sprintf(buffer, __VA_ARGS__); \
        V8_EXCEPTION(buffer); \
        return scope.Close(Undefined()); \
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

  s = '#include "%s_addon.h"\n' % module

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

def GenGlobalDecl(module):
  s = "extern %s(Handle<Object> exports, Handle<Object> module);\n" \
      % GetInitName(module)
  return s

def GenGlobalInit(module):
  s = "    %s(exports, module);\n" % GetInitName(module)
  return s

def GenPreGlobalInit():    
  s = \
'''
#include <node.h>
#include <v8.h>
#include "%s"

using namespace v8;

void init(Handle<Object> exports) {

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

NODE_MODULE(%s, init)
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
  fmt = "%-15s:   +%-4d -%-4d\n"
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
      files += "'" + GYP_SRC_PATH + f + "',\n"
  
  files = AddIndent(files, 6)

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
      '%s'
    ],

    'libraries' : [
      #'-L/io/library/path/,
      #'-liolib'
    ]

  }]
}
''' % (EXPORT_MODULE, files, GYP_SRC_PATH)