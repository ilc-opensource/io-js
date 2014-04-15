var io = require('..');

io.initWithTty('/dev/ttyGS0', '/dev/tty', '/dev/tty');

var LED = 13;

io.pinMode(LED, 1);

while(true) {
  io.digitalWrite(LED, 1);
  io.delay(1000);
  io.digitalWrite(LED, 0);
  io.delay(1000);
}
