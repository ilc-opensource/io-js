(function(exports, global) {
  exports.toArray = function(args) {
    return Array.prototype.slice.call(args, 0);
  };
//})('object' === typeof module? module: (this.utils = {}), this);
})(typeof exports === 'object'? exports: (this.utils = {}), this );
