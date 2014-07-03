exports.testLonglongArrayPoint = function () {
  console.log("Test \'long\'/\'long long\' Array/Pointer Start!!!");

  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  // Test long[] & long long[] & long long* arguments and long long* return-type
  a = [0x12345678, 0x9abcdef0, 12, 13]
  b = [0xaa12345678, 0xbb9abcdef0, 12, 13]
  c = [0xcc12345678, 0xdd9abcdef0, 12, 13]

  ret = io.funcLP(a, b, c);

  if (a[0] != 0x12345678 || a[1] != 0x5a5a5a || a[2] != 12 || a[3] != 13)
    throw Error("Failed!!!");

  if (b[0] != 0xaa12345678 || b[1] !=0xbb9abcdef0 || b[2] != 0x5a5a5a5a5a || b[3] != 13)
    throw Error("Failed!!!");

  if (c[0] != 0x1a1a1a1a1a || c[1] != 0xdd9abcdef0 || c[2] != 12 || c[3] != 13)
    throw Error("Failed!!!");

  if (ret[0] != 0x1a1a1a1a1a || ret[1] != 0xdd9abcdef0 || ret[2] != 12 || ret[3] != 13)
    throw Error("Failed!!!");

  // Test setter/getter function for long[] global variable
  la = [0x12345678, 0x23456789, 3, 4]
  io.setLaV8(la)
  lat = io.getLaV8()
  if (lat[0] != la[0] || lat[1] != la[1] || lat[2] != la[2] || lat[3] != la[3])
    throw Error("Failed!!!");

  // Test setter/getter function for long long[] global variable
  lla = [0x112233445566, 0x6677889900AA, 23, 24]
  io.setLlaV8(lla)
  llat = io.getLlaV8()
  if (llat[0] != lla[0] || llat[1] != lla[1] || llat[2] != lla[2] || llat[3] != lla[3])
    throw Error("Failed!!!");

  plla = io.getPllaV8()
  if (plla[0] != lla[0] || plla[1] != lla[1] || plla[2] != lla[2] || plla[3] != lla[3])
    throw Error("Failed!!!");

  // Test setter/getter function for long long* global variable
  plla = [0x1122334455, 0x6677889900, 23, 24]
  io.setPllaV8(plla)
  pllat = io.getPllaV8()
  if (pllat[0] != plla[0] || pllat[1] != plla[1] || pllat[2] != plla[2] || pllat[3] != plla[3])
    throw Error("Failed!!!");
  lla = io.getLlaV8()
  if (lla[0] != plla[0] || lla[1] != plla[1] || lla[2] != plla[2] || lla[3] != plla[3])
    throw Error("Failed!!!");

  console.log("Test \'long\'/\'long long\' Array/Pointer Passed!!!");
}
