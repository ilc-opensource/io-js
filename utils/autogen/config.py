
import os

INPUT_DIR = '../../../face_detection'
INPUT_DECL_PATHS  = [
   INPUT_DIR + "/face_detection.h"
#  "../../target/device/libio/export"
#   "../../../pia-sdk-repo/iolib/arduino/arduiPIA.h"
]
INPUT_LIB_PATH = INPUT_DIR + '/build/libfd.a'

ATLAS_PATH           = '../../../Atlas'
NODERED_PATH         = ATLAS_PATH + '/iot/sample/face_detection' 
INSTALL_DIR          = NODERED_PATH + '/addon'
EXTRA_LIB            = '/usr/local/lib/libopencv_calib3d.so /usr/local/lib/libopencv_core.so /usr/local/lib/libopencv_features2d.so /usr/local/lib/libopencv_flann.so /usr/local/lib/libopencv_highgui.so /usr/local/lib/libopencv_imgproc.so /usr/local/lib/libopencv_ml.so /usr/local/lib/libopencv_objdetect.so /usr/local/lib/libopencv_photo.so /usr/local/lib/libopencv_stitching.so /usr/local/lib/libopencv_superres.so /usr/local/lib/libopencv_ts.a /usr/local/lib/libopencv_video.so /usr/local/lib/libopencv_videostab.so'

AUTOGEN_TEST = 0

DEBUG = 1
