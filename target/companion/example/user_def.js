var IOLIB = (typeof require === 'function') ?
            require('iot-io-companion'): this.IOLIB;

var io = new IOLIB.IO({
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});

io.addRpc('myFun');

myFun('world'); //will output 'hello world'

