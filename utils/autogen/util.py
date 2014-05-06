import re
from config import *
from termcolor import colored
import globalVar

CURR_MODULE = "-"

summary = {}

def SetPrintModule(m):
  global CURR_MODULE
  CURR_MODULE = m

def UnsetPrintModule():
  global CURR_MODULE
  CURR_MODULE = "-"

def printDbg(str):
  if not DEBUG:
    return

  print colored("[%s][dbg] " % CURR_MODULE + str, "blue")

def printLog(str):
  print colored(str, "green")

def printVerb(str):
  print "[%s][veb] " % CURR_MODULE + str

def printWarn(str):
  print colored("[%s][warn] " % CURR_MODULE + str, "yellow")

def printErr(str):
  print colored("[%s][err] " % CURR_MODULE + str, "red")


reFloat = re.compile('[-+]?[1-9]\d*\.\d*[fF]?|-?0\.\d*[1-9]\d*[fF]?')
reEFloat = re.compile('[-+]?[1-9]\d*\.?\d*[eE][+-]?\d*|-?0\.\d*[1-9]\d*[eE][+-]?\d*')
reHexInt = re.compile('[-+]?0[xX][0-9a-fA-F]+[uU]?[lL]?[lL]?')
reOctInt = re.compile('[-+]?[1-9][0-9]*[uU]?[lL]?[lL]?')
reDecInt = re.compile('[-+]?0[0-7]*[uU]?[lL]?[lL]?')
reString = re.compile('\".*\"|\'.*\'', re.M and re.S)

C2V8 = { \
  "int": ["Int32", "ToInt32", "IntegerValue", "int", "IsInt32"], \
  "unsigned int": ["Uint32", "ToUint32", "Uint32Value", "unsigned int", "IsUint32" ], \
  "float": ["Number", "ToNumber", "NumberValue", "float", "IsNumber"], \
  "bool" : ["Boolean", "ToBoolean", "BooleanValue", "bool", "IsBoolean"], \
  "char*": ["v8::String", "ToString", "", "char*", "IsString"] \
}

#link other types
C2V8["char"] = C2V8["int"]
C2V8["byte"] = C2V8["int"]
C2V8["long"] = C2V8["int"]
C2V8["boolean"] = C2V8["bool"]

C2V8["size_t"] = C2V8["unsigned int"]
C2V8["uint8_t *"] = C2V8["char*"]

def GetIdenticalType(t):
  f = t
  t = t.replace("register ", "")
  t = t.replace("const ", "")
  t = t.replace("extern ", "")
  t = t.replace("auto ", "")
  t = t.replace("inline ", "")

  if t.find('''*''') == -1 and t.find('''&''') == -1:
    if t.find("unsigned") != -1 or t.find("uint") != -1 or t.find("__u") != -1:
      t = "unsigned int"
    elif t.find("signed") != -1 or t.find("int") != -1 or t.find("__s") != -1:
      t = "int"
  else:
    t = t.replace('''uint8_t''', "char")
    t = t.replace('''__u8''', "char")
    if t.replace(" ","") == "char*":
      t = "char*"

  return t;

def GetV8Type(t):
  if t == "" or t == "void":
    return True

  t = GetIdenticalType(t);  

  if t not in C2V8:
    return False  
  return C2V8[t][0]

def GetConvToCFunc(t):
  t = GetIdenticalType(t);
  if (t == 'char*'):
    raise "Please Use other way to transform char* to String"
  return C2V8[t][2]

def GetCValue(value, t):
  t = GetIdenticalType(t);
  if (t == 'char*'):
    raise "Please Use other way to transform char* to String"
  if (value):
    s = "%s->%s()" % (value, C2V8[t][2])
  return s

def GetV8Value(value, t):
  t = GetIdenticalType(t);
  return "%s::New((%s)%s)" % (C2V8[t][0], C2V8[t][3], value)

def GetV8TypeCheck(t):
  t = GetIdenticalType(t);
  return C2V8[t][4]

def IsV8FuncGen(func):
  flag = False
  if func["override"]:
    for f in func["funcs"]:
      if CheckSanity(f):
        flag = True;
        break;
  else:
    if CheckSanity(func):
      flag = True;
  return flag

def GetBasicType(arg):
  argType = arg["type"]
  if arg.has_key("pointer") and arg["pointer"] == 1:
    starIndex = argType.index("*")
    argBasicType = argType[:starIndex].strip()
  else:
    argBasicType = argType
  return argBasicType

def IsStructArg(argType):
  classes = globalVar.cppHeader.classes
  return (classes.has_key(argType) and \
          ((classes[argType]["declaration_method"] == "struct") or \
           (classes[argType]["declaration_method"] == "typedef") and \
            (classes[argType]["name"] == "struct")));

