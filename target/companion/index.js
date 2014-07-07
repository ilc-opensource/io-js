(function(exports, global) {

/**
  @class IO
  @param {Object} options 
  @param {Boolean} [options.log=false] - dump log
  @param {Boolean} [options.quickInit=true] - quickly init galileo IO
  @param {Boolean} [options.emu=false] - Run in emulation mode
  @param {Boolean} [options.fake=false] - alias of options.emu
  @param {Boolean} [options.rpc=false] - enable RPC client
  @param {String}  [options.hostname=undefined] - remote RPC server's IP address
  @param {Integer} [options.port=undefined] - remote RPC server's port
 
 */
exports.IO =  function(config) {

  var self = this;

  //Initialize default configu
  config.log = config.log || false;
  if(config.quickInit == undefined)
    config.quickInit = true;

  if(!(config.emu || config.fake || config.rpc))
    throw "only support emu/fake/rpc mode";

  var Board = (typeof require === 'function')? 
                require(__dirname + '/lib/board/galileo.js').Board
              : global.Board;
  var Submit;
  if(config.emu || config.fake) {
    Submit = (typeof require === 'function')? 
               require(__dirname + '/lib/submit/print.js').SubmitPrint
             : global.SubmitPrint;
  } else if(config.rpc) { 
    Submit = (typeof require === 'function')? 
               require(__dirname + '/lib/submit/rpc.js').SubmitRpc
             : global.SubmitRpc;
    config.url = 'http://' + config.hostname + ':' + config.port;     
  }

  var submit = new Submit(config);
  
  Board.call(self, {'submit': submit});   

  self.config(config);

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


  // add special interfaces for rpc  
  if(config.rpc) {

    /**
     @function IO.offload
     @type Function
     @param {Function} func - the function will be offloaded to remote
     @param {Object} config - configuration
     @param {Function} callback - the callback function for return value
     @desc offload a function to remote server. 
     */
    self.offload = function(func, config, callback) {
      self.submit.offloadReq(func, config, callback);
    };

    /**
     @function IO.offloadClear
     @desc clear all of offloaded function
     */
    self.offloadClear = function() {
      var callback = undefined;
      var config = null;

      if(arguments.length == 1) {
        var arg = arguments[0];
        if(typeof arg === 'object') 
          config = arg;
        else if (typeof arg === 'function')
          callback = arg
      } else if(arguments.length > 1) {
        config = arguments[0];
        callback = arguments[1];
      }
 
      self.submit.offloadClear(config, callback);
    };

    /**
     @function IO.offloadQuery
     @desc query the data saved in the remote context
     @param {Object} options - configuration
     @param {Function} [callback] - callback functions for queried value
     */
    self.offloadQuery = function() {
      var callback = undefined;
      var config = null;

      if(arguments.length == 1) {
        var arg = arguments[0];
        if(typeof arg === 'object') 
          config = arg;
        else if (typeof arg === 'function')
          callback = arg
      } else if(arguments.length > 1) {
        config = arguments[0];
        callback = arguments[1];
      }
      self.submit.offloadQuery(config, callback);
    };

    /**
     @function IO.addRpc
     @desc add extra customized RPC function
     @param {String} funcName - function name
     */
    self.addRpc = function(funcName) {
      self[funcName] = function(){
        self.submit.rpc(arguments, funcName);
      };
    };

    /**
     @function IO.rpc
     @desc call customized RPC function
     @param {String} funcName - function name
     @param {...*} arg - function arguments
     */
    self.rpc = function() {
      self.submit.rpc(arguments);
    };
  } else {
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

  }
 
};

// Merge high level APIs into this interface
var extension = null;
if(typeof require === 'function') {
  var fs = require('fs');
  if(fs.existsSync(__dirname + '/../extension'))
    extension = require(__dirname + '/../extension').Extension;
  else if(fs.existsSync(__dirname + '/extension'))
    extension = require(__dirname + '/extension').Extension;   
} else {
  extension = global.Extension;
}

if(extension) {
  var idx;
  for (idx in extension)
    exports[idx] = extension[idx];    
}

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB );
