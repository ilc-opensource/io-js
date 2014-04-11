from config import *
from util import *
import re
from genC import GroupFunc

def GenArgs(hdl, args):
  for idx, arg in enumerate(args):
    argName = arg["name"]
    if len(argName) == 0:
      argName = "arg%d"%(idx)

    hdl.write(argName)
    hdl.write(", ")
  
  if len(args) > 0:
    hdl.seek(hdl.tell() - 2)
    
  hdl.write("){\n")


def GenConst(hdl, module, const, val):
  hdl.write(\
'''
%s.%s = %s;
'''%(module, const, val))

def GetFuncName(f, override):
  fname = f['name']
  if override:
    fname += "With"
    for arg in f["parameters"]:
      t = re.sub('\s+', "",arg["type"])
      t = t.capitalize()
      fname += t

  return fname


def GenMethod(hdl, f, override, moduleName, className):
  funcName = GetFuncName(f, override)
  if className == "":
    name_t = moduleName
    hdl.write("\n%s.%s = function(" %(name_t, funcName))
  else:
    name_t = className
    hdl.write("\n%s.prototype.%s = function(" %(name_t, funcName))

  args = f["parameters"]
  GenArgs(hdl, args)

  hdl.write(\
'''
  console.log("%s.%s");
};
'''%(name_t, funcName))

#genreate functions
def GenFunc(hdl, func, moduleName, className):
  if func.has_key("override") and func["override"]:
    for f in func["funcs"]:
      GenMethod(hdl, f, True, moduleName, className)
  else:
    GenMethod(hdl, func, False, moduleName, className)

def GenClass(hdl, module, className, c):
  hdl.write(\
'''
%s = function(options) {
};
'''%(className))
  
  funcs = c["methods"]["public"]
  for func in funcs:
    GenFunc(hdl, func, module, className)

  if module != className:
    hdl.write("\n%s.%s = %s\n"%(module, className, className))
    
def GenJsApi(module, cppHeader):
  f = OUTPUT_COMP_PATH + "/" + module + ".js"

  fp = open(f, "w")

  for c in cppHeader.classes:
    GenClass(fp, module, c, cppHeader.classes[c])

  #gen external functions
  for func in cppHeader.functions:
    GenFunc(fp, func, module, "")

  #gen constant
  for define in cppHeader.defines:

    macros = IsValidMacro(define)

    if len(macros) != 0:
      GenConst(fp, module, macros[0], macros[1])

  #end of module
  fp.write(\
'''
module.exports = %s;
'''%(module))

  printDbg("generate " + f)

