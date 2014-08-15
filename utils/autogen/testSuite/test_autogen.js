console.log("Test Autogen Start!!!")

var t = require("./test_common/common");
t.testCommon()

var te = require("./test_enum/enum");
te.testEnum()

var tc = require("./test_class/class");
tc.testClass()

var tcd = require("./test_char/str");
tcd.testCharArrayPointer()

var tfd = require("./test_pointer/pointerL");
tfd.testLonglongArrayPoint()

var tld = require("./test_pointer/pointerF");
tld.testFloatDoubleArrayPointer()

var tid = require("./test_pointer/pointer");
tid.testIntShortArrayPointer();

var ts = require("./test_struct/struct");
ts.testStruct();

var tfp = require("./test_fp/funcPoint");
tfp.testFuncPointer();

var tfp1 = require("./test_fp/mug");
tfp1.testFuncPointerStruct();

console.log("Test Autogen Passed!!!")
