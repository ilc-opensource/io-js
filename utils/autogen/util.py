import re
from config import *

reNum = re.compile('[-+]?[1-9]\d*\.\d+|-?0\.\d*[1-9]\d*')
reInt = re.compile('[-+]?\d*')

C2V8 = { \
  "int": ["Int32", "ToInt32", "IntegerValue", "int", "IsInt32"], \
  "unsigned int": ["Uint32", "ToUint32", "Uint32Value", "unsigned int", "IsUint32" ], \
  "float": ["Number", "ToNumber", "NumberValue", "float", "IsNumber"], \
  "bool" : ["Boolean", "ToBoolean", "BooleanValue", "bool", "IsBoolean"], \
  "char*": ["v8::String", "ToString", "", "char*", "IsObject"] \
}

#link other types
C2V8["char"] = C2V8["int"]
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

  if f != t and DEBUG == 1 :
    print "Before t %s" %(f)
    print "After t %s" %(t)
  return t;

def GetV8Type(t):
  t = GetIdenticalType(t);
  print "converted " + t
  if t == "void":
    return True

  if t not in C2V8:
    return False  
  return C2V8[t][0]

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

def CheckSanity(func):
  #if func.has_key("override") and func["override"]:
  #  return True
  
  if func["pure_virtual"]:
    print "pure virtual function."
    return False
  
  if re.match(r"operator.*", func["name"]):
    print '''
[Error] Func %s is not converted''' %(func["name"])
    return False

  if not GetV8Type(func["rtnType"]):
    print '''
[Error]Func %s return type: %s can't transfer to V8''' %(func["name"], func["rtnType"])
    return False

  for arg in func["parameters"]:
    print arg["type"]
    if not GetV8Type(arg["type"]):
      print '''
[Error]Func %s arg type: %s can't transfer to V8''' %(func["name"], arg["type"])
      return False

  if not GetV8Type(func["rtnType"]):
    print '''
[Error]Func %s return type: %s can't transfer to V8''' %(func["name"], func["rtnType"])
    return False

  return True

def IsNum(s):
  m = reNum.match(s)
  return m and m.end() == len(s)

def IsInt(s):
  m = reInt.match(s)
  return m and m.end() == len(s)

def IsValidMacro(defines):
  macros = defines.split("//")[0].split()
  if len(macros) != 2:
    return []

  if macros[1].isdigit() or IsNum(macros[1]):
    return macros 

  return []

def RemoveLastComma(s):
  if s.endswith(','):
    return s.rsplit(',', 1)[0]
  else:
    return s


def AddIndent(s, num):
  indent = " " * num
  lines = s.split("\n")
  for idx, line in enumerate(lines):
    lines[idx] = indent + line
  s = "\n".join(lines)
  return s
