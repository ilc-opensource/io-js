
var IOLIB = (typeof require === 'function') ? require('..'): this.IOLIB;

var io = new IOLIB.IO({
  log: true,
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});

io.offload(function(IOLIB, context) { 
  var io = new IOLIB.IO({
    emu: true,
    log: true
  });
  var led = new IOLIB.Led({
    io: io,
    pin: 13
  });
  
  led.off();

  context.save = 1;  
  return true;
});

io.offload(function(IOLIB, context) { 
  var io = new IOLIB.IO({
    //emu: true
    log: true,
    quickInit: false
  });
  var led = new IOLIB.Led({
    io: io,
    pin: 13
  });
  
  led.on();

  context.save++;  
  return true;
});

io.offloadQuery(function(error, response) {
  console.log(JSON.stringify(response));
});

