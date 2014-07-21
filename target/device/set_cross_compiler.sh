ARDUINO_PATH="$HOME/arduino-1.5.3"
SYSROOT="$ARDUINO_PATH/hardware/tools/sysroots/i586-poky-linux-uclibc"
BIN_ROOT="$ARDUINO_PATH/hardware/tools/sysroots/x86_64-pokysdk-linux/usr/bin/i586-poky-linux-uclibc/i586-poky-linux-uclibc-"
export CC="${BIN_ROOT}gcc --sysroot=$SYSROOT -m32 -march=i586"
export CXX="${BIN_ROOT}gcc --sysroot=$SYSROOT -m32 -march=i586"
export LINK=$CXX
$ARDUINO_PATH/hardware/tools/install_script.sh 
