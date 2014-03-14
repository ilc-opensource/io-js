from config import *
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
  r = re.compile('[-+]?[1-9]\d*\.\d+|-?0\.\d*[1-9]\d*');
  for defines in cppHeader.defines:
    macros = defines.split("//")[0].split()

    #only handle simple define    
    if len(macros) != 2:
      continue

    m = r.match(macros[1])

    if macros[1].isdigit() or (m and m.end() == len(macros[1])):
      GenConst(fp, module, macros[0], macros[1])

  #end of module
  fp.write(\
'''
module.exports = %s;
'''%(module))

  print "generate " + f

