import os
from config import *
from util import *

def GenExport(module):
  s = \
'''
void Init(Handle<Object> exports) {

    Local<Function> constructFn = FunctionTemplate::New(%s)->GetFunction();
    exports->Set(String::NewSymbol("%s"), constructFn);
}

NODE_MODULE(%s, Init);
'''%(module, module, module)
  return s

def GenSetFunc(obj, func):
  s = \
'''
    %s->Set(String::NewSymbol("%s"),
           FunctionTemplate::New(%sV8)->GetFunction());
'''%(obj, func["name"], func["name"])
  return s

def GetFuncDesc(func):
  return '''//%d: %s\n'''% (func["line_number"], func["debug"])

def GenFuncDecl(funcs):
  s = "\nvoid SetMemberFunc(Handle<Object> obj) {"
  for func in funcs:
    if not CheckSanity(func):
      continue;
    s += GenSetFunc("obj", func)
  s += "}"
  return s

def GenArgName(idx, args):
  return "arg%d"%idx

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
   
def GenArgTrans(func):
  s = ""
  args = func["parameters"] 
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    argName = GenArgName(idx, args)
    s += \
'''
%s %s = %s;
'''% (arg["type"], argName, GetCValue(argName, arg["type"]))
  return s


def GenCall(func):
  s = "%s(%s)" % (func["name"], GenArgList(func, False))
  return s

def GetRetName(func):
  retType = func["returns"]
  if retType == "" or retType == "void":
    return ""
  else:
    return "ret"

def MangleFuncName(func):
  return func["name"]

def GenRet(func):
  retType = func["returns"]
  if retType == "" or retType == "void":
    return ""
  else:
    return "%s %s;" % (retType, GetRetName(func)) 

def GenFunc(func):
  s = "" 
  if not CheckSanity(func):
    return GetFuncDesc(func)

  s = \
'''
Handle<Value> %s(const Arguments &args) {
    HandleScope scope;
'''%(func["name"])
 
  temp  = GenArgTrans(func)
  s += AddIndent(temp, 4)

  sRetType = func["returns"]

  if sRetType == "" or sRetType == "void":
    s += \
'''
    %s;

    return scope.Close(Undefined());
}
'''% GenCall(func)
  else :
    s += \
