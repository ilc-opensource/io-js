# IOT IO Library

A unified IO Javascript library for IOT device(Galileo/Edison), companion device(phone/tablet) and XDK.

## Features

* Arduino like API
* Unified API for nodejs and browser
* Standard JSON-RPC 2.0 support
* Offload execution
* Autogen tools for customized IO functions

## Installation

npm install

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
