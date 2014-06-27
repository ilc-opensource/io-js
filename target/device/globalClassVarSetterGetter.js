var IO = require('bindings')('galileo.node')

IO.getSerialV8 = function() {
  var tmp = new IO.TTYUARTClass("__instanceV8");
  tmp.getSerialV8E();
  return tmp;
}

IO.getSerial2V8 = function() {
  var tmp = new IO.TTYUARTClass("__instanceV8");
  tmp.getSerial2V8E();
  return tmp;
}

IO.getSerial1V8 = function() {
  var tmp = new IO.TTYUARTClass("__instanceV8");
  tmp.getSerial1V8E();
  return tmp;
}

IO.setSerialV8 = function(value) {
  value.setSerialV8E();
}

IO.setSerial2V8 = function(value) {
  value.setSerial2V8E();
}

IO.setSerial1V8 = function(value) {
  value.setSerial1V8E();
}

IO.setSpiV8 = function(value) {
  value.setSpiV8E();
}

IO.getSpiV8 = function() {
  var tmp = new IO.SPIClass("__instanceV8");
  tmp.getSpiV8E();
  return tmp;
}

IO.setWireV8 = function(value) {
  value.setWireV8E();
}

IO.getWireV8 = function() {
  var tmp = new IO.TwoWire("__instanceV8");
  tmp.getWireV8E();
  return tmp;
}

module.exports = IO;
