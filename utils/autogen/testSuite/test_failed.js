console.log("Test Autogen Start!!!")

// 'Integer *Uint32::New()'
// Can not return a unsigned int32 value.
var tu = require("./test_failed/unsigned_failed");
tu.testUnsignedFailed()

console.log("Test Autogen Passed!!!")
