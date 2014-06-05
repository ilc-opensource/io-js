var jayson  = require('../../lib/jayson');
var Board   = require(__dirname + '/lib/board/galileo.js');
var handle  = require(__dirname + '/lib/handleRpc.js');
var IOLIB   = require(__dirname + '/../');

var io  = new IOLIB.IO({
  emu: true,
  quickInit: false,
  log: true,
});

var board = new Board({
  io: io,
  handle: handle
});

board.map['offload'] = function() {
  board.handle.offloadReq(arguments);
};

board.map['offloadClear'] = function() {
  board.handle.offloadClear(arguments);
};

board.map['offloadQuery'] = function() {
  board.handle.offloadQuery(arguments);
};
 
var server = jayson.server(board.map);

var PORT = 2000;
server.http().listen(PORT);

console.log('Listening ' + PORT + '...');
