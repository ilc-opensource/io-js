from config import *
from util import *

def GenArgsMap(args):
  if len(args) == 0:
    s = '\n"parameters": []'
    return s

  s = \
'''
"parameters": [
'''
  for idx, arg in enumerate(args):
    argName = arg["name"]
    if len(argName) == 0:
      argName = "arg%d"%idx

    s += \
'''  {
    "name": "%s",
    "type": "%s"
  }'''%(argName, arg["type"]) 
    
    if idx == len(args) - 1:
      s += "\n"
    else:
      s += ",\n"

  s += "]"
  return s

def GenFuncMap(module, func):  
  t  = '\n\n"%s": {' % func["name"]
  t += AddIndent(GenArgsMap(func["parameters"]), 2)
  t += ",\n"

  if len(func["returns"]) == 0:
    r = '"return":[]'
  else:
    r = '"return": ["%s"]' % (func["returns"])
  t += AddIndent(r, 2)
  t += '\n}'
  s = AddIndent(t, 2)    
  return s

def GenPropertyMap(props):
  s = ''
  for p in props:
    s += '''
{
  "name" : "%s",
  "type" : "%s"
},''' %(p['name'], p['type'])
  
  s = RemoveLastComma(s);
  s = AddIndent(s, 2)
  return s

def GenClassMap(module, name, c):
  s = '\n\n"properties": ['
  s += GenPropertyMap(c["properties"]["public"])
  s += '\n]\n'

  s += '\n"methods": {'
  methods = c["methods"]["public"]
  
  for m in methods:
    s += GenFuncMap(module, m)
    s += ','

  s = RemoveLastComma(s)
  s += '\n}'
  return s

def GenDefineMap(defines):
  r = "\nconstants: {"
  for idx, define in enumerate(defines):
    macros = IsValidMacro(define)
    if len(macros) == 0:
      continue
    r += AddIndent('\n"' + macros[0] + '": ' + macros[1] + ',', 2)

  RemoveLastComma(r)
  r += '\n}\n'
  return r

def GenJsApiMap(module, cppHeader):
  s = '"%s" : {'%(module)  

  #generate map of class
  for c in cppHeader.classes:
    t = AddIndent(GenClassMap(module, c, cppHeader.classes[c]), 2)
    if c != module:
      t = \
'''
"%s":{%s
},
''' %(c, t)
      t = AddIndent(t, 2)
    s += t

  s = RemoveLastComma(s)
  
  if len(cppHeader.defines) > 0:
    s += ','
    s += AddIndent(GenDefineMap(cppHeader.defines), 2)

  if len(cppHeader.functions) > 0:
    s += ','

  #generate map of functions
  for idx, func in enumerate(cppHeader.functions):
    s += GenFuncMap(module, func)
    s += ","
  
  s = RemoveLastComma(s) + "\n}"
  
  #generate outermost {}
  rs = "{\n"
  rs += AddIndent(s, 2)
  rs += "\n}"

  #write to map file
  f = OUTPUT_CMD_MAP_PATH + "/" + module + "_map.json"  
  
  fp = open(f, "w")
  fp.write(rs)
  printDbg( "generate " + f)
    
