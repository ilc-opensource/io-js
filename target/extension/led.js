(function(exports, global) {
/////////////////////////////////////////////


/**
 * @class Led
   @param {Object}  options - configuration options
   @param {Object}  options.io - io object created with new IO()
   @param {Integer} [options.pin=13] - pin number
   @param {bright}  [options.bright=0] - led brightness
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

/** 
 * @function Led.on
 * @type Function
 * @desc Turn on Led
 * @instance
 */
Led.prototype.on = function () {
  this.io.digitalWrite(this.pin, this.io.HIGH);
  this.bright = 255;
}

/**
 * @function Led.off
 * @type Function
 * @desc Turn off Led
 * @instance
 */
Led.prototype.off = function () {
  this.io.digitalWrite(this.pin, this.io.LOW);
  this.bright = 0;
}

/**
 * @function Led.brightLevel
 * @type Function
 * @desc Set Led brightness level
 * @instance
 * @param {Integer} val - Bright less level [0, 15]
 */
Led.prototype.brightLevel = function(val) {
  this.io.analogWrite(this.pin, this.bright = val);
}

/**
 * @function Led.fade
 * @type Function
 * @desc Led dime out
 * @instance
 * @param {Integer} interval - time interval
 */
Led.prototype.fade = function(interval) {
  to = (interval || 5000) / (255 * 2);
  var self = this;
  setInterval(function() {
    if(self.bright == 0) direction = 1;
    if(self.bright == 255) direction = -1;
    self.brightLevel(self.bright + direction);
  }, to);
}

/**
 * @function Led.blink
 * @type Function
 * @desc Led blink 
 * @instance
 * @param {Integer} interval - time interval
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
