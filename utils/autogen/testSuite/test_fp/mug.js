exports.testFuncPointerStruct = function() {

  console.log("Test function pointer with struct-params Start!!!");

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  var cb_mug_func = function(a) {
    return io.mug_func(a)
  }
  
  a1 = io.getMsaV8();

  io.mug_read_motion_sensor_async(cb_mug_func);
  a1 = io.getMsaV8();

  if (a1.ax != 10 || a1.ay != 20)
    throw Error("Failed!!!")

  console.log("Test function pointer with struct-params Passed!!!");
}
