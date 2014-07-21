var IOLIB = require('..');
var io = new IOLIB.IO({
  log: true,
});

io.pinMode(13, io.OUTPUT);
io.digitalWrite(13, io.HIGH);

