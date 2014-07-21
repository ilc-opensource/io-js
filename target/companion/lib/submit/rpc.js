(function(exports, global) {

  var utils = undefined;
  var jayClient = undefined;

  var Submit = function(options) {
  }

  var defaultCallback = function(error, response) {
    console.log(JSON.stringify(response));
  };

  var getCallback = function(args) {
    if(typeof args[args.length -1] == 'function')
      return args.pop();
    else
      return defaultCallback;
  }

  Submit.prototype.config = function(options) {

    var self = this;	  
    if(typeof require === 'function' && typeof module === 'object') {
      jayson = require('../lib/jayson');
      utils = require('../utils.js');
      jayClient = jayson.client.http(options);
    } else {
      utils = global.utils;
      var jayson = new window.Jayson(options);

      jayClient = {
        'request': function(method, params, callback) {
          return jayson.request(method, params, undefined, callback);
        }        
      }
    }

    self.id = utils.generateId();

    if(!options.log)
      utils.log = function(){};

    utils.log('config with ' + JSON.stringify(options));
    
  };

  Submit.prototype.offloadReq = function(offloadFunc, config, cb) {
    var callback = cb;
    if(cb === undefined)
      callback = defaultCallback;
    
    args = [offloadFunc.toString(), config, this.id];
    //args.push(config);
    //args.push(this.id); 
    utils.log('offload ' + JSON.stringify(args)); 
    jayClient.request('offload', args, function(error, response) {
      callback(error, response);
    });
  };

  Submit.prototype.offloadClear = function(config, cb) {
    var callback = cb;
    if(cb === undefined)
      callback = defaultCallback;
    
    var args = [config, this.id];
    
    utils.log('offloadClear ' + JSON.stringify(args));

    jayClient.request('offloadClear', args, function(error, response) {
      callback(error, response);
    });
   
  };

  Submit.prototype.offloadQuery = function(config, cb) {
    var callback = cb;
    if(cb === undefined)
      callback = defaultCallback;

    var args = [config, this.id];

    jayClient.request('offloadQuery', args, function(error, response) {
      callback(error, response);
    });

  };

  Submit.prototype.classReq = function(className, args, self) {

    var callback = getCallback(args);
    args = utils.toArray(args); 

    self.rpcid = utils.generateId();

    args.push(self.rpcid);

    utils.log('classReq ' + className + '(' + JSON.stringify(args) + ')');

    jayClient.request(className, args, function(error, response) {
      callback(error, response);
      ret = response;
    });

  };


  Submit.prototype.classMethodReq = function(className, methodName, args, self) {

    args = utils.toArray(args);

    // attach rpcid
    args.push(self.rpcid);

    var callback = getCallback(args);
    var ret = undefined;

    utils.log('classMethodReq ' + className + '.' + methodName + '(' + JSON.stringify(args) + ')');

    jayClient.request(className + '.' + methodName, utils.toArray(args), function(error, response) {
      callback(error,response);
      ret = response;
    });
        
    return ret;
  };


  Submit.prototype.funcReq = function(funcName, args) {

    args = utils.toArray(args);
    var callback = getCallback(args);
    var ret = undefined;

    utils.log('funcReq ' + funcName + '(' + JSON.stringify(args) + ')');
    jayClient.request(funcName, utils.toArray(args), function(error,response) {
      ret = response;
      callback(error, response);
    });

    return ret;
  };


  Submit.prototype.rpc = function(args, funcName) {

    args = utils.toArray(args);
    var callback = getCallback(args);
    var ret = undefined;
    
    if(funcName !== undefined) {
      args.unshift(funcName);
    }

    utils.log('rpc: ' + JSON.stringify(args));
   
    jayClient.request('rpc', args, function(error,response) {
      ret = response;
      callback(error, response);
    });
  };
/*
  Submit.prototype.funcReq = function(funcName, args) {
    args = utils.toArray(args);
    var callback = getCallback(args);

    var asyncChain = $.whenSync(function(deferred) {
      jayClient.request(funcName, utils.toArray(args), function(error, response){
        callback(error, response); 
        deferred.resolve(response);
      });
    });

    asyncChain.done(function(result){
      console.log('done: ' + JSON.stringify(result)); 
    });

  };
*/
  exports.SubmitRpc = Submit;

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB);
