INPUT_DECL_PATHS  = [
  "../../arduino-1.5.3/hardware/arduino/x86/cores/arduino/", 
  "../../arduino-1.5.3/hardware/arduino/x86/variants/galileo_fab_c/",
  "../../c_decl/"
]

OUTPUT_COMP_PATH     = '../../lib/companion'
OUTPUT_DEV_PATH      = '../../lib/device/src'
OUTPUT_CMD_MAP_PATH  = '../../lib/dispatcher/map'
EXPORT_DEF           = 'main.h'
EXPORT_CPP           = 'main.cpp'
EXPORT_MODULE        = 'galileo'

GYP_PATH             = '../../lib/device/'
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_FILE             = 'binding.gyp'

DEBUG = 1

