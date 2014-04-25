var IO = require('bindings')('galileo.node');

// version check
ver = IO.version();
ver_addon = IO.version_addon();
if (ver != ver_addon)
  throw Error("libio-addon version('" + ver
      + "') is different with libio version('"
      + ver_addon + "')");

module.exports = IO;
