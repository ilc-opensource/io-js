exports.testCharArrayPointer = function() {
  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  console.log("Test char array/pointer Start!!!");

  // User Buffer to map C-String, if C-String is changed
  str = new Buffer("ni hao")

  ret = io.changeStr(str)

  if (str.toString() != "nj hao")
    throw Error("Failed!!!");

  if (ret != "Done")
    throw Error("Failed!!!");

  // User JS-String to map C-String, if C-String is not changed
  ret = io.copyCharArray("Hi")
  if (ret != "Done")
    throw Error("Failed!!!");

  // Test global variable with type "char array", ex: "char a[5]"
  a = io.getAV8()
  if (a != "Hi")
    throw Error("Failed!!!");

  io.setAV8("Ok")

  a = io.getAV8()
  if (a != "Ok")
    throw Error("Failed!!!");

  // Test global variable with type "char*", ex: "char *p"
  pa = io.getPV8()
  if (pa != "Ok")
    throw Error("Failed!!!");

  io.setPV8("Me")

  a = io.getAV8()
  if (a != "Me")
    throw Error("Failed!!!");

  pa = io.getPV8()
  if (pa != "Me")
    throw Error("Failed!!!");

  pc = io.getPcV8()
  if (pc != "Done")
    throw Error("Failed!!!");

  console.log("Test char array/pointer Passed!!!");
}