def CheckArgSanity(arg):
  print arg
  if arg.has_key("array") and arg["array"] == 1:
    return False

  if arg.has_key("pointer") and arg["pointer"] > 1 :
    return False

  # check sanity of function pointer
  if (arg.has_key("function_pointer") and \
      isinstance(arg["function_pointer"], dict) and len(arg["function_pointer"]) > 0) :
    if not GetV8Type(arg["function_pointer"]["rtnType"]):
      return False
    for argT in arg["function_pointer"]["paraTypes"]:
      argTDict = {"type": argT}
      if not CheckArgSanity(argTDict):
        return False
    return True

  # check sanity of struct
  argType = arg["type"]
  argBasicType = GetBasicType(arg)

  if (IsStructArg(argBasicType)):
    classes = globalVar.cppHeader.classes
    props = classes[argBasicType]["properties"]["public"]
    for idxs, prop in enumerate(props):
      if not CheckArgSanity(prop):
        return False
    return True

  if not GetV8Type(argType):
    return False
  return True

def CheckSanity(func):
  if func["pure_virtual"]:
    printDbg("pure virtual function is not allowed")
    return False

  if re.match(r"operator.*", func["name"]):
    printDbg("Func %s is not converted" %(func["name"]))
    return False

  # Check return type
  if not GetV8Type(func["rtnType"]):
    printDbg("Func %s return type: %s can't transfer to V8" %(func["name"], func["rtnType"]))
    return False

  # Check parameters
  for arg in func["parameters"]:
    if not CheckArgSanity(arg):
      printDbg("Func %s arg type: %s can't transfer to V8" %(func["name"], arg["type"]))
      return False
  return True

def IsEFloat(s):
  m = reEFloat.match(s)
  return m and m.end() == len(s)

def IsFloat(s):
  m = reFloat.match(s)
  return m and m.end() == len(s)

def IsString(s):
  m = reString.match(s)
  return m and m.end() == len(s)

def IsInt(s):
  m = reHexInt.match(s)
  if m and m.end() == len(s):
    return True
  m = reDecInt.match(s)
  if m and m.end() == len(s):
    return True
  m = reOctInt.match(s)
  if m and m.end() == len(s):
    return True
  return False

def IsValidMacro(defines):
  defines = defines.expandtabs(1);
  defines = re.sub(r' +', " ", defines)

  macros = defines.split("//")[0].split(" ", 1)
  if len(macros) != 2:
    return []

  macros[0] = macros[0].strip()
  macros[1] = macros[1].strip()

  if IsInt(macros[1]) or IsString(macros[1]) or IsFloat(macros[1]) or IsEFloat(macros[1]):
    return macros 

  return []

def RemoveLastComma(s):
  return s.rsplit(',', 1)[0]


def AddIndent(s, num):
  indent = " " * num
  lines = s.split("\n")
  for idx, line in enumerate(lines):
    lines[idx] = indent + line
  s = "\n".join(lines)
  return s

def ParseFuncPointTypedef(type_t):
  stack = type_t.split("(", 1);
  if stack[0] != type_t:
    retType = stack[0].strip()
    argTypes = stack[1].split(")", 1)
    if argTypes[0] == stack[1][0:-1]:
      argTypes = argTypes[0].split(",")
      for i in range(len(argTypes)):
        argTypes[i] = argTypes[i].strip()
      type_t = { \
        "rtnType" : retType, \
        "paraTypes": argTypes \
      }
  return type_t

def ParseTypedefs(typedefs):
  for key in typedefs.keys():
    value = re.sub(r" +", " ", typedefs[key])
    funcPointerType = ParseFuncPointTypedef(value)
    if funcPointerType == value:
      valueFP = {
        "function_pointer" : 0, \
        "type" : funcPointerType, \
      }
    else:
      valueFP = {
        "function_pointer" : 1, \
        "type" : funcPointerType, \
      }
    typedefs[key] = valueFP

def ParseFuncPointerParams(params, typedefs):
  for idx, arg in enumerate(params):
    argType = arg["type"]
    lparenCnt = argType.count("(")
    rparenCnt = argType.count(")")

    if arg["name"] == "" and lparenCnt >= 2 and lparenCnt == rparenCnt:
      lstack = argType.split("(");
      starIndex = lstack[1].find("*")
      if starIndex != -1:
        # get arg name of function pointer
        rparenIndex = lstack[1].find(")")
        params[idx]["name"] = lstack[1][starIndex+1:rparenIndex]

        # get arg type of function pointer
        type_t = lstack[0] + "(" + lstack[2]
        funcPointerType = ParseFuncPointTypedef(type_t)

        if (funcPointerType != type_t):
          params[idx]["function_pointer"] = funcPointerType
        continue

    # expand typedef
    if typedefs.has_key(argType):
      value = typedefs[argType]
      if value["function_pointer"] == 1:
        params[idx]["function_pointer"] = value["type"]
      else:
        params[idx]["type"] = value["type"]
        params[idx]["function_pointer"] = {}
      continue

    params[idx]["function_pointer"] = {}

def ParseFuncPoint(cppHeader):
  for c in cppHeader.classes:
    for idx in range(len(cppHeader.classes[c]["methods"]["public"])):
      ParseFuncPointerParams(cppHeader.classes[c]["methods"]["public"][idx]["parameters"], cppHeader.typedefs)

  for idx in range(len(cppHeader.functions)):
    ParseFuncPointerParams(cppHeader.functions[idx]["parameters"], cppHeader.typedefs)
