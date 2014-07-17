exports.testFloatDoubleArrayPointer = function() {
  console.log("Test float/double array/pointer Start!!!")

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  fp_cmp = require("../fp_cmp");

  // Test int* & int[] & short* arguments and int* return-type
  a = [2.5, 8.5]
  b = [20.6e80, 70.8e56];
  c = [30.6, 9.5e100]

  ret = io.funcFP(a, b, c);

  if (!fp_cmp.float_eq(a[0], 2.5) || !fp_cmp.float_eq(a[1], 1238.789))
    throw Error("Failed!!!");

  if (!fp_cmp.double_eq(b[0], 20.6e80) || !fp_cmp.double_eq(b[1], 123456.0e+50))
    throw Error("Failed!!!");

  if (!fp_cmp.double_eq(c[0], 15896.0e+78) || !fp_cmp.double_eq(c[1], 9.5e100))
    throw Error("Failed!!!");

  if (!fp_cmp.double_eq(ret[0], 15896.0e+78))// || !fp_cmp.double_eq(ret[1], 9.5e100))
    throw Error("Failed!!!");

  // Test setter/getter function for float[] global variable
  fa = [123789.986, 5.36e37, -9.6e-3]
  io.setFaV8(fa)
  fat = io.getFaV8()
  if (!fp_cmp.float_eq(fa[0], fat[0]) || !fp_cmp.float_eq(fa[1], fat[1]) || !fp_cmp.float_eq(fa[2], fat[2]))
    throw Error("Failed!!!");

  // Test setter/getter function for double[] global variable
  lfa = [123789.98765, 5.789e100, 789.32e-120]
  io.setLfaV8(lfa)
  lfat = io.getLfaV8()
  if (!fp_cmp.double_eq(lfa[0], lfat[0]) || !fp_cmp.double_eq(lfa[1], lfat[1]) || !fp_cmp.double_eq(lfa[2], lfat[2]))
    throw Error("Failed!!!");

  plfa = io.getPlfaV8()
  if (!fp_cmp.double_eq(lfa[0], plfa[0]))// || !fp_cmp.double_eq(lfa[1], plfa[1]) || !fp_cmp.double_eq(lfa[2], plfa[2]))
    throw Error("Failed!!!");

  // Test setter/getter function for double* global variable
  plfa = [0x1122334455e27, 0x6677889900e-120, 24.5]
  io.setPlfaV8(plfa)
  plfat = io.getPlfaV8()
  if (!fp_cmp.double_eq(plfat[0], plfa[0]))// || !fp_cmp.double_eq(plfat[1], plfa[1]) || !fp_cmp.double_eq(plfat[2], plfa[2]))
    throw Error("Failed!!!");
  lfa = io.getLfaV8()
  if (!fp_cmp.double_eq(lfa[0], plfa[0]) || !fp_cmp.double_eq(lfa[1], plfa[1]) || !fp_cmp.double_eq(lfa[2], plfa[2]))
    throw Error("Failed!!!");

  console.log("Test float/double array/pointer Passed!!!")
}
