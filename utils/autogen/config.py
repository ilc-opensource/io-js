INPUT_DECL_PATHS  = [
#  "../../../arduino-1.5.3/hardware/arduino/x86/cores/arduino/", 
#  "../../../arduino-1.5.3/hardware/arduino/x86/variants/galileo_fab_c/",
#  "../../c_decl/"
#  "../../test_struct/"
#  "../../test_fp/"
#  "../../test_pointer/"
  "../../../libio/export"
]

TARGET               = 'galileo'
OUTPUT_COMP_PATH     = '../../lib/companion/lib/board/'
OUTPUT_DEV_PATH      = '../../lib/device/src'
OUTPUT_SERVER_PATH   = '../../lib/server/lib/board'
OUTPUT_CMD_MAP_PATH  = '../../lib/map/'
EXPORT_DEF           = 'main.h'
EXPORT_CPP           = 'main.cpp'
CALLBACK_DEF           = '_callback.h'
CALLBACK_CPP           = '_callback.cpp'
EXPORT_MODULE        = 'galileo'

GYP_PATH             = '../../lib/device/'
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_FILE             = 'binding.gyp'

DEBUG = 1
