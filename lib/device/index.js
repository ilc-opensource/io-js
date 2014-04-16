ga = require('bindings')('galileo.node');

// version check
ver = ga.version();
ver_addon = ga.version_addon();
if (ver != ver_addon)
  throw Error("libio-addon version('" + ver
            + "') is different with libio version('"
            + ver_addon + "')");

module.exports = ga;
