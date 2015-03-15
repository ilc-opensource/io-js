
import os

INPUT_DIR = '../../../face_detection'
INPUT_DECL_PATHS  = [
   INPUT_DIR + "/face_detection.h"
#  "../../target/device/libio/export"
#   "../../../pia-sdk-repo/iolib/arduino/arduiPIA.h"
]

ATLAS_PATH           = '../../../Atlas'
NODERED_PATH         = ATLAS_PATH + '/iot/sample/face_detection'  
INSTALL_DIR          = NODERED_PATH + '/addon'
OPENCV_LIB           = '/usr/local/lib/libopencv_calib3d.dylib /usr/local/lib/libopencv_core.dylib /usr/local/lib/libopencv_features2d.dylib /usr/local/lib/libopencv_flann.dylib /usr/local/lib/libopencv_highgui.dylib /usr/local/lib/libopencv_imgcodecs.dylib /usr/local/lib/libopencv_imgproc.dylib /usr/local/lib/libopencv_ml.dylib /usr/local/lib/libopencv_objdetect.dylib /usr/local/lib/libopencv_photo.dylib /usr/local/lib/libopencv_shape.dylib /usr/local/lib/libopencv_stitching.dylib /usr/local/lib/libopencv_superres.dylib /usr/local/lib/libopencv_ts.a /usr/local/lib/libopencv_video.dylib /usr/local/lib/libopencv_videoio.dylib /usr/local/lib/libopencv_videostab.dylib'
INPUT_LIB_PATH       = '../' + os.path.relpath(INPUT_DIR, INSTALL_DIR) + '/build/libfd.a'

GYP_LIB              = '"' + INPUT_LIB_PATH + ' ' + OPENCV_LIB + '"'


##### DO NOT CHANGE BELOW VAR ######

AUTOGEN_TEST = 0

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

#NODERED_PATH         = '../../../node-red/nodes/Atlas/iot/funcNodes/' # Please set directory where nodes generated 
GYP_PATH             = OUTPUT_DEV_PATH + '/../' 
GYP_SRC_PATH         = 'src/' #the relative path of GYP_SRC_PATH to OUTPUT_DEV_PATH from 
GYP_FILE             = 'binding.gyp'
Global_CLASS_VAR_FILE    = 'globalClassVarSetterGetter.js'
INSTANCE_V8CLASS_ARG     = '__instanceV8' # used to generate a V8 class Object without
                                          # corresponding C class generated.

INC_MAKEFILE         = 'autogen.make'

DEBUG = 1
