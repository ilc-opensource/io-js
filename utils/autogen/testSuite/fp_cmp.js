exports.float_eq =  function(f1, f2) {
  if (Math.abs(f1 - f2)/f1 < 1e-6)
    return true;
  else
    return false;
}

exports.double_eq =  function(d1, d2) {
  if (Math.abs(d1 - d2)/d1 < 1e-23)
    return true;
  else
    return false;
}
