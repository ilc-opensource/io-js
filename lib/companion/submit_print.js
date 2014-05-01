(function(exports, global) {

//////////////////////////////////////////////

  var utils = undefined;
  if(typeof require === 'function' && typeof module === 'object') { 
    utils = require('./utils.js');
  } else {
    utils = global.utils;
  }

  exports.classReq = function(className, args) {
    console.log(className + ": " + JSON.stringify(utils.toArray(args)));
    return className + " OK";
  };

  exports.classMethodReq = function(className, methodName, args) {
    console.log(className + "." + methodName + ": " + JSON.stringify(utils.toArray(args)));
    return className + "." + methodName + " OK";
  };

  exports.funcReq = function(funcName, args) { 
    console.log(funcName + ": " + JSON.stringify(utils.toArray(args)));
    return funcName + " OK";
  };

//////////////////////////////////////////////

})(typeof exports === 'object'? exports: (this.submit = {}), this );
