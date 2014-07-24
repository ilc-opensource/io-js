INPUT_DECL_PATHS  = [
  "../../../mug/include"
#   "../../../pia-sdk-repo/iolib/arduino/arduiPIA.h"
]

AUTOGEN_TEST = 0

VERSION              = '0.0.1'
TARGET               = 'galileo'
OUTPUT_COMP_PATH     = '../../target/companion/lib/board/'
OUTPUT_DEV_PATH      = '../../target/device/src'
OUTPUT_SERVER_PATH   = '../../target/server/lib/board'
OUTPUT_CMD_MAP_PATH  = '../../target/desc/'
EXPORT_DEF           = 'main.h'
EXPORT_CPP           = 'main.cpp'
GLOBAL_DEF           = '_globalvar.h'
GLOBAL_CPP           = '_globalvar.cpp'
EXPORT_MODULE        = 'galileo'

GYP_PATH             = OUTPUT_DEV_PATH + '/../'
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_LIB              = "'../../../../mug/bin/libmug.a'"
GYP_INC              = ""
GYP_FILE             = 'binding.gyp'
Global_CLASS_VAR_FILE    = 'globalClassVarSetterGetter.js'
INSTANCE_V8CLASS_ARG     = '__instanceV8' # used to generate a V8 class Object without
                                          # corresponding C class generated.

INC_MAKEFILE         = 'autogen.make'

DEBUG = 1
