ga = require("../lib/device/build/Debug/galileo")

a = new Array();
a[0] = 15;
b = new Array();
b[0] = 20;
c = new Buffer("nihao")
console.log("Before Call")
console.log("a:", a)
console.log("b:", b)
console.log("c:", c.toString())
ga.funcP(a, b, c);
console.log("After Call")
console.log("a:", a)
console.log("b:", b)
console.log("c:", c.toString())
