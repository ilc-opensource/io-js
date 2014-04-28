module.exports.dump = function(className, funcName, args) {
  var argArr = Array.prototype.slice.call(args);

  var prefix;

  if (className) {
    prefix = className + "." + funcName;
  } else {
    prefix = funcName;
  }
  console.log(funcName + ":(" + JSON.stringify(argArr) + ")");
}
