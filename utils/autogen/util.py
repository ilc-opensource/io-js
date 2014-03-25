import re

reNum = re.compile('[-+]?[1-9]\d*\.\d+|-?0\.\d*[1-9]\d*')
reInt = re.compile('[-+]?\d*')

C2V8 = { \
  "int": ["Int32", "ToInt32", "IntegerValue", "int"], \
  "unsigned int": ["Uint32", "ToUint32", "Uint32Value", "unsigned int" ], \
  "float": ["Number", "ToNumber", "NumberValue", "float"], \
  "bool" : ["Boolean", "ToBoolean", "BooleanValue", "bool"], \
  "char*": ["String", "ToString", "","char*"] \
}

#link other types
C2V8["long"] = C2V8["int"]
C2V8["int8_t"] = C2V8["int"]
C2V8["int16_t"] = C2V8["int"]
C2V8["int32_t"] = C2V8["int"]

C2V8["unsigned long"] = C2V8["unsigned int"]
C2V8["uint8_t"] = C2V8["unsigned int"]
C2V8["uint16_t"] = C2V8["unsigned int"]
C2V8["uint32_t"] = C2V8["unsigned int"]

def GetV8Type(t):
  if (t.replace(" ", "") == 'char*'):
    t = 'char*'

  if t == "void":
    return True

  if t not in C2V8:
    return False  
  return C2V8[t][0]

def GetCValue(value, t):
  if (t.replace(" ", "") == 'char*'):
    raise "Please Use other way to transform char* to String"
  if (value):
    s = "%s->%s()" % (value, C2V8[t][2])
  return s

def GetV8Value(value, t):
  return "%s::New((%s)%s)" % (C2V8[t][0], C2V8[t][3], value)

def CheckSanity(func):
  if func.has_key("overwrite") and func["overwrite"]:
    return True

  for arg in func["parameters"]:
    if not GetV8Type(arg["type"]):
      return False

  if not GetV8Type(func["returns"]):
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
