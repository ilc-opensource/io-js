exports.testEnum = function() {
  console.log("Test Enumeration Start!!!");

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  // Test function with enum arguments or enum ret-type
  a1 = io.testEnum(io.A1)
  if (a1 != io.B5)
    throw Error("Failed!!!")

  b2 = io.testEnumT(io.B3)
  if (b2 != io.A2)
    throw Error("Failed!!!")

  // Test global enum var:ga
  ga = io.getGaV8()
  if (ga != io.A2)
    throw Error("Failed!!!")

  io.setGaV8(io.A4)

  ga = io.getGaV8()
  if (ga != io.A4)
    throw Error("Failed!!!")

  // Test global enum var: gb
  gb = io.getGbV8()
  if (gb != io.B2)
    throw Error("Failed!!!")

  io.setGbV8(io.B4)

  gb = io.getGbV8()
  if (gb != io.B4)
    throw Error("Failed!!!")

  console.log("Test Enumeration Passed!!!");
}
