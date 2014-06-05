(function(exports, global) {

  if(typeof require === 'function') {
    require('./config.js');
    testConfig.prefix = 'node-rpc-sync';
  } else {
    testConfig.prefix = 'browser-rpc-sync';
  }

  console.log(JSON.stringify(testConfig));
  testConfig.rpc         = true;
  testConfig.crossDomain = true;
  testConfig.async       = false;

  exports.testConfig = testConfig;

})(typeof exports === 'object'? global: this, this);
