from config import *
from util import *

def GenArgsMap(args):
  if len(args) == 0:
    s = '"parameters": []'
    return s

  s = \
'''"parameters": [
'''
  for idx, arg in enumerate(args):
    argName = arg["name"]
    if len(argName) == 0:
      argName = "arg%d"%idx

    s += \
'''  {
    "name": "%s",
    "type": "%s"
  },
'''%(argName, GetV8Type(arg["type"])) 
  
  s = RemoveLastComma(s)
  s += "\n]"
  return s

def GenRetMap(ret):
  if ret == "":
    return '"return": []'
  else:
    return '"return": ["%s"]' % (GetV8Type(ret))

def GenFuncMap(module, func):  
  if func.has_key("override") and func["override"]:
    overrideStr = "true"
    argStr = '"parameters": []'
    retStr = '"return":[]'
  else:
    overrideStr = "false"
    argStr = GenArgsMap(func["parameters"])
    retStr = GenRetMap(func["rtnType"])

  return '''
"%s": {
  "override" : %s,
%s,
%s
},
''' % (func["name"], \
       overrideStr, \
       AddIndent(argStr, 2), \
       AddIndent(retStr, 2))

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

  mapStr = GenPropertyMap(c["properties"]["public"])

  methodStr = ''
  methods = c["methods"]["public"]
  for m in methods:
    methodStr += GenFuncMap(module, m)

  methodStr = RemoveLastComma(methodStr)
  
  return '''
"%s" : {

  "properties": [
%s
  ],

  "methods" : {
%s
  }
}
'''  % (name, AddIndent(mapStr, 4), AddIndent(methodStr, 4))

def GenDefineMap(defines):
  s = ''
  for idx, define in enumerate(defines):
    macros = IsValidMacro(define)
    if len(macros) == 0:
      continue
    s += '"' + macros[0] + '": ' + macros[1] + ',\n'

  return RemoveLastComma(s)  

def GenJsApiMap(module, cppHeader):

  totalStr = ''

  s = '''
  "name" : "%s",
''' % module

  #generate map of class
  t = ''
  for c in cppHeader.classes:
    t += GenClassMap(module, c, cppHeader.classes[c])

  s += '''
  "classes" : {
%s
  },
''' % AddIndent(t, 4)

  #s = RemoveLastComma(s)
  
  t = GenDefineMap(cppHeader.defines)
  s += '''
  "constants" : {
%s
  },
''' % AddIndent(t, 4)  

  t = ''
  #generate map of functions
  for idx, func in enumerate(cppHeader.functions):
    t += GenFuncMap(module, func)    
  
  t = RemoveLastComma(t)
  s += '''
  "functions" : {
%s
  }
''' % AddIndent(t, 4)  
  
  #generate outermost {}
  rs = "{\n"
  rs += AddIndent(s, 2)
  rs += "\n}"

  #write to map file
  f = OUTPUT_CMD_MAP_PATH + "/" + module + "_map.json"  
  
  fp = open(f, "w")
  fp.write(rs)
  printDbg( "generate " + f)
    
