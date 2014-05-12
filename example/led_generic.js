var GA = require('../lib/');

var io = GA.IO;

io.initWithTty(new Buffer("/dev/tty1"),
               new Buffer("/dev/tty1"),
               new Buffer("/dev/tty1"));

var led = new GA.Led({
  io: io,
  pin: 13
});

led.blink();
