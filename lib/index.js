var Galileo = {
  //IO   : require('./device'),
  IO   : require('./companion/io_rpc.js'),
  Led  : require('./common/led'),
  Sensor : require('./common/sensors/basic_sensor'),
};

module.exports = Galileo;
