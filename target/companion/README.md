# IOT IO Library for Companion

Remotely call iot-io built-in Arduino like functions and user-defined functions. Make sure an iot-io-server is running before you use this library.

## Quick start

### Call built-in APIs

The only difference to iot-io library is to denote remote RPC server's address & port and enable rpc client. Below example *demo.js* has shown how to enable rpc request and use user defined function

```javascript
var IOLIB = (typeof require === 'function') ?
            require('iot-io-companion'): this.IOLIB;

var io = new IOLIB.IO({
  rpc: true,  // turn on rpc call
  port: 2000, // port of RPC server
  hostname: 'localhost', //address or machine name of RPC server
});

// directly use built-in Arduino functions
io.pinMode(13, io.OUTPUT);
io.digitalWrite(13, io.HIGH);

// add user-defined function in RPC server, 
io.addRpc('myFun');
// then use it as normal method
io.myFun('world'); 
```

Then IOT device which runs `iot-io-server` can receive the RPC request and execute these functions.

```shell
iot-io-server
```

### Call user defined functions

The iot-io-server can expose user defined functions. Below file extra.js can expose function *Foo* as *myFun*

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

Run server with extra.js

```shell
iot-io-server extra.js
```

In companion device you can call *myFun* by
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

## Execution environment

iot-io-companion can run in nodejs and browser. In nodejs please load it as normal module. In browser please load the file `iot-io-browser-general.js` or `iot-io-browser-general.min.js', it has contained all of dependent libraries except for jquery, so you need to load jquery before it.

```html
<script src = 'http://code.jquery.com/jquery-1.11.0.min.js'> </script>
<script src = './iot-io-browser-general.js'></script>
<script src = './led_rpc.js'></script>
```

## APIs

### Arduino like APIs
It shares almost the same APIs with `iot-io` library except for below APIs. Please read the [API document] ( http://ilc-opensource.github.io/io-js/doc) to know more details

### new IO(options)
Only list the extra options here compares to iot-io. 
* options.rpc (boolean). Set it true to enable RPC calls.
* options.port(integer, default is 2000). Port of remote iot-io-server
* options.hostname(string). The hostname or ip address of iot-io-server

### io.addRpc(funName)
Added a remote user-defined function
* funName(string). The name of user-defined function

## License

The BSD License 
