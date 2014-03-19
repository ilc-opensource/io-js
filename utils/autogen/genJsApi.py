from config import *
from util import *
import re

def GenArgs(hdl, args):
  for idx, arg in enumerate(args):
    argName = arg["name"]
    if len(argName) == 0:
      argName = "arg%d"%(idx)

    hdl.write(argName)

    if idx == (len(args) - 1):
      hdl.write("){\n")
    else:
      hdl.write(", ")

#genreate functions
#TODO: eliminate static functions
def GenFunc(hdl, module, func):
  hdl.write("\n%s.%s = function("%(module, func["name"]))
  GenArgs(hdl, func["parameters"])
  hdl.write(\
'''
  console.log("%s")
}
'''%(func["name"]))
 
def GenConst(hdl, module, const, val):
  hdl.write(\
'''
%s.%s = %s;
'''%(module, const, val))
  
def GenClass(hdl, module, name, c):
  hdl.write(\
'''
%s = function(options) {
};
'''%(name))

  for m in c["methods"]["public"]:
    hdl.write("\n%s.prototype.%s = function("%(name, m["name"]))

    args = m["parameters"]
    GenArgs(hdl, args)

    hdl.write(\
'''
  console.log("%s.%s");
}
'''%(name, m["name"]))

  if module != name:
    hdl.write("\n%s.%s = %s\n"%(module, name, name))
    
def GenJsApi(module, cppHeader):
  f = OUTPUT_COMP_PATH + "/" + module + ".js"

  fp = open(f, "w")

  for c in cppHeader.classes:
    GenClass(fp, module, c, cppHeader.classes[c])

  #gen external functions
  for func in cppHeader.functions:
    GenFunc(fp, module, func)

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

  print "generate " + f

