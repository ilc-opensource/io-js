/* This lib is for simple sensor which does not need converter,
 * Such as light sensor
 */

/*
 * Main Sensor constructor
 */
var Sensor = function (options) {
  if (options == undefined || options.io == undefined)
      throw new Error('\"io\" is not configured to Sensor.');

  if (options.pin == undefined)
      console.log('\"pin\" is not configured, default value is ANALOG0.');

  this.io = options.io;                    // set io

  this.pin = options.pin || this.io.A0;     // set pin

  this.io.pinMode(this.pin, this.io.INPUT);
};

Sensor.prototype.read = function(callback) {
  var val = this.io.analogRead(this.pin);
  if (val < 0)
    return callback(1);
  else
    return callback(0, val);
}

module.exports = Sensor;
