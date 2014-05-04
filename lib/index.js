var Galileo = {
  //IO   : require('./device'),
  IO   : require('./companion/io_fake.js'),
  IO_rpc   : require('./companion/io_rpc.js'),
  Led  : require('./common/led').Led,
  Sensor : require('./common/sensors/basic_sensor').Sensor,
};

module.exports = Galileo;
