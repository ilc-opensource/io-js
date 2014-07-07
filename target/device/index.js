var Board = require('./globalClassVarSetterGetter');

var IO = function(config) {

 var self = this;

  //Initialize default configu
  config.log = config.log || false;
  if(config.quickInit == undefined)
    config.quickInit = true;
  
  self.config = function(options) {
  };

  if(config.emu || config.fake || config.rpc)   
    throw "only support native mode, don't set emu/fake/rpc";


  Board.call(self, config);

  // initializee ttys, it will effect serial.write/read
  var ttys = [];
  if(config.tty != undefined) {
    ttys[0] = config.tty;
    ttys[1] = config.tty;
    ttys[2] = config.tty;
  } else {
    ttys = ["/dev/tty", "/dev/tty", "/dev/tty"];
  }
  
  if(config.quickInit) {
    self.initWithTty.apply(self, ttys);
  }

  var unsupport = function() {
    console.log('Unsupport function ');
  };

  self.offload = unsupport;
  self.offloadClear = unsupport;
  self.offloadQuery = unsupport;
  self.rpc = unsupport;
  self.addRpc = function(funcName) {
    self[funcName] = function() {
      console.log('Unsupport ' + funcName);
    }
  };

};

// Merge high level APIs into this interface
var extension = null;
var fs = require('fs');
if(fs.existsSync('../extension'))
  extension = require('../extension').Extension;
else if(fs.existsSync('./extension'))
  extension = require('./extension').Extension;

if(extension) {
  var idx;
  for (idx in extension)
    exports[idx] = extension[idx];
}

exports.IO = IO; 
