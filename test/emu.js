(function(exports, global) {

  if(typeof require === 'function') {
    require('./config.js');
    testConfig.prefix = 'node-emu';
  } else {
    testConfig.prefix = 'browser-emu';
  }

  testConfig.emu = true;

  exports.testConfig = testConfig;

})(typeof exports === 'object'? global: this, this);
