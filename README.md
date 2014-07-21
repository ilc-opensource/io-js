# IOT IO Library

A unified Javascript IO library for IOT device([Galileo](http://www.intel.com/content/www/us/en/intelligent-systems/galileo/galileo-overview.html)/Edison), companion device(phone/tablet) and XDK. 

## Components

It is consisted of

* Two libraries: iot-io, iot-io-companion
* A server: iot-io-server
* An automation tool: autogen

### iot-io

A Javascript based IO library which provides Arduino like APIs. 

The target execution environment is IOT devices including Galileo and Edison

### iot-io-companion

Remotely call iot-io built-in Arduino like functions and user-defined functions. The function call will be translated to a JSON-RPC request and the iot-io-server will receive the request then call iot-io library natively. 

The target execution environment is companion devices including phone/tablet/pc/etc. This library runs in Nodejs or Browser.
 
### iot-io-server

A RPC server. It can expose iot-io APIs and user defined functions to remote companion devices. 

Basiclly the target execution environment is IOT device.

### autogen

A Python tool is used to generate the main skeleton of iot-io/iot-io-companion/iot-io-server. If user want to add more C/C++ functions to these software stack he can use it to read standard .h files then the new iot-io/iot-io-companion/iot-io-server will be generated.  

## Prebuild

If you only want to build some components, please go to the corresponding directory and read the README. 

* Please follow the document [Intel Galileo Getting Started](https://communities.intel.com/docs/DOC-22796) to install Yocto on Galileo and boot your board from a SD card

* Install node-gyp
```shell
sudo npm install -g node-gyp
```
* Install cross compiler

  - The Galileo Arduino IDE has contained a cross compiler, please download the Linux version from https://communities.intel.com/docs/DOC-22226 to your host Linux machine
 
  - Edit target/device/set_cross_compiler.sh and set `ARDUINO_PATH` to the right path
  
  - run the script to set environment values
```shell
    source target/device/set_cross_compiler.sh
```

* Optionally install uglify for compressing and mangling 
```shell
sudo npm install uglify-js
```

* Optionally install jsdoc for document generation
```shell
sudo npm install -g jsdoc
```
## Build

Build it with gmake
```shell
make
```
but make will not download all dependent nodejs modules, then we suggest you to use npm
```shell
npm install
```

## Quick Start


### Control IO with Javascript on IOT device

With iot-io you can develop the program with Javascript to control IO. The API is Arduino like and easy to understand.

For example we can turn on a LED by below file
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

We can use all of iot-io APIs as RPC(Remote Procdure call) functions with iot-io-companion. The below code can remotely turn on the LED from another PC. The only difference to above example is we must set extra options to tell where is remote RPC server. Then save below codes to file `led_rpc.js` on remote PC. 

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

On IOT device please install iot-io-server.
```shell
npm install -g iot-io-server
```

Run the RPC server on IOT device
```shell
iot-io-server
```

Back to your remote PC. Now you can run led_rpc.js and it will turn on the IOT device's LED remotely.
```shell
node led_rpc.js
```

### Run in Browser

The remote control codes can run in browser & nodejs. Because our library is based on jQuery, please load jQuery firstly. You can create a HTML file `index.html` and put it in the directory in which `led_rpc.js` is.

```html
<script src = 'http://code.jquery.com/jquery-1.11.0.min.js'> </script>
<script src = './iot-io-browser-general.js'></script>
<script src = './led_rpc.js'></script>
```

Then you can open `led.html` in browser and led will be turned on

### Pack it to Mobile APP

The above HTML page can be packed to an Android/iOS/WP/Tizen/... application with [Intel XDK](http://xdk-software.intel.com/). You can create a project in XDK and import above index.html with libraries. You can also debug the application with XDK.

### Expose user defined function

The iot-io-server can not only expose built-in APIs but also user defined functions. 

Prepare the file which contains expose candidate. Suppose it is called `extra.js`. User defined functions are saved in variable `RPC`. A global variable `isRpcServer` can help determine whether this file is opened  by iot-io-server.

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

The client side can use exposed function `myFun` in nodejs or browser.

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

Suppose user has a new function in my_print.cpp

```c
void myPrint(char *s) {
  printf("hello %s\n", s);
}
```

In my_print.h the function myPrint is declared as extern
```c
extern void myPrint(char *s);
```

Go to target/device/libio and put these two files under src, then add .cpp file to libio.gyp

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

Finally go to the root directory and rebuild all of library

```shell
cd io-js
make
```

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

## Licese

All of components use the BSD license  
