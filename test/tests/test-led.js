// Node.js tests
if(typeof require === 'function') {
  buster = require("buster");
}

console.log(JSON.stringify(testConfig));
var assert = buster.assert;

var IOLIB = (typeof require === 'function') ? require('../..'): this.IOLIB;

var PIN = 13;
buster.testCase("\n" + "test Led [" + testConfig.prefix + "] -", {
  "init led": function() {
    var io = new IOLIB.IO(testConfig);
    var led = new IOLIB.Led({
      io: io,
      pin: PIN
    });
    assert(true);
  },
  
  "led on" : function() {
    var io = new IOLIB.IO(testConfig);
    var led = new IOLIB.Led({
      io: io,
      pin: PIN
    });
    led.on();
    assert(true);
  },

  "led off" : function() {
    var io = new IOLIB.IO(testConfig);
    var led = new IOLIB.Led({
      io: io,
      pin: PIN
    });
    led.off();
    assert(true);
  },


});

