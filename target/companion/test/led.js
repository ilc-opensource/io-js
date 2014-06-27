
var IOLIB = (typeof require === 'function') ? require('../'): this.IOLIB;

var io = new IOLIB.IO({
  emu: true,  
  log: true,
  //rpc: true,
  port: 2000,
  hostname: 'localhost',
});

io.digitalWrite(13, io.HIGH);
io.digitalWrite(13, io.LOW);

var led = new IOLIB.Led({
  io: io,
  pin: 13
});

