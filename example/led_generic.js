var GA = require('../lib/');

var io = GA.IO;

io.initWithTty("/dev/tty1", "/dev/tty1", "/dev/tty1");

var led = new GA.Led({
  io: io,
  pin: 13
});

led.blink();
