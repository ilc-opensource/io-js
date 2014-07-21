# IOT IO Library

A Javascript based IO library. It provides Arduino like APIs.

## Target execution environment

* Intel Galileo
* Intel Edison (TODO) 

## Preinstall

* Please follow the document [Intel Galileo Getting Started](https://communities.intel.com/docs/DOC-22796) to install Yocto on Galileo and boot your board from a SD card

### Native compilation

If you have installed native gcc on Galileo board, you can login Galileo and install with npm. Please make sure node-gyp is installed

```shell
npm install -g node-gyp
```

Now you can begin to install iot-io and it may take several minutes.

```shell
npm install iot-io
```

### Cross compilation

If you don't install gcc on Galileo or just want a much faster compilation, please prepare a host Linux machine to setup cross compiler. 

* The Galileo Arduino IDE has contained a cross compiler, please download the Linux version from https://communities.intel.com/docs/DOC-22226 to your host Linux machine

* Make sure node-gyp is installed. If not install it with npm

```shell
sudo npm install -g node-gyp
```

* Set cross compiler environment. Save below script as `set_cross_compiler.sh` and change ARDUINO_PATH to correct path

```shell
ARDUINO_PATH="$HOME/arduino-1.5.3"
SYSROOT="$ARDUINO_PATH/hardware/tools/sysroots/i586-poky-linux-uclibc"
BIN_ROOT="$ARDUINO_PATH/hardware/tools/sysroots/x86_64-pokysdk-linux/usr/bin/i586-poky-linux-uclibc/i586-poky-linux-uclibc-"
export CC="${BIN_ROOT}gcc --sysroot=$SYSROOT -m32 -march=i586"
export CXX="${BIN_ROOT}g++ --sysroot=$SYSROOT -m32 -march=i586"
export LINK=$CXX
$ARDUINO_PATH/hardware/tools/install_script.sh
```

* Then execute this script to set env.

```shell
chmod +x set_cross_compiler.sh
source set_cross_compiler.sh
```

* Now install the library with npm. By default it will be saved under ./node_modules/iot-io

```shell
npm install 
```

* Copy the whole directory to Galileo

## Quick start

We provide Arduino like APIs

* Set digital pin output and set its voltage high

```javascript
var IOLIB = require('iot-io');
var io = new IOLIB.IO({
  log: true,
});

io.pinMode(13, io.OUTPUT);
io.digitalWrite(13, io.HIGH);
```

* Turn on the led on pin 13 with friend API. Above example has done the same thing, but we want to use simpler and more direct interfaces.

```javascript
var IOLIB = require('iot-io');
var io = new IOLIB.IO({
  log: true,
});

var led = new IOLIB.Led({
  io: io,
  pin: 13
});

led.on();
```  

## APIs

Currently there are more than 100 APIs which come from the Intel Galileo Arduino SW. Please go to doc directory to know more details. These APIs are automatically generated with our tools. Please read the [API document] ( http://ilc-opensource.github.io/io-js/doc) to know more details

## License

The BSD License
