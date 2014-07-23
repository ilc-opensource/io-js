exports.testCommon = function() {
  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  fp_cmp = require("../fp_cmp");

  console.log("Test Common-Type conversion Start!!!");

  // Test Float-Pointer arg-type/return-val conversion
  d = io.funcd(234.78, 1.23e70);
  if (!fp_cmp.double_eq(d, 1.23e70))
    throw Error("Failed!!!")

  d = io.funcd(234.78, 1234.11);
  if (!fp_cmp.float_eq(d, 1468.89))
    throw Error("Failed!!!")

  f = io.funcf(12.3e18);
  if (!fp_cmp.float_eq(f, 1.23e19))
    throw Error("Failed!!!")

  // Test Integer arg-type/return-val conversion
  ull = io.funcull(0x12345678, 0xab00000000)

  if (ull != 0xab12345678)
    throw Error("Failed!!!");

  ll = io.funcll(0xab76543210, 0x76543210);
  if (ll != 0xab00000000)
    throw Error("Failed!!!");

  ul = io.funcul(0xcd123456, 0x123456);
  if (ul != 0x00000000cd000000)
    throw Error("Failed!!!");

  l = io.funcl(0x11111111, 0x0012345678);
  if (l != 0x23456789)
    throw Error("Failed!!!");

  ui = io.funcui(0x48120000, 0xf456);
  if (ui != 0x000000004812f456)
    throw Error("Failed!!!");

  u = io.funcu(0x78120000, 0x3456);
  if (u != 0x0000000078123456)
    throw Error("Failed!!!");

  i = io.funci(0x79243456, 0x11123456);
  if (i != 0x68120000)
    throw Error("Failed!!!");

  us = io.funcus(0x8120000);
  if (us != 0x0)
    throw Error("Failed!!!");

  s = io.funcs(0x12345678);
  if (s != 0x5600)
    throw Error("Failed!!!");

  uc = io.funcuc(0x123456D8, 0x25);
  if (uc != 0xB3)
    throw Error("Failed!!!");

  c = io.funcc(0x12345678, 0x25);
  if (c != 0x53)
    throw Error("Failed!!!");

  // Test Float-Pointer global variable
  io.setGfV8(123456.789)
  f = io.getGfV8()
  if (!fp_cmp.float_eq(f, 123456.789))
    throw Error("Failed!!!");

  io.setGdV8(1234.23e89)
  d = io.getGdV8()
  if (!fp_cmp.float_eq(d, 1234.23e89))
    throw Error("Failed!!!");

  io.setGdV8(1234.2389123456)
  d = io.getGdV8()
  if (!fp_cmp.double_eq(d, 1234.2389123456))
    throw Error("Failed!!!");

  // Test Integer global variable
  io.setGucV8(0xB4)
  uc = io.getGucV8()
  if (uc != 0xB4)
    throw Error("Failed!!!");

  io.setGcV8(0xB4)
  c = io.getGcV8()
  if (c != -76)
    throw Error("Failed!!!");

  io.setGiV8(-0xF901234)
  i = io.getGiV8()
  if (i != -0xF901234)
    throw Error("Failed!!!");

  io.setGuiV8(0x8901234)
  ui = io.getGuiV8()
  if (ui != 0x8901234)
    throw Error("Failed!!!");

  io.setGuV8(0x78901234)
  u = io.getGuV8()
  if (u != 0x78901234)
    throw Error("Failed!!!");

  io.setGsV8(-3805)
  s = io.getGsV8()
  if (s != -3805)
    throw Error("Failed!!!");

  io.setGusV8(0x9234)
  us = io.getGusV8()
  if (us != 0x9234)
    throw Error("Failed!!!");

  io.setGlV8(-913873597)
  l = io.getGlV8()
  if (l != -913873597)
    throw Error("Failed!!!");

  io.setGulV8(0xF1239234)
  ul = io.getGulV8()
  if (ul != 0xF1239234)
    throw Error("Failed!!!");

  io.setGllV8(0xabcd01239234)
  ll = io.getGllV8()
  if (ll != 0xabcd01239234)
    throw Error("Failed!!!");

  io.setGllV8(-1)
  ll = io.getGllV8()
  if (ll != -1)
    throw Error("Failed!!!");

  io.setGullV8(0xFFFFabcd01239234)
  ull = io.getGullV8()
  if (ull != 0xFFFFabcd01239234)
    throw Error("Failed!!!");

  console.log("Test Common-Type conversion Passed!!!");
}
