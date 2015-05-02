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

  s = [{
    ss1: 2,
    e: io.EUC,
    e1: io.EUD1,
    ss2: [2,3,4,5,6,6,7]
  }]

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

  if (obj.st[0].ss1 != 2 || ((obj.st[0]).ss2)[2] != 4)
    throw Error("Failed!!!");

  if (ret.a[0] != 789 || !fp_cmp.float_eq(ret.b, 23.45) || ret.e != io.EUC1 || ret.str[3] != 't')
    throw Error("Failed!!!");
  if (ret.st[0].ss1 != 18 || ret.st[0].ss2[0] != 2)
    throw Error("Failed!!!");

  objArr = obj
  ret = io.funcp(b, objArr)
  if (objArr.a[0] != 789 || !fp_cmp.float_eq(objArr.b, 23.45) || objArr.e != io.EUC1 || objArr.str[3] != 0x74)
    throw Error("Failed!!!");
  if (objArr.st[0].ss1 != 18 || objArr.st[0].ss2[2] != 2)
    throw Error("Failed!!!");

  objs = {
    ss1: 10,
    e: io.EUA,
    e1: io.EUA1,
    ss2: [10,20,30]
  }

  objsArr = [ objs ]

  ret = io.funcss(objsArr)

  if ((objsArr[0].ss1 != 20) || objsArr[0].e != io.EUB || objsArr[0].e1 != io.EUC1 || objsArr[0].ss2[0] != 10 || objsArr[0].ss2[2] != 3)
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

  ste = io.getStV8();
  if (ste.a[0] != 789 || ste.a[2] != 30 || !fp_cmp.float_eq(ste.b, 23.45) || ste.e != io.EUC1 || ste.str[3] != 't' || ste.str[0] != 'n')
    throw Error("Failed!!!");
  if (ste.st[0].ss1 != 18 || ste.st[0].ss2[0] != 2)
    throw Error("Failed!!!");

  // Test global variable(struct_t stp[2]) getter/setter function
  s0 = {
    ss1: 2,
    e: io.EUC,
    e1: io.EUD1,
    ss2: [2,3,4,5,6,6,7]
  }

  s1 = {
    ss1: 22,
    e: io.EUB,
    e1: io.EUC1,
    ss2: [4,5,6,6,7]
  }

  obj0 = {
    a: [10,20,30,40],
    b: 21.36,
    e: io.EUA,
    str: "nihao",
    st: [s0]
  }

  obj1 = {
    a: [20,30,40],
    b: 98.76,
    e: io.EUB,
    str: "please",
    st: [s0, s1]
  }
  io.setStpV8([obj0, obj1]);

  stpe = io.getStpV8();

  if (stpe[0].a[0] != obj0.a[0] || stpe[0].a[2] != obj0.a[2] || !fp_cmp.float_eq(stpe[0].b, obj0.b) || stpe[0].e != obj0.e || stpe[0].str[3] != obj0.str[3] || stpe[0].str[0] != obj0.str[0])
    throw Error("Failed!!!");
  if (stpe[0].st[0].ss1 != obj0.st[0].ss1 || stpe[0].st[0].ss2[0] != obj0.st[0].ss2[0])
    throw Error("Failed!!!");

  if (stpe[1].a[0] != obj1.a[0] || stpe[0].a[2] != obj0.a[2] || !fp_cmp.float_eq(stpe[1].b, obj1.b) || stpe[1].e != obj1.e || stpe[1].str[3] != obj1.str[3] || stpe[1].str[0] != obj1.str[0])
    throw Error("Failed!!!");
  if (stpe[1].st[0].ss1 != obj1.st[0].ss1 || stpe[1].st[0].ss2[0] != obj1.st[0].ss2[0])
    throw Error("Failed!!!");

  console.log("Test global struct variable Passed!!!");
}
