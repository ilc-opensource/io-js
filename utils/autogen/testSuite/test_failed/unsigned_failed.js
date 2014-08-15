exports.testUnsignedFailed = function() {
  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  console.log("Test unsigned global variable Start!!!");

  io.setGueV8(2828014132);
  // 'Integer *Uint32::New()'
  // Can not return a unsigned int32 value.
  u = io.getGueV8();
  // if (u != -1466953164)
  if (u != 2828014132)
    console.log("Error:Test unsigned global variable Failed!!!");

  console.log("Test unsigned global variable Passed!!!");
}
