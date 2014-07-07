var IOLIB = require('../');
var io = new IOLIB.IO({
  'log': true,
  'emu': true,
  //'rpc': true,
  'quickInit' : false,
  'hostname': 'localhost',
  'port': 2000
});

io.digitalWrite(13, io.HIGH);
//io.rpc('abc', 1, 2);
io.addRpc('abc');
io.addRpc('hello');
io.abc(1, 2);
io.hello(1, 2);
//io.rpc('hello', 'world');
//io.hello('world');
