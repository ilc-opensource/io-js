# IOT IO Library

A unified IO Javascript library for IOT device(Galileo/Edison), companion device(phone/tablet) and XDK.

## Features

* Arduino like API
* Unified API for nodejs and browser
* Standard JSON-RPC 2.0 support
* Offload execution
* Autogen tools for customized IO functions

## PreInstall
* This library can run correctly both on Intel dev kit https://software.intel.com/en-us/iotdevkit which contains host a machine running DevKit Live USB image and target Intel Galileo platform. This IO library can run on both of them. Below is a quick guide of how to enable nodejs on host and target. 

### Install yocoto on galileo

* [Download SD card image (200M)](http://iotdk.intel.com/images/iot-devkit-201402201605-mmcblkp0.direct.bz2)

* Uncompress image & recover image to micro sd card with `dd` cmd
```bash
dd if=/path/to/image  of=/sd/dev/path bs=1M
```
* insert SD card to galileo, then power on galileo 

* ssh login
```bash
ssh root@ip_address_for_galileo
```

* check node/node-gyp/npm
  - If not in $PATH, please find it under root directory, then create  symbol link for it. for example,
```bash
ln -s /usr/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js /usr/bin/node-gyp
```

* Make sure Galileo system is set correctly.

* copy io-js to galileo, then you can jump to `Installation` section. But the installation is very slow on Galileo. You may want to compile the library on host machine with cross compiler

### Install devkit live image on host machine

* Download iot dev kit image (4.2G)
  - [devkit-live-img-final.binblob.bz2](https://software.intel.com/sites/landingpage/iotdk/devkit-live-img-final.binblob.bz2)

* Although devkit officially suggest to use it as bootable USB key, but we suggest you to boot it in virtual machine.

* Download & Install Virtual box
  - [Refer to virtual box official website](https://www.virtualbox.org/wiki/Downloads)
* uncompress image & convert image to virtual box image
```bash
vboxmanage convertfromraw --format VMDK devkit-live-img-final.binblob ~/devkit.vmdk
```
* Boot up devkit.vmdk in virtual box

* login virtual machine

* check node/node-gyp/npm
  - If not under $PATH, please find it under root directory, then create  symbol link for it. for example,
```bash
  ln -s /opt/iot-devkit/1.5.1/yocto/sysroots/i586-poky-linux/usr/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js /usr/bin/node-gyp
```
* copy io-js to devkit, then run it followed `Installation` part. 

## Installation

  npm install
  (if run `io-js` as root, please use "npm install -unsafe-perm" instead)
  
## Examples

* Native IO operation on IOT device

```javascript
var IOLIB = (typeof require === 'function') ? require('../'): this.IOLIB;

var io = new IOLIB.IO({
  log: true
});

var led = new IOLIB.Led({
  io: io,
  pin: 13
});

led.blink();

```

* RPC client which submits the IO request to IOT device. 

Only needs to add RPC options to IO constructor. The code works in nodejs or browser. 

```javascript
var io = new IOLIB.IO({
  log: true,
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});

```

* Offload execution

The client can offload functions to remote server.

```javascript
var IOLIB = (typeof require === 'function') ? require('..'): this.IOLIB;

var io = new IOLIB.IO({
  log: true,
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});

io.offload(function(IOLIB, context) {
  var io = new IOLIB.IO({
    emu: true,
    log: true
  });
  var led = new IOLIB.Led({
    io: io,
    pin: 13
  });

  led.off();

  context.save = 1;
  return true;
});

io.offloadQuery(function(error, response) {
  console.log(JSON.stringify(response));
});
```

## Test

We choose Buster.js to run tests in Nodejs and browser

Install buster.js

```bash
npm install -g buster
```

Run test
```bash
make test
```

## Arduino Library

Go to target/device/libio

## License

BSD

/*
Copyright (c) <2014>, Intel Corporation

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of Intel Corporation nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
