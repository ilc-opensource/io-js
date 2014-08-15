var IOLIB = (typeof require === 'function') ? require('../'): this.IOLIB;

var io = new IOLIB.IO({
  log: true,
  rpc: true,  // turn on rpc call
  port: 2000, // port of RPC server
  hostname: 'hostname', //address or machine name of RPC server
});

var led = new IOLIB.Led({
  io: io, 
  pin: 13
});

led.off();
led.blink(100);
