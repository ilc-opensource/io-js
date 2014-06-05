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
  
  "pinMode" : function() {
    var io = new IOLIB.IO(testConfig);
    io.pinMode(PIN, io.INPUT); 
    io.pinMode(PIN, io.OUTPUT); 
    assert(true);
  },

  "analogWrite " : function() {
    var io = new IOLIB.IO(testConfig);
    io.pinMode(PIN, io.OUTPUT); 
    io.analogWrite(PIN, io.HIGH);
    io.analogWrite(PIN, 0.5);
    io.analogWrite(PIN, io.LOW);
    assert(true);
  },

  "analogRead " : function() {
    var io = new IOLIB.IO(testConfig);
    io.pinMode(PIN, io.INPUT); 
    io.analogWrite(PIN);
    assert(true);
  },

});

