var GA = require('../lib/');

var io = GA.IO;

io.initWithTty(new Buffer("/dev/tty1"),
               new Buffer("/dev/tty1"),
               new Buffer("/dev/tty1"));

myservo = new io.Servo();

// attaches the servo on pin 9 to the servo object
myservo.attach(9);

setInterval(function() {
 // goes from 0 degrees to 180 degre in step of 1 degree
  for(pos = 0; pos < 180; pos += 1) {
    myservo.write(pos);
    io.delay(15);
  }

  // goes from 180 degrees to 0 degrees in step of 1 degree
  for(pos = 180; pos>=1; pos-=1) { 
    myservo.write(pos);
    io.delay(15);
  }
}, 500);
