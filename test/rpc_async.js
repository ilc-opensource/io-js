(function(exports, global) {

  if(typeof require === 'function') {
    require('./config.js');
    testConfig.prefix = 'node-rpc-async';
  } else {
    testConfig.prefix = 'browser-rpc-async';
  }

  console.log(JSON.stringify(testConfig));
  testConfig.rpc         = true;
  testConfig.crossDomain = true;
  testConfig.async       = true;

  exports.testConfig = testConfig;

})(typeof exports === 'object'? global: this, this);
