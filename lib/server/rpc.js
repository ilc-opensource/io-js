var jayson = require('jayson');
var Methods = require('./lib/board/galileo.js');
var methods = new Methods({
  ioPath: __dirname + '/../companion/io_fake.js', 
  handleReqPath: __dirname + '/lib/handleRpc.js'
});
 
var server = jayson.server(methods.map);

server.http().listen(2000);
