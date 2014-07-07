var utils = require('./utils.js');

var rpcCounter = 0;
var objMap = {};
var offloadMap = {};

toArray = function(args) {
  var ret = Array.prototype.slice.call(args, 0);
  return ret;
}

function construct(constructor, args) {
    function F() {
        return constructor.apply(this, args);
    }
    F.prototype = constructor.prototype;
    return new F();
}

var handleRequest = {

  'funcReq': function(func, inputArgs, funcName) {

    var args = toArray(inputArgs); 
    var callback = args.pop();
    
    utils.log(funcName + ': ' + JSON.stringify(args));

    var ret = func.apply(func, args);
    callback(null, ret);
  },

  'classReq' : function(func, inputArgs, className) {

    var args = toArray(inputArgs); 

    var callback = args.pop();
    utils.log('new ' + className + '(' + JSON.stringify(args) + ')');

    var rpcid = args.pop();
    var obj = construct(func, args);
    //var obj = new func();
    obj.rpcid = rpcid;
    objMap[rpcid] = obj;
    utils.log('update objMap with rpcid: ' + rpcid);    
    callback(null, {'rpcid': rpcid});
  },

  'classMethodReq' : function(inputArgs, className, methodName) { 

    var args = toArray(inputArgs); 

    var callback = args.pop();
    utils.log( className + '.' + methodName + '(' + JSON.stringify(args) + ')');
    //utils.log('use objMap' + JSON.stringify(objMap));    

    var rpcid = args.pop();
    utils.log('get obj with rpcid: ' + rpcid);
    var obj = objMap[rpcid];

    
    var ret = obj[methodName].apply( args);
    
    callback(null, ret);
  },

  'offloadReq' : function(inputArgs) {

    var args = toArray(inputArgs);

    var callback = args.pop();

    utils.log('offload: ' + JSON.stringify(args));

    var rpcid = args.pop();

    var ctx = {};
    var func = eval('(' + args[0] + ')');
    var config = {};
    
    if(args.length > 1) {
      config = args[1];
    }
   
    if( offloadMap[rpcid] === undefined) {
      ctx.iolib = require('../..');
      ctx.context = {};
      offloadMap[rpcid] = ctx;
    } else {
      ctx = offloadMap[rpcid];
    }

    utils.log('offload with rpcid: ' + rpcid + ' context:' + JSON.stringify(ctx.context));

    var ret = func(ctx.iolib, ctx.context);    
    callback(null, ret); 
  },
  
  'offloadClear' : function(inputArgs) {
    var args = toArray(inputArgs);

    var callback = args.pop();

    utils.log('offloadClear: ' + JSON.stringify(args));

    var id = args.pop();

    offloadMap[id] = undefined;

    callback(null, true);
  },

  'offloadQuery' : function(inputArgs) {
    var args = toArray(inputArgs);
    
    utils.log('offloadQuery: ' + JSON.stringify(args));

    var callback = args.pop();
    var id = args.pop();

    var ctx = offloadMap[id];

    if(ctx === undefined) {
      utils.log('no record for id ' + id);
      callback(utils.genErr('offload', 'no context' , null));
    } else {
      callback(null, ctx);
    }
  },

  'rpc' : function(extraMap, args) {
    args = toArray(args);
    var callback = args.pop();
    var funcName = args.shift();
    utils.log(funcName + '(' + JSON.stringify(args) + ')');
   
    var ret;
    if(!extraMap[funcName]) 
      callback(utils.genErr(funcName, 'no such function', null));

    ret = extraMap[funcName].apply(undefined, args);
 
    callback(null, ret);
  }, 

};

module.exports = handleRequest;
