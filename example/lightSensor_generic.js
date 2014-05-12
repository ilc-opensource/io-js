var GA = require('../lib/');

var io = GA.IO;

io.initWithTty(new Buffer("/dev/tty1"),
               new Buffer("/dev/tty1"),
               new Buffer("/dev/tty1"));

var sensor = new GA.Sensor({
  io : io,
  pin: io.A2
});

setInterval(function() {
  sensor.read(function(err, val) {
    if (err)
      throw Error('read error.');

    console.log('The data read from sensor is ' + val + '.');

    var led = new GA.Led({
      io : io,
      pin: 13
    });

    // TODO: this val(152) can be changed according to the PWM-model
    //       and light-sensor-model
    if (val <= 300) {
      console.log('Led attached on pin ' + led.pin + ' is on.');
      led.on();
    } else {
      console.log('Led attached on pin ' + led.pin + ' is off.');
      led.off();
    }

  });
}, 500);

