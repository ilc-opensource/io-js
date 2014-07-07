var Board = require('bindings')('galileo.node');

module.exports = function(options) {
  var self = this;
  Board.IO.call(self, options);

  /**
   @function IO#getSerialV8
   @type Function
   @returns global variable 'Serial' value
   @instance
   */
  self.getSerialV8 = function() {
    var tmp = new self.TTYUARTClass("__instanceV8");
    tmp.getSerialV8E();
    return tmp;
  }

  /**
   @function IO#getSerial2V8
   @type Function
   @returns global variable 'Serial2' value
   @instance
   */
  self.getSerial2V8 = function() {
    var tmp = new self.TTYUARTClass("__instanceV8");
    tmp.getSerial2V8E();
    return tmp;
  }

  /**
   @function IO#getSerial1V8
   @type Function
   @returns global variable 'Serial1' value
   @instance
   */
  self.getSerial1V8 = function() {
    var tmp = new self.TTYUARTClass("__instanceV8");
    tmp.getSerial1V8E();
    return tmp;
  }

  /**
   @function IO#setSerialV8
   @type Function
   @param {Object} value - value
   @desc Set global variable 'Serial' value
   @instance
   */
  self.setSerialV8 = function(value) {
    value.setSerialV8E();
  }

  /**
   @function IO#setSerial2V8
   @type Function
   @param {Object} value - value
   @desc Set global variable 'Serial2' value
   @instance
   */
  self.setSerial2V8 = function(value) {
    value.setSerial2V8E();
  }

  /**
   @function IO#setSerial1V8
   @type Function
   @param {Object} value - value
   @desc Set global variable 'Serial1' value
   @instance
   */
  self.setSerial1V8 = function(value) {
    value.setSerial1V8E();
  }

  /**
   @function IO#setSpiV8
   @type Function
   @param {Object} value - value
   @desc Set global variable 'SPI' value
   @instance
   */
  self.setSpiV8 = function(value) {
    value.setSpiV8E();
  }

  /**
   @function IO#getSpiV8
   @type Function
   @returns global variable 'SPI' value
   @instance
   */
  self.getSpiV8 = function() {
    var tmp = new self.SPIClass("__instanceV8");
    tmp.getSpiV8E();
    return tmp;
  }

  /**
   @function IO#setWireV8
   @type Function
   @param {Object} value - value
   @desc Set global variable 'Wire' value
   @instance
   */
  self.setWireV8 = function(value) {
    value.setWireV8E();
  }

  /**
   @function IO#getWireV8
   @type Function
   @returns global variable 'Wire' value
   @instance
   */
  self.getWireV8 = function() {
    var tmp = new self.TwoWire("__instanceV8");
    tmp.getWireV8E();
    return tmp;
  }

}
