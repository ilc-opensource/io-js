ga = require("../lib/device/build/Debug/galileo")

obj = {
  a: [10,20,30,40],
  b: 21.36,
  str: new Buffer("nihao"),
  st: {
    ss1: 2,
    ss2: [2,3,4,5,6,6,7]
  }
}

b = [20,10]

console.log("!!!1Before Call")
console.log('b:\n', b)
console.log('obj:\n', obj)
console.log('obj.str:\n', obj.str.toString())
ret = ga.func(obj, b )
console.log("!!!!After Call func")
console.log('b:\n', b)
console.log('obj:\n', obj)
console.log('obj.str:\n', obj.str.toString())
console.log('==return value:\n', ret)
ret = ga.funcp(obj, b )
console.log("\n!!!!After Call funcp")
console.log('b:\n', b)
console.log('obj:\n', obj)
console.log('obj.str:\n', obj.str.toString())
console.log('==return value:\n', ret)
