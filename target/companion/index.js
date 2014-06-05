
(function(exports, global) {

exports.Companion =  function(config) {

  var self = this;

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

  if(config.rpc) {

    self.offload = function(func, config, callback) {
      self.submit.offloadReq(func, config, callback);
    };

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

  }
 
};

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB );
