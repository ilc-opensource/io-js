var jayson = require('jayson');
var Methods = require(__dirname + '/lib/board/galileo.js');
var handle = require(__dirname + '/lib/handleRpc.js');
var io = require(__dirname + '/../companion/io_fake.js');
//var io = new require(__dirname + '../device');

var methods = new Methods({
  io: io,
  handle: handle
});
 
var server = jayson.server(methods.map);

server.http().listen(2000);
