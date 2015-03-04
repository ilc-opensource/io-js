INPUT_DIR = '../../../face_detection'

INPUT_DECL_PATHS  = [
   INPUT_DIR + "/face_detection.h"
#  "../../target/device/libio/export"
#   "../../../pia-sdk-repo/iolib/arduino/arduiPIA.h"
]

AUTOGEN_TEST = 0

TARGET_DIR           = '../../target'
VERSION              = '0.0.1'
TARGET               = 'galileo'
OUTPUT_COMP_PATH     = TARGET_DIR + '/companion/lib/board/'
OUTPUT_DEV_PATH      = TARGET_DIR + '/device/src'
OUTPUT_SERVER_PATH   = TARGET_DIR + '/server/lib/board'
OUTPUT_CMD_MAP_PATH  = TARGET_DIR + '/desc/'
EXPORT_DEF           = 'main.h'
EXPORT_CPP           = 'main.cpp'
GLOBAL_DEF           = '_globalvar.h'
GLOBAL_CPP           = '_globalvar.cpp'
EXPORT_MODULE        = 'galileo'

#NODERED_PATH         = '../../../node-red/nodes/Atlas/iot/funcNodes/' # Please set directory where nodes generated 
ATLAS_PATH           = '../../../Atlas'
NODERED_PATH         = '../../../Atlas/iot/sample/face_detection' # Please set directory where nodes generated 
GYP_PATH             = OUTPUT_DEV_PATH + '/../' 
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_FILE             = 'binding.gyp'
GYP_LIB              = '"' + '../' +  INPUT_DIR + '/build/libfd.a /usr/local/lib/libopencv_calib3d.dylib /usr/local/lib/libopencv_core.dylib /usr/local/lib/libopencv_features2d.dylib /usr/local/lib/libopencv_flann.dylib /usr/local/lib/libopencv_highgui.dylib /usr/local/lib/libopencv_imgcodecs.dylib /usr/local/lib/libopencv_imgproc.dylib /usr/local/lib/libopencv_ml.dylib /usr/local/lib/libopencv_objdetect.dylib /usr/local/lib/libopencv_photo.dylib /usr/local/lib/libopencv_shape.dylib /usr/local/lib/libopencv_stitching.dylib /usr/local/lib/libopencv_superres.dylib /usr/local/lib/libopencv_ts.a /usr/local/lib/libopencv_video.dylib /usr/local/lib/libopencv_videoio.dylib /usr/local/lib/libopencv_videostab.dylib' + '"'
Global_CLASS_VAR_FILE    = 'globalClassVarSetterGetter.js'
INSTANCE_V8CLASS_ARG     = '__instanceV8' # used to generate a V8 class Object without
                                          # corresponding C class generated.

INC_MAKEFILE         = 'autogen.make'

DEBUG = 1
