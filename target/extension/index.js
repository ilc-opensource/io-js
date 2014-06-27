(function(exports, global) {

var Extension;

if(typeof require === 'function') {

  Extension = {
    Led: require('./led.js').Led,
  };
} else {
  Extension = {
    Led: global.Led,
  };
}

exports.Extension = Extension;

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB);
