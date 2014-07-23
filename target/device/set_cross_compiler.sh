ARDUINO_PATH="$HOME/arduino-1.5.3"
MACHINE_TYPE=`getconf LONG_BIT`
if [ $MACHINE_TYPE -eq 32 ]
then
  ARCH=i586
else
  if [ $MACHINE_TYPE -eq 64 ]
  then
    ARCH=x86_64
  else
     echo 'Error machine type:', $MACHINE_TYPE
  fi
fi
SYSROOT="$ARDUINO_PATH/hardware/tools/sysroots/i586-poky-linux-uclibc"
BIN_ROOT="$ARDUINO_PATH/hardware/tools/sysroots/$ARCH-pokysdk-linux/usr/bin/i586-poky-linux-uclibc/i586-poky-linux-uclibc-"
export CC="${BIN_ROOT}gcc --sysroot=$SYSROOT -m32 -march=i586"
export CXX="${BIN_ROOT}gcc --sysroot=$SYSROOT -m32 -march=i586"
export LINK=$CXX
$ARDUINO_PATH/hardware/tools/install_script.sh 
