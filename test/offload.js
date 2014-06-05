
var IOLIB = (typeof require === 'function') ? require('../..'): this.IOLIB;

var io = new IOLIB.IO({
  //emu: true,  
  //log: true,
  rpc: true,
  port: 2000,
  hostname: 'localhost',
});

io.offload(function(IOLIB, context) { 
  var io = new IOLIB.IO({
    emu: true
  });

  io.pinMode(13, io.INPUT);
  console.log('hello');
  context.save = 1;
  return 3;
});

io.offload(function(IOLIB, context) { 
  context.save++;
}, {emu: true});

io.offloadQuery(function(error, response){
  console.log('query -> ' + JSON.stringify(error) + ' : ' + JSON.stringify(response));
} );

io.offloadClear(function(error, response) {
  console.log('offloadclear: ' + JSON.stringify(error) + ' : ' + JSON.stringify(response));
});

io.offloadQuery({}, function( error, response){
  console.log('error query -> ' + JSON.stringify(error) + ' : ' + JSON.stringify(response));
});

