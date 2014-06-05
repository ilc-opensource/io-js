(function(exports, global) {

  if(typeof require === 'function') {
    require('./config.js');
    testConfig.prefix = 'node-native';
  } else {
    throw "browser doesn't support native mode";
  }

  exports.testConfig = testConfig;

})(typeof exports === 'object'? global: this, this);
