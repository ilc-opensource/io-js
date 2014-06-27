(function(exports, global) {

exports.IO = function(config) {
  var self = this;
  var target;
  if(config.emu || config.fake || config.rpc) {
    target = (typeof require === 'function')?
                require('./companion')
              : exports;
  } else {
    target = (typeof require === 'function')?
                require('./device')
              : exports;
  }


  target.IO.call(self, config);

};

// Merge high level APIs into this interface
var extension = null;
if(typeof require === 'function') {
  var fs = require('fs');
  if(fs.existsSync(__dirname + '/extension'))
    extension = require(__dirname + '/extension').Extension;
} else {
  extension = global.Extension;
}

if(extension) {
  var idx;
  for (idx in extension)
    exports[idx] = extension[idx];
}


})(typeof exports === 'object'? module.exports: this.IOLIB, this.IOLIB);
