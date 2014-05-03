(function(exports, global) {
  exports.toArray = function(args) {
    return Array.prototype.slice.call(args, 0);
  };

  exports.generateId = function() {
    return Math.round(Math.random() * Math.pow(2, 24));
  };

  exports.log = console.log;

//})('object' === typeof module? module: (this.utils = {}), this);
})(typeof exports === 'object'? exports: (this.utils = {}), this );