'''
    %s %s = %s;
    return scope.Close(%s);
}
'''%(sRetType, GetRetName(func), GenCall(func), GetV8Value(GetRetName(func), sRetType))
  
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
    obj->Set(String::NewSymbol("%s"),
'''%macros[0]

    if IsInt(macros[1]):
      s += "             Int32::New(%s));\n"% macros[1]
    else:
      s += "             Number::New(%s));\n"% macros[1]

  s += "\n}"

  return s


def GenConstructorDecl(func):
  s = "explicit %sV8"% func["name"]
  s += "(%s);"%GenArgList(func, True)
  return s 
  
def GenClassDecl(name, c):
  s = \
'''
#include <node.h>

class %sV8:: public node::ObjectWrap {

private:
    %s *m_val;
    ~%sV8();
    static v8::Handle<v8::Value> New(const v8::Arguments& args);
    static v8::Persistent<v8::Function> constructor;

public:
    static void Init(v8::Handle<v8::Object> exports);
'''%(name, name, name)

  for m in c["methods"]["public"]:
    if m["name"] == name:
      s += "    " + GenConstructorDecl(m)
      continue

    s += \
'''
    static v8::Handle<v8::Value> %s(const v8::Arguments& args);''' \
    % MangleFuncName(m)

  s += "\n};\n"
  return s

def GenConstructor(name, func):
  s = \
'''
%sV8::%sV8(%s) {
    m_val = new %s(%s);
}
''' % (name, name, GenArgList(func, True), name, GenArgList(func, False))
  return s

def GenMethodHead(name, func):
  return \
'''
Handle<Value> %sV8::%s(const Arguments& args) {
    HandleScope scope;

    %sV8* obj = ObjectWrap::Unwrap<%sV8>(args.This());
''' % (name, MangleFuncName(func), name, name)

def GenMethodObjCall(func):
  sRetType = func["returns"]
  
  s = ""

  if sRetType == "" or sRetType == "void":
    s += \
'''
obj->m_val->%s;
return scope.Close(Undefined());
''' % GenCall(func)
  else:
    s += \
'''
%s %s = obj->m_val->%s;
return scope.Close(%s);''' \
    % (sRetType, GetRetName(func), GenCall(func), GetV8Value(GetRetName(func), sRetType))

  return s

def GenOverwrite(name, func):
  s = GenMethodHead(name, func)

  for f in func["funcs"]:
    temp =  GenArgTrans(f)    
    s += \
'''
    if (args.Length() == %d) {
%s%s
    }
''' %(len(f["parameters"]), \
      AddIndent(GenArgTrans(f), 8), \
      AddIndent(GenMethodObjCall(f), 8))

  s += "}\n"

  return s

def GenMethod(name, func):
  if not CheckSanity(func):
    return GetFuncDesc(func) 

  s = GenMethodHead(name, func) 
  s += AddIndent(GenArgTrans(func), 4)
  s += AddIndent(GenMethodObjCall(func), 4)
  s += "\n}"
  return s

def GenClassInit(name, funcs) :
  s = \
'''
void %sV8::Init(Handle<Object> exports) {

    // Prepare constructor template
    Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
    tpl->SetClassName(String::NewSymbol("%s"));
    tpl->InstanceTemplate()->SetInternalFieldCount(1);

    // Prototype ''' % (name, name)
  for func in funcs:
    s += \
'''
    tpl->PrototypeTemplate()->Set(String::NewSymbol("%s"),
        FunctionTemplate::New(%sV8)->GetFunction());
''' % (func["name"], func["name"])

  s += \
'''
    constructor = Persistent<Function>::New(tpl->GetFunction());
    exports->Set(String::NewSymbol("%s"), constructor);
}''' % (name)
  return s
  
def GenClass(name, c):
  s = \
'''
Persistent<Function> %sV8::constructor;

Handle<Value> %sV8::New(const Arguments& args) {
    HandleScope scope;

    if (args.IsConstructCall()) {
      // Invoked as constructor: `new %s(...)`
      double value = args[0]->IsUndefined() ? 0 : args[0]->NumberValue();
      %sV8 *obj = new %sV8(value);
      obj->Wrap(args.This());
      return args.This();
    } else {
      // Invoked as plain function `%s(...)`, turn into construct call.
      return scope.Close(constructor->NewInstance(argc, argv));
    }
}
'''% (name, name, name, name, name, name)
  funcs = c["methods"]["public"]
  for func in funcs:
    if func["name"] == name:
      s += GenConstructor(name, func)
      continue
    if func["overwrite"]:
      s += GenOverwrite(name, func)
    else:
      s += GenMethod(name,func)

  s += GenClassInit(name, funcs)
  return s    

def GenInit(cppHeader): 
  s = \
'''
void Init(Handle<Object> exports, Handle<Object> module) {
'''
  for c in cppHeader.classes:
    s += \
'''
    %sV8::Init(exports);
''' % c

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
      g[0]["overwrite"] = False
      funcs.append(g[0])
    
    if len(g) > 1:
      funcs.append({ \
        "name": g[0]["name"], \
        "funcs": g, \
        "overwrite": True \
        })

def GenModule(module, cppHeader):
  s = \
'''
#include <v8.h>
#include <node.h>
#include "%s.h"

using namespace v8;
''' % module

  for func in cppHeader.functions:
    s += GenFunc(func)

  s += GenFuncDecl(cppHeader.functions)

  s += GenConst(cppHeader.defines)

  #to handle the overwrite functions
  for c in cppHeader.classes:    
    GroupFunc(cppHeader.classes[c]["methods"]["public"])

  for c in cppHeader.classes:
    s += GenClassDecl(c, cppHeader.classes[c])
    s += GenClass(c, cppHeader.classes[c])
  
  s += GenInit(cppHeader)

  #tail
  s += \
'''
NODE_MODULE(%s, Init)
'''% module

  return s

def GenC(module, cppHeader):
  f = OUTPUT_DEV_PATH + "/" + module + ".cpp"
  fp = open(f, "w")
  
  fp.write(GenModule(module, cppHeader))
  print "generate " + f
