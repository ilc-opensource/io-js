(function(exports, global) {
/////////////////////////////////////////////


/*
 * Main LED constructor
 */
var Led = function (options) {
  if (options === undefined || options.io === undefined)
    throw new Error('Must supply required options to LED');
  this.io = options.io;
  this.pin = options.pin || 0;
  this.bright = 0;
  this.io.pinMode(this.pin, this.io.OUTPUT);
  this.direction = -1;
}

/*
 * Turn the LED on
 */
Led.prototype.on = function () {
  this.io.digitalWrite(this.pin, this.io.HIGH);
  this.bright = 255;
}

/*
 * Turn the LED off
 */
Led.prototype.off = function () {
  this.io.digitalWrite(this.pin, this.io.LOW);
  this.bright = 0;
}

Led.prototype.brightLevel = function(val) {
  this.io.analogWrite(this.pin, this.bright = val);
}

Led.prototype.fade = function(interval) {
  to = (interval || 5000) / (255 * 2);
  var self = this;
  setInterval(function() {
    if(self.bright == 0) direction = 1;
    if(self.bright == 255) direction = -1;
    self.brightLevel(self.bright + direction);
  }, to);
}

/*
 * Start a bariable blinking pattern
 */
Led.prototype.blink = function (interval) {
  interval = interval || 1000;
  var self = this;
  setInterval(function(){
    if (self.bright) {
      self.off()
    } else {
      self.on();
    }
  }, interval);
}

exports.Led = Led;

/////////////////////////////////////////////
})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB );
