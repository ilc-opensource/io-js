// Node.js tests
if(typeof require === 'function') {
  buster = require("buster");
}

var assert = buster.assert;

var IOLIB = (typeof require === 'function') ? require('../..'): this.IOLIB;

var PIN = testConfig.pin;

buster.testCase("\n" + "test Digital [" + testConfig.prefix + "] -", {
  "init io": function() {
    var io = new IOLIB.IO(testConfig);
    assert(true);
  },
  
  "pin mode" : function() {
    var io = new IOLIB.IO(testConfig);
    io.pinMode(PIN, io.INPUT); 
    io.pinMode(PIN, io.OUTPUT); 
    assert(true);
  },

  "digitalWrite " : function() {
    var io = new IOLIB.IO(testConfig);
    io.pinMode(PIN, io.OUTPUT); 
    io.digitalWrite(PIN, io.HIGH);
    io.digitalWrite(PIN, io.LOW);
    assert(true);
  },

  "digitalRead " : function() {
    var io = new IOLIB.IO(testConfig);
    io.pinMode(PIN, io.INPUT); 
    io.digitalWrite(PIN);
    assert(true);
  },

});

