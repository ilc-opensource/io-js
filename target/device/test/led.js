
var IOLIB = (typeof require === 'function') ? require('../'): this.IOLIB;

var io = new IOLIB.IO({
  log: true,
  port: 2000,
  hostname: 'localhost',
});

/*
var led = new IOLIB.Led({
  io: io,
  pin: 13
});

led.off();
led.blink();
*/
