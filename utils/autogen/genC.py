import os
from config import *
from util import *

def GenExport(module):
  s = \
'''
void InitV8(Handle<Object> exports) {

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
  if func.has_key("override") and func["override"]:
    s = "//%s" % func["name"]
  else:
    s = "//%d: %s"% (func["line_number"], func["debug"])

  return s

def GenSetMemberFunc(funcs):
  s = "\nvoid SetMemberFunc(Handle<Object> obj) {"
  for func in funcs:
    flag = False
    if func["override"]:
      for f in func["funcs"]:
        if CheckSanity(f):
          flag = True;
          break;
    else:
      if CheckSanity(func):
        flag = True;

    if flag:
      s += GenSetFunc("obj", func)
  s += "}\n"
  return s

def GenArgName(idx, args):
  return "arg%d"%idx

def GenArgArrayName(idx, args):
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
   
def GenArgTrans(func):
  s = ""
  args = func["parameters"] 
  for idx, arg in enumerate(args):
    if arg["type"] == "void":
      continue
    argName = GenArgName(idx, args)

    argType = GetIdenticalType(arg["type"])

    if argType == "char*":
      s += \
'''
String::AsciiValue strVal(%s->ToString());
char* %s = (char *)*strVal;
'''% (GenArgArrayName(idx, args), argName)
    else:
      s += \
'''
%s %s = %s;
'''% (argType, argName, GetCValue(GenArgArrayName(idx, args), argType))
  return s


def GenCall(func):
  s = "%s(%s)" % (func["name"], GenArgList(func, False))
  return s

def GetRetName(func):
  retType = func["rtnType"]
  if retType == "" or retType == "void":
    return ""
  else:
    return "ret"

def MangleFuncName(func):
  return func["name"]

def GenRet(func):
  retType = func["rtnType"]
  if retType == "" or retType == "void":
    return ""
  else:
    return "%s %s;" % (retType, GetRetName(func)) 

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
      if m["override"]:
        print "[TODO]: override constructor function %s" %(name)
      else:
        s += "    " + GenConstructorDecl(m)
      continue

    s += \
'''
    static v8::Handle<v8::Value> %s(const v8::Arguments& args);''' \
    % MangleFuncName(m)

  s += "\n};\n"
  return s

def GenConstructor(name, func):
  if DEBUG == 1:
    print "Gen Constructor %s" %(name)
  s = \
'''
//constructor
%sV8::%sV8(%s) {
    m_val = new %s(%s);
}
''' % (name, name, GenArgList(func, True), name, GenArgList(func, False))
  return s

def GenMethodHead(className, func):
  if className != "":
    return \
'''
%s
Handle<Value> %sV8::%s(const Arguments& args) {
    HandleScope scope;

    %sV8* obj = ObjectWrap::Unwrap<%sV8>(args.This());
''' % (GetFuncDesc(func), className, MangleFuncName(func), className, className)
  else:
    return \
'''
%s
Handle<Value> %s(const Arguments &args) {
    HandleScope scope;
'''%(GetFuncDesc(func), func["name"] + 'V8')
 
def GenMethodCall(func, className):
  s = ""
  sRetType = GetIdenticalType(func["rtnType"])
  if className == "":
    objStr = ""
  else:
    objStr = '''
obj->m_val->
'''

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
    % (sRetType, GetRetName(func), objStr, GenCall(func), GetV8Value(GetRetName(func), sRetType))

  return s

def GenOverride(className, func):
  s = GenMethodHead(className, func)

  for f in func["funcs"]:
    if not CheckSanity(f):
      continue;
    temp  =  GenArgTrans(f)
    temp +=  GenMethodCall(f, className)
    s += \
'''
    %s
    if (args.Length() == %d) {
%s
    }
''' %(GetFuncDesc(f), \
      len(f["parameters"]), \
      AddIndent(temp, 8))

  s += '''
    return scope.Close(Undefined());
}
'''

  return s

def GenMethod(className, func):
  if DEBUG == 1:
    print ">>Gen func %s" %(MangleFuncName(func))

  if not CheckSanity(func):
    return GetFuncDesc(func)

  s = GenMethodHead(className, func)
  s += AddIndent(GenArgTrans(func), 4)
  s += AddIndent(GenMethodCall(func, className), 4)
  s += "\n}"
  return s

def GenClassInit(className, funcs) :
  s = \
'''
void %sV8::Init(Handle<Object> exports) {

    // Prepare constructor template
    Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
    tpl->SetClassName(String::NewSymbol("%s"));
    tpl->InstanceTemplate()->SetInternalFieldCount(1);

    // Prototype ''' % (className, className)
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
}''' % (className)
  return s
  
def GenClass(className, c):
  if DEBUG == 1:
    print "Begin: gen Class %s." %(className)

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
'''% (className, className, className, className, className, className)
  
  if DEBUG == 1:
    print "End: gen New."

  funcs = c["methods"]["public"]
  for func in funcs:
    if func["override"]:
      if func["name"] == className:
        print "[TODO]: override constructor function %s" %(className)
      else:
        s += GenOverride(className, func)
    else:
      if func["name"] == className:
        s += GenConstructor(className, func)
      else:
        s += GenMethod(className, func)

  s += GenClassInit(className, funcs)
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

#include <v8.h>
#include <node.h>
#include "%s.h"

using namespace v8;
''' % (module.upper(), module.upper(), module)
  
  for c in cppHeader.classes:
    s += GenClassDecl(c, cppHeader.classes[c])
  
  s += "\n#endif"
  return s

def GenModule(module, cppHeader):

  s = '#include "%s_addon.h"\n' % module
  
  if DEBUG == 1:
    print ">>>>Begin: gen Class"

  for c in cppHeader.classes:
    s += GenClass(c, cppHeader.classes[c])
  
  if DEBUG == 1:
    print "<<<<End: gen Class"
    print ">>>>Begin: gen function"

  for func in cppHeader.functions:
    s += GenFunc(func)

  if DEBUG == 1:
    print "<<<<End: gen func"
    print ">>>>Begin: set Member func"
  
  s += GenSetMemberFunc(cppHeader.functions)

  if DEBUG == 1:
    print "<<<<End: set Member func"
    print ">>>>Begin: gen const"
  
  s += GenConst(cppHeader.defines)
 
  if DEBUG == 1:
    print "<<<<End: gen const"
    print ">>>>Begin: gen init"
  
  s += GenInit(cppHeader)

  if DEBUG == 1:
    print "<<<<End: gen init"
  #tail
  s += \
'''
NODE_MODULE(%s, Init)
'''% module
  
  if DEBUG == 1:
    print "<<End: gen Class"

  return s

def GenC(module, cppHeader):
  if DEBUG == 1:
    print ">>Start: gen Module."

  f = OUTPUT_DEV_PATH + "/" + module + "_addon.cpp"
  fp = open(f, "w")  
  fp.write(GenModule(module, cppHeader))

  print "generate " + f

  f = OUTPUT_DEV_PATH + "/" + module + "_addon.h"
  fp = open(f, "w")  
  fp.write(GenModuleDecl(module, cppHeader))

  print "generate " + f
