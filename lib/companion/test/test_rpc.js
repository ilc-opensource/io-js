var io =require('../io_rpc.js');
io.config({
  'log': true,
  'hostname': 'localhost',
  'port': 2000
});

io.digitalRead(1, 2);
io.digitalWrite(1, 2);

var servo0 =new Servo({a: 'b'});
console.log('servo0 ' + JSON.stringify(servo0));
servo0.write(1, 2);

var servo1 =new Servo({c: 'd'});
