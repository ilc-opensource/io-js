var Board = require('bindings')('galileo.node');

module.exports = function(options) {
  var self = this;
  Board.IO.call(self, options);

  self.getSerialV8 = function() {
    var tmp = new self.TTYUARTClass("__instanceV8");
    tmp.getSerialV8E();
    return tmp;
  }

  self.getSerial2V8 = function() {
    var tmp = new self.TTYUARTClass("__instanceV8");
    tmp.getSerial2V8E();
    return tmp;
  }

  self.getSerial1V8 = function() {
    var tmp = new self.TTYUARTClass("__instanceV8");
    tmp.getSerial1V8E();
    return tmp;
  }

  self.setSerialV8 = function(value) {
    value.setSerialV8E();
  }

  self.setSerial2V8 = function(value) {
    value.setSerial2V8E();
  }

  self.setSerial1V8 = function(value) {
    value.setSerial1V8E();
  }

  self.setWireV8 = function(value) {
    value.setWireV8E();
  }

  self.getWireV8 = function() {
    var tmp = new self.TwoWire("__instanceV8");
    tmp.getWireV8E();
    return tmp;
  }

  self.setSpiV8 = function(value) {
    value.setSpiV8E();
  }

  self.getSpiV8 = function() {
    var tmp = new self.SPIClass("__instanceV8");
    tmp.getSpiV8E();
    return tmp;
  }

}
