# IOT IO Library

A unified Javascript IO library for IOT device([Galileo](http://www.intel.com/content/www/us/en/intelligent-systems/galileo/galileo-overview.html)/Edison), companion device(phone/tablet) and XDK. 

## Components

* Two libraries: iot-io, iot-io-companion
* A server: iot-io-server
* An automation tool: autogen

### iot-io

A Javascript based IO library which provides Arduino like APIs. 

The target execution environment is IOT devices including Galileo and Edison

### iot-io-companion

Remotely call iot-io built-in Arduino like functions and user-defined functions. The function call will be translated to a JSON-RPC request and the iot-io-server will receive the request then call iot-io library natively. 

The target execution environment is companion devices including phone/tablet/pc/etc. This library can run in Nodejs or browser.
 
### iot-io-server

A [JSON-RPC]( http://json-rpc.org/) server can expose iot-io's [Arduino like APIs](http://ilc-opensource.github.io/io-js/doc) and even user defined functions to remote companion devices.

Basically its target execution environment is IOT device.

### autogen

It is a Python tool. Its input is standard C header file and its output is the main skeleton of iot-io/iot-io-companion/iot-io-server. When user wants to add C/C++ functions as new interfaces to io-js software stack he doesn't need to learn any C to JS binding. This tool can help this javascript library adapt to the changes of C/C++ library. 

## Prebuild

If you only want to build some of components, please go to the corresponding directory and read the README. Below instruction is about how to build the whole software stack.

* Please follow the document [Intel Galileo Getting Started](https://communities.intel.com/docs/DOC-22796) to install Yocto on Galileo and boot your board from a SD card

* Because SD card image does not contain development tools such as gcc, g++ etc, then we have to do cross build. Then please prepare a Linux machine and install below tools. 

* Install [node-gyp](https://github.com/TooTallNate/node-gyp). Please notice node-gyp will detect the version of local nodejs and automatically download some header files and libraries for compilation. Then please make sure the version of nodejs on host machine is the same as which of nodejs on Galileo. If you do not want to the keep the nodejs version. You can manually open target/device/Makefile and added the version of target nodejs on Galileo.

```makefile
rebuild:
    node-gyp rebuild --arch=ia32 --target=0.x.x

configure:
    node-gyp configure  --arch=ia32 --target=0.x.x
```
* Install cross compiler

  - The Galileo Arduino IDE has contained a cross compiler, please download the Linux version from https://communities.intel.com/docs/DOC-22226 to your host Linux machine
 
  - Edit target/device/set_cross_compiler.sh and set `ARDUINO_PATH` to the right path
  
  - run the script to set environment values
```shell
source target/device/set_cross_compiler.sh
```

* Optionally install uglify for Javascript library compressing and mangling
```shell
sudo npm install -g uglify-js
```

* Optionally install jsdoc for document generation
```shell
sudo npm install -g jsdoc
```
## Build

Build with npm and install dependent libraries
```shell
npm install
```

## Quick Start


### Control IO with Javascript on IOT device

With iot-io library programmer can develop the program with Javascript to control IO. The API is Arduino like and easy to understand.

For example we can turn on a LED on digital pin 13 with below file
```javascript
var IOLIB = require('iot-io');
var io = new IOLIB.IO({
  log: true
});

io.pinMode(13, io.OUTPUT);
io.digitalWrite(13, io.HIGH);
```

Or you can use high level APIs which have hidden some hardware details. For above example, you can use API of `Led`
```javascript
var IOLIB = require('iot-io');
var io = new IOLIB.IO({
  log: true
});

var led = new IOLIB.Led({
  io: io,
  pin: 13
});

led.on();
```

### Remote IO Control 

We can use all of iot-io APIs as RPC(Remote Procdure call) functions with iot-io-companion. The below code can remotely turn on the LED from another machine. The only difference to above example is we must set extra options to tell where remote RPC server is. Please save below codes to file `led_rpc.js` on remote PC. The first line is to make sure this library can be loaded in nodejs and browser.

```javascript
var IOLIB = (typeof require === 'function') ?
            require('iot-io-companion'): this.IOLIB;

var io = new IOLIB.IO({
  log: true,
  rpc: true,  // turn on rpc call
  port: 2000, // port of RPC server
  hostname: '192.168.2.11', //address or machine name of RPC server
});

var led = new IOLIB.Led({
  io: io,
  pin: 13
});

led.on();
```

On IOT device please install and run iot-io-server to expose built-in APIs
```shell
npm install -g iot-io-server
iot-io-server
```

Back to your remote machine and run led_rpc.js to turn on the LED on IOT device.
```shell
node led_rpc.js
```

### Run in Browser

The remote control codes can run in browser & nodejs. Because iot-io-companion library for browser is based on jQuery please load jQuery firstly. You can create a HTML file `led_rpc.html` and put it in the directory in which `led_rpc.js` is.

```html
<script src='http://code.jquery.com/jquery-1.11.0.min.js'> </script>
<script src='./iot-io-browser-general.js'></script>
<script src='./led_rpc.js'></script>
```

Then you can open `led_rpc.html` in browser and LED on IOT device will be turned on

### Pack it to mobile APP

The above HTML page can be packed to an Android/iOS/WP/Tizen/... application with [Intel XDK](http://xdk-software.intel.com/). You can create a project in XDK and import above index.html with libraries. You can also debug the application with XDK.

### Expose user defined function

The iot-io-server can expose not only built-in APIs but also user defined functions. 

Prepare the file which contains expose candidate. User defined functions are saved in global variable expose's member: `RPC`. A global variable `isRpcServer` can help determine whether this file is opened by iot-io-server.

```javascript
var Foo = function(s) {
  console.log('hello ' + s);
};

if(isRpcServer) {
  exports.RPC = {
    'myFun': Foo
  };
}
```

Load it with `iot-io-server`
```shell
iot-io-server extra.js
```

The client side can use exposed function `myFun` in nodejs or browser after called `io.addRpc`.

```javascript
var IOLIB = (typeof require === 'function') ? 
            require('iot-io-companion'): this.IOLIB;

var io = new IOLIB.IO({
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});

io.addRpc('myFun');

myFun('world'); //will output 'hello world'
```

### Add C/C++ function with autogen

With autogen tool programmer can easily translate C/C++ function to Javascript functions. Suppose user has a new function `myPrint` in my_print.cpp

```c
void myPrint(char *s) {
  printf("hello %s\n", s);
}
```

In my_print.h the function myPrint is declared as extern
```c
extern void myPrint(char *s);
```

Go to target/device/libio and put these two files under directory src, then add .cpp file to libio.gyp

```javascript
      'extra_srcs' : [
        '<(extra_dir)/my_print.cpp',
      ],

```

add .h file to export.gyp

```javascript
      'export_headers' : [
        '<(extra_dir)/my_print.h',
      ],
```

Finally go to the root directory and rebuild the whole software stack

```shell
cd io-js
make
```
## Arduino like APIs

Currently there are more than 100 APIs which are translated from the [Intel Galileo Arduino SW]( https://communities.intel.com/docs/DOC-22226) with autogen tool. Please read the [API document] (http://ilc-opensource.github.io/io-js/doc) to know more details

## Test

* Test functionality with [buster.js](http://busterjs.org/)

```shell
make test
```

* Test autogen parser

```shell
./test_autogen
```

## Directories

| Directory            | Description |
|:---------------------|:------------|
| /target/device       | iot-io |
| /target/device/libio | Arduino library |
| /target/companion    | iot-io-companion |
| /target/server       | iot-io-server |
| /target/extension    | high level APIs for iot-io & iot-io-companion |
| /util/autogen        | autogen tool |
| /doc                 |documents. This directory will be created by jsdoc |

## License

All of components use the BSD license  
