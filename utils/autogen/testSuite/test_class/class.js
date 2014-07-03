exports.testClass = function() {
  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  console.log("Test class Start!!!");

  // Test new function of class A
  a1 = new io.A(5);
  if (a1.getValue() != 5)
    throw Error("Failed!!!");

  a2 = new io.A(10);
  if (a2.getValue() != 10)
    throw Error("Failed!!!");

  // Test new function of class B
  b1 = new io.B(a1);
  if (b1.getValue() != 5)
    throw Error("Failed!!!");

  b2 = new io.B(a2);
  if (b2.getValue() != 10)
    throw Error("Failed!!!");

  // Test getA (the type of return value is class)
  a3 = b1.getA()
  if (a3.getValue() != 5)
    throw Error("Failed!!!");

  a4 = b2.getA()
  if (a4.getValue() != 10)
    throw Error("Failed!!!");

  // Test setA (arguments type is class)
  b1.setA(a2)
  if (b1.getValue() != 10)
    throw Error("Failed!!!");

  b2.setA(a1)
  if (b2.getValue() != 5)
    throw Error("Failed!!!");

  // Test setter/getter function of Ainstance
  a = io.getAinstanceV8();
  if (a.getValue() != 100)
    throw Error("Failed!!!");

  io.setAinstanceV8(a2);

  a = io.getAinstanceV8();
  if (a.getValue() != 10)
    throw Error("Failed!!!");

  // Test setter/getter function of Binstance
  b = io.getBinstanceV8();
  if (b.getValue() != 10)
    throw Error("Failed!!!");

  io.setBinstanceV8(b2);
  b = io.getBinstanceV8();
  if (b.getValue() != 5)
    throw Error("Failed!!!");

  console.log("Test Class Passed!!!");
}
