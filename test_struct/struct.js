ga = require("../lib/device/build/Debug/galileo")

obj = {
a: 15,
b: 21.36,
str: "hello",
st: {
  ss1: 2,
  ss2: 3,
}}

console.log(obj)
ga.func(obj, 5 )
console.log(obj)
ga.funcp(obj, 5 )
console.log(obj)

