var utils = require('./utils.js');

var rpcCounter = 0;
var objMap = {};

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
  }

};

module.exports = handleRequest;
