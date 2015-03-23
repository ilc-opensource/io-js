VERSION = '0.0.1'
TARGET_DIR           = '../../target'
VERSION              = '0.0.1'
TARGET               = 'galileo'
ADDON_DIR            = TARGET_DIR + '/device'
OUTPUT_COMP_PATH     = TARGET_DIR + '/companion/lib/board/'
OUTPUT_DEV_PATH      = ADDON_DIR + '/src'
OUTPUT_SERVER_PATH   = TARGET_DIR + '/server/lib/board'
OUTPUT_CMD_MAP_PATH  = TARGET_DIR + '/desc/'
EXPORT_DEF           = 'main.h'
EXPORT_CPP           = 'main.cpp'
GLOBAL_DEF           = '_globalvar.h'
GLOBAL_CPP           = '_globalvar.cpp'
EXPORT_MODULE        = 'galileo'

GYP_PATH             = OUTPUT_DEV_PATH + '/../' 
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_FILE             = 'binding.gyp'
GLOBAL_CLASS_VAR_FILE    = 'globalClassVarSetterGetter.js'
INSTANCE_V8CLASS_ARG     = '__instanceV8' # used to generate a V8 class Object without
                                          # corresponding C class generated.

INC_MAKEFILE         = 'autogen.make'

