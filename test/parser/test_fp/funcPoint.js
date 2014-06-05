ga = require("../lib/device/build/Debug/galileo")

var callback = function(a) {
  ga.f3(a)
}

var callback1 = function(a) {
  return ga.fint(a)
}

var cbif = function(a, b) {
  return ga.fintfloat(a, b)
}

ga.fp7 (callback)

a = ga.fp4 (callback1, callback1)
console.log("addon result: ", a)

console.log(ga.fp5(cbif))
