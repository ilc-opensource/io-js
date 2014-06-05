(function(exports, global) {

var HighLevel;

if(typeof require === 'function') {

  HighLevel = {
    Led: require('./led.js').Led,
//    Sensor: require('./sensors/basic_sensor.js').Sensor
  };
} else {
  HighLevel = {
    Led: global.Led,
//    Sensor: global.IOLIB.Sensor
  };
}

exports.HighLevel = HighLevel;

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB);
