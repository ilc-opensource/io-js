* Set Arduino path
  - Open ext.gypi and set arduino_path and libio_path
  - CC/CXX/LINK to Arduino toolchain 

* gyp configuration
  - node-gyp configure --arch=ia32 --target=0.8.18

* gyp build
  - node-gyp build
