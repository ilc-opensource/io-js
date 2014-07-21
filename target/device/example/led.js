
var IOLIB = require('../');

var io = new IOLIB.IO({
  log: true,
});

var led = new IOLIB.Led({
  io: io,
  pin: 13
});

led.off();
led.on();
