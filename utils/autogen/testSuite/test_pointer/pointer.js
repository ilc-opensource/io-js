exports.testIntShortArrayPointer = function() {
  console.log("Test int/short array/pointer Start!!!");

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  // Test int* & int[] & short* arguments and int* return-type
  a = [10, 11, 12, 13]
  b = [20];
  c = [30]

  ret = io.funcP(a, b, c);

  if (a[0] != 5 || a[1] != 11 || a[2] != 12 || a[3] != 13)
    throw Error("Failed!!!");

  if (b[0] != 10 || c[0] != 15)
    throw Error("Failed!!!");

  if (ret[0] != 5)// || ret[1] != 11 || ret[2] != 12 || ret[3] != 13)
    throw Error("Failed!!!");

  // Test setter/getter function for int[] global variable
  ia = [1,2,3,4]
  io.setPiaV8(ia)
  pia = io.getPiaV8()
  if (pia[0] != 1 || pia[1] != 2 || pia[2] != 3 || pia[3] != 4)
    throw Error("Failed!!!");

  // Test setter/getter function for short[] global variable
  sa = [11, 12, 13, 14]
  io.setPsaV8(sa)
  psa = io.getPsaV8()
  if (psa[0] != 11 || psa[1] != 12 || psa[2] != 13 || psa[3] != 14)
    throw Error("Failed!!!");

  ppsa = io.getPpsaV8()
  if (ppsa[0] != 11)// || ppsa[1] != 12 || ppsa[2] != 13 || ppsa[3] != 14)
    throw Error("Failed!!!");

  // Test setter/getter function for short* global variable
  psa = [21, 22, 23, 24]
  io.setPpsaV8(psa)
  ppsa = io.getPpsaV8()
  if (ppsa[0] != 21)// || ppsa[1] != 22 || ppsa[2] != 23 || ppsa[3] != 24)
    throw Error("Failed!!!");
  if (psa[0] != 21 || psa[1] != 22 || psa[2] != 23 || psa[3] != 24)
    throw Error("Failed!!!");

  console.log("Test int/short array/pointer Passed!!!");
}
