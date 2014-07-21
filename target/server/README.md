# IOT IO RPC Server

Expose iot-io APIs and user defined functions to remote companion devices. 

## Install

```shell
sudo npm install -g iot-io-server
```

## Command line options

The files which contain user defined RPC functions can be listed in options

```shell
iot-io-server [file0, file1, ...]
```

## Expose user defined functions

User defined functions are saved in variable `RPC`. A global variable `isRpcServer` can help determine whether this file is opened by iot-io-server.

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

## Remote RPC call from companion device

The exposed functions can be called from companion device which has installed *iot-io-companion* library which supports nodejs & browser.

### Call built-in functions

After enabled `rpc`, set `hostname` and `port`, you can access built-in Arduino like APIs.
 
```javascript
var IOLIB = (typeof require === 'function') ? 
            require('iot-io-companion'): this.IOLIB;

var io = new IOLIB.IO({
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});
io.pinMode(13, io.OUTPUT);
io.digitalWrite(13, io.HIGH);
```

### User defined functions

You should call *io.addRpc* to add user-defined functions to context, then you can call it like a normal method.

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

## License

The BSD License
