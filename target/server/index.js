#!/usr/bin/env node

var jayson  = require(__dirname + '/lib/jayson');
var Board   = require(__dirname + '/lib/board/galileo.js');
var handle  = require(__dirname + '/lib/handleRpc.js');
var fs      = require('fs');

var IOLIB;

if(fs.existsSync(__dirname + '/../index.js'))
  IOLIB = require(__dirname + '/../');
else
  IOLIB = require('iot-io');

isRpcServer = true;

var io  = new IOLIB.IO({
  //emu: true,
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

board.extraMap = {};

if(process.argv.length > 2) {
  for(var idx = 2; idx < process.argv.length; idx++) {
    var f = process.argv[idx];
    var rel = process.cwd() + '/' + f;
   
    if(fs.existsSync(rel)) {
      f = rel;
    } else if(fs.existsSync(f)) {
    } else {
      console.log('discard ' + f);
      continue;
    }

    console.log('=> ' + f); 
    var extra = require(f);
    if(!extra.RPC){
      console.log('  no rpc functions');
      continue;
    }

    for(var m in extra.RPC) {
      console.log('  + ' + m);
      board.extraMap[m] = extra.RPC[m];
    }
  }
}

board.map['rpc'] = function() {
  board.handle.rpc(board.extraMap, arguments);
};
 
var server = jayson.server(board.map);

var PORT = 2000;
server.http().listen(PORT);

console.log('Listening ' + PORT + '...');
