exports.testStruct = function() {
  var IOLIB = (typeof require === 'function') ? require('../../../../'): this.IOLIB;

  var io = new IOLIB.IO({
    log: true,
    //rpc: true,
    port: 2000,
    hostname: 'localhost',
    quickInit: false
  });

  var fp_cmp = require("../fp_cmp");

  console.log("Test struct args/ret-value Start!!!");

  s = {
    ss1: 2,
    e: io.EUC,
    e1: io.EUD1,
    ss2: [2,3,4,5,6,6,7]
  }

  obj = {
    a: [10,20,30,40],
    b: 21.36,
    e: io.EUA,
    str: new Buffer("nihao"),
    st: s
  }

  b = [20,10]

  ret = io.func(obj, b)

  if (b[0] != 10)
    throw Error("Failed!!!");

  if (obj.a[0] != 10 || !fp_cmp.float_eq(obj.b, 21.36) || obj.e != io.EUA || obj.str[3] !=  97)
    throw Error("Failed!!!");
  if (obj.st.ss1 != 2 || obj.st.ss2[2] != 4)
    throw Error("Failed!!!");

  if (ret.a[0] != 789 || !fp_cmp.float_eq(ret.b, 23.45) || ret.e != io.EUC1 || ret.str[3] != 't')
    throw Error("Failed!!!");
  if (ret.st.ss1 != 18 || ret.st.ss2[2] != 2)
    throw Error("Failed!!!");

  ret = io.funcp(b, obj)
  if (obj.a[0] != 789 || !fp_cmp.float_eq(obj.b, 23.45) || obj.e != io.EUC1 || obj.str[3] != 0x74)
    throw Error("Failed!!!");
  if (obj.st.ss1 != 18 || obj.st.ss2[2] != 2)
    throw Error("Failed!!!");

  objs = {
    ss1: 10,
    e: io.EUA,
    e1: io.EUA1,
    ss2: [10,20,30]
  }

  ret = io.funcss(objs)

  if ((objs.ss1 != 20) || objs.e != io.EUB || objs.e1 != io.EUC1 || objs.ss2[0] != 10 || objs.ss2[2] != 3)
    throw Error("Failed!!!");

  if ((ret.ss1 != 20) || ret.e != io.EUB || ret.e1 != io.EUC1 || ret.ss2[0] != 10 || ret.ss2[2] != 3)
    throw Error("Failed!!!");

  console.log("Test struct args/ret-value Passed!!!");

  console.log("Test global struct variable Start!!!");
  // Test global variable(struct ss sg) getter/setter function
  io.setSgV8(objs);
  sge = io.getSgV8();
  if ((sge.ss1 != 20) || sge.e != io.EUB || sge.e1 != io.EUC1 || sge.ss2[0] != 10 || sge.ss2[2] != 3)
    throw Error("Failed!!!");

  // Test global variable(struct_t st) getter/setter function
  io.setStV8(obj);

  stpe = io.getStpV8();
  if (stpe.a[0] != 789 || stpe.a[2] != 30 || !fp_cmp.float_eq(stpe.b, 23.45) || stpe.e != io.EUC1 || stpe.str[3] != 't' || stpe.str[0] != 'n')
    throw Error("Failed!!!");
  if (stpe.st.ss1 != 18 || stpe.st.ss2[2] != 2)
    throw Error("Failed!!!");

  ste = io.getStV8();
  if (ste.a[0] != 789 || ste.a[2] != 30 || !fp_cmp.float_eq(ste.b, 23.45) || ste.e != io.EUC1 || ste.str[3] != 't' || ste.str[0] != 'n')
    throw Error("Failed!!!");
  if (ste.st.ss1 != 18 || ste.st.ss2[2] != 2)
    throw Error("Failed!!!");

  // Test global variable(struct_t *stp) getter/setter function
  s = {
    ss1: 2,
    e: io.EUC,
    e1: io.EUD1,
    ss2: [2,3,4,5,6,6,7]
  }

  obj = {
    a: [10,20,30,40],
    b: 21.36,
    e: io.EUA,
    str: "nihao",
    st: s
  }

  io.setStpV8(obj);

  stpe = io.getStpV8();
  if (stpe.a[0] != 10 || stpe.a[2] != 30 || !fp_cmp.float_eq(stpe.b, 21.36) || stpe.e != io.EUA || stpe.str[3] != 'a' || stpe.str[0] != 'n')
    throw Error("Failed!!!");
  if (stpe.st.ss1 != 2 || stpe.st.ss2[2] != 4)
    throw Error("Failed!!!");

  console.log("Test global struct variable Passed!!!");
}
