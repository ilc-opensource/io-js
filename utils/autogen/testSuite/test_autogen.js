console.log("Test Autogen Start!!!")
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

console.log("Test Autogen Passed!!!")
