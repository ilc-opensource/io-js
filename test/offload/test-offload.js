if(typeof require === 'function') {
  buster = require("buster");
}
var assert = buster.assert;

var IOLIB = (typeof require === 'function') ? require('../..'): this.IOLIB;

//require('../rpc_async.js');

buster.testCase("\n" + "test offload [" + testConfig.prefix + "] -", {

  'single offload' : function() {

    testConfig.quickInit = false;
    var io = new IOLIB.IO(testConfig);
    
    io.offload(function(IOLIB, context){
      var io = new IOLIB.IO({
        emu: true,
        quickInit: false
      });
     
      io.pinMode(13, io.INPUT);
    });
    assert(true);
  },

});
