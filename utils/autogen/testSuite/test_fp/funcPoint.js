exports.testFuncPointer = function() {

  console.log("Test function pointer Start!!!");

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  var cb_int_r_int = function(a) {
    return io.func_int_r_int(a)
  }

  var cb_int_r_floatp = function(a) {
    return io.func_int_r_floatp(a);
  }

  var cb_intp_r_intp = function(a) {
    return io.func_intp_r_intp(a);
  }

  var cb_float_r_int_charp = function(a, b) {
    return io.func_float_r_int_charp(a, b);
  }

  var cb_v_r_v = function() {
    io.func_v_r_v();
  }

  var cb_v_r_intp = function(a) {
    io.func_v_r_intp(a);
  }

  var cb_v_r_intp_t = function(a) {
    io.func_v_r_intp_t(a);
  }

  a1 = io.func_int_r_fp2(cb_int_r_int, cb_int_r_int);
  if (a1 != 11)
    throw Error("Failed!!!")

  a2 = io.func_int_r_fp1(cb_int_r_floatp);
  if (a2 != 1)
    throw Error("Failed!!!")

//  a3 = io.func_intp_r_fp1(cb_intp_r_intp);
//  if (a3[0] != 10)// || a3[1] != 3 || a3[2] != 4)
//    throw Error("Failed!!!")

  a4 = io.func_float_r_fp1(cb_float_r_int_charp);
  if (a4 != 110)
    throw Error("Failed!!!")

  a5 = io.func_int_r_fpd(cb_int_r_int);
  if (a5 != 123)
    throw Error("Failed!!!")

  io.func_v_r_fp(cb_v_r_v);
  ga = io.getGafpV8();
  if (ga != 16)
    throw Error("Failed!!!")

  ret = io.func_int_r_int_fp1(2, cb_v_r_intp);
  gb = io.getGbfpV8();
  if (ret != 2 || gb != 26)
    throw Error("Failed!!!")

  ret = io.func_int_r_int_fp1_t(21, cb_v_r_intp_t);
  gb = io.getGbfpV8();
  if (ret != 21 || gb != 46)
    throw Error("Failed!!!")

  console.log("Test function pointer Passed!!!");
}
