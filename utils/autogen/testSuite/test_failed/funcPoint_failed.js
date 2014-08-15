exports.testFuncPointerFailed = function() {

  console.log("[JS]: Test function pointer Start!!!");

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  var cb_v_r_intp = function(a) {
    io.fail_func_v_r_intp(a);
  }

  ret = io.fail_func_int_r_int_fp1(2, cb_v_r_intp);
  ga = io.getFail_gafpV8();
  if (ret != 2 || ga != 26)
    throw Error("Failed!!!")

  console.log("[JS]: Test function pointer Passed!!!");
}
