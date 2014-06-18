INPUT_DECL_PATHS  = [
  "../../target/device/libio/export"
#   "../../../pia-sdk-repo/iolib/arduino/arduiPIA.h"
]

VERSION              = '0.0.1'
TARGET               = 'galileo'
OUTPUT_COMP_PATH     = '../../target/companion/lib/board/'
OUTPUT_DEV_PATH      = '../../target/device/board/src'
OUTPUT_SERVER_PATH   = '../../target/server/lib/board'
OUTPUT_CMD_MAP_PATH  = '../../target/map/'
EXPORT_DEF           = 'main.h'
EXPORT_CPP           = 'main.cpp'
CALLBACK_DEF         = '_callback.h'
CALLBACK_CPP         = '_callback.cpp'
EXPORT_MODULE        = 'galileo'

GYP_PATH             = OUTPUT_DEV_PATH + '/../'
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_FILE             = 'binding.gyp'

INC_MAKEFILE         = 'autogen.make'

DEBUG = 1
