(function(exports, global) {

//////////////////////////////////////////////


  var utils = undefined;
  if(typeof require === 'function' && typeof module === 'object') { 
    utils = require('../utils.js');
  } else {
    utils = global.utils;
  }

  var Submit = function(options) {
  };

  Submit.prototype.config = function(options) {
  };

  Submit.prototype.classReq = function(className, args) {
    console.log(className + ": " + JSON.stringify(utils.toArray(args)));
    return className + " OK";
  };

  Submit.prototype.classMethodReq = function(className, methodName, args) {
    console.log(className + "." + methodName + ": " + JSON.stringify(utils.toArray(args)));
    return className + "." + methodName + " OK";
  };

  Submit.prototype.funcReq = function(funcName, args) { 
    console.log(funcName + ": " + JSON.stringify(utils.toArray(args)));
    return funcName + " OK";
  };

  exports.Submit = Submit;

//////////////////////////////////////////////

})(typeof exports === 'object'? exports: this, this );
