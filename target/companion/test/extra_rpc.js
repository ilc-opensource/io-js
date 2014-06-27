var IOLIB = require('../');
var io = new IOLIB.IO({
  'log': true,
  'rpc': true,
  'hostname': 'localhost',
  'port': 2000
});

io.digitalWrite(13, io.HIGH);
//io.rpc('test0', 1, 2);
