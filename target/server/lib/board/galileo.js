
/*********************************************
Generated with autogen tool
*********************************************/

var methods = function(options) {
  var self = this;
  self.io = options.io;
  self.handle = options.handle;
  var map = {};


  /****************************************
             fast_gpio_sc
  ****************************************/

  map['fastGpioSCInit'] = function() {
    self.handle.funcReq(self.io.fastGpioSCInit, arguments, 'fastGpioSCInit');
  };

  map['fastGpioSCFini'] = function() {
    self.handle.funcReq(self.io.fastGpioSCFini, arguments, 'fastGpioSCFini');
  };

  map['fastGpioDigitalWrite'] = function() {
    self.handle.funcReq(self.io.fastGpioDigitalWrite, arguments, 'fastGpioDigitalWrite');
  };

  map['fastGpioDigitalWriteDestructive'] = function() {
    self.handle.funcReq(self.io.fastGpioDigitalWriteDestructive, arguments, 'fastGpioDigitalWriteDestructive');
  };

  map['fastGpioDigitalLatch'] = function() {
    self.handle.funcReq(self.io.fastGpioDigitalLatch, arguments, 'fastGpioDigitalLatch');
  };

  /****************************************
             pin_map_norm
  ****************************************/

  /****************************************
             Arduino
  ****************************************/

  /****************************************
             Servo
  ****************************************/

  map['Servo'] = function() {
    self.handle.classReq(self.io.Servo, arguments, 'Servo');
  };

  map['Servo.attach'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'attach');
  };

  map['Servo.detach'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'detach');
  };

  map['Servo.write'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'write');
  };

  map['Servo.writeMicroseconds'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'writeMicroseconds');
  };

  map['Servo.read'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'read');
  };

  map['Servo.readMicroseconds'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'readMicroseconds');
  };

  map['Servo.attached'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'attached');
  };

  map['Servo.set48hz'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'set48hz');
  };

  map['Servo.set188hz'] = function() {
    self.handle.classMethodReq(arguments, 'Servo', 'set188hz');
  };

  /****************************************
             OSAbstract_norm
  ****************************************/

  map['initWithTty'] = function() {
    self.handle.funcReq(self.io.initWithTty, arguments, 'initWithTty');
  };

  /****************************************
             pins_arduino
  ****************************************/

  /****************************************
             wiring_digital_norm
  ****************************************/

  map['pinInit'] = function() {
    self.handle.funcReq(self.io.pinInit, arguments, 'pinInit');
  };

  map['pinMode'] = function() {
    self.handle.funcReq(self.io.pinMode, arguments, 'pinMode');
  };

  map['pinModeIRQ'] = function() {
    self.handle.funcReq(self.io.pinModeIRQ, arguments, 'pinModeIRQ');
  };

  map['digitalWrite'] = function() {
    self.handle.funcReq(self.io.digitalWrite, arguments, 'digitalWrite');
  };

  map['digitalRead'] = function() {
    self.handle.funcReq(self.io.digitalRead, arguments, 'digitalRead');
  };

  map['pinHandleReopen'] = function() {
    self.handle.funcReq(self.io.pinHandleReopen, arguments, 'pinHandleReopen');
  };

  map['pinGetIndex'] = function() {
    self.handle.funcReq(self.io.pinGetIndex, arguments, 'pinGetIndex');
  };

  map['pin2path'] = function() {
    self.handle.funcReq(self.io.pin2path, arguments, 'pin2path');
  };

  map['gpio2gpiohandle'] = function() {
    self.handle.funcReq(self.io.gpio2gpiohandle, arguments, 'gpio2gpiohandle');
  };

  map['pin2gpiohandle'] = function() {
    self.handle.funcReq(self.io.pin2gpiohandle, arguments, 'pin2gpiohandle');
  };

  /****************************************
             AnalogIO
  ****************************************/

  map['pwmInit'] = function() {
    self.handle.funcReq(self.io.pwmInit, arguments, 'pwmInit');
  };

  map['analogRead'] = function() {
    self.handle.funcReq(self.io.analogRead, arguments, 'analogRead');
  };

  map['analogReadResolution'] = function() {
    self.handle.funcReq(self.io.analogReadResolution, arguments, 'analogReadResolution');
  };

  map['analogReference'] = function() {
    self.handle.funcReq(self.io.analogReference, arguments, 'analogReference');
  };

  map['analogWrite'] = function() {
    self.handle.funcReq(self.io.analogWrite, arguments, 'analogWrite');
  };

  map['pin2pwmhandle_enable'] = function() {
    self.handle.funcReq(self.io.pin2pwmhandle_enable, arguments, 'pin2pwmhandle_enable');
  };

  /****************************************
             sysfs
  ****************************************/

  map['sysfsPwmExport'] = function() {
    self.handle.funcReq(self.io.sysfsPwmExport, arguments, 'sysfsPwmExport');
  };

  map['sysfsPwmEnable'] = function() {
    self.handle.funcReq(self.io.sysfsPwmEnable, arguments, 'sysfsPwmEnable');
  };

  map['sysfsPwmDisable'] = function() {
    self.handle.funcReq(self.io.sysfsPwmDisable, arguments, 'sysfsPwmDisable');
  };

  map['sysfsGpioSet'] = function() {
    self.handle.funcReq(self.io.sysfsGpioSet, arguments, 'sysfsGpioSet');
  };

  map['sysfsGpioGet'] = function() {
    self.handle.funcReq(self.io.sysfsGpioGet, arguments, 'sysfsGpioGet');
  };

  map['sysfsGpioExport'] = function() {
    self.handle.funcReq(self.io.sysfsGpioExport, arguments, 'sysfsGpioExport');
  };

  map['sysfsGpioDirection'] = function() {
    self.handle.funcReq(self.io.sysfsGpioDirection, arguments, 'sysfsGpioDirection');
  };

  map['sysfsGpioEdgeConfig'] = function() {
    self.handle.funcReq(self.io.sysfsGpioEdgeConfig, arguments, 'sysfsGpioEdgeConfig');
  };

  map['sysfsGpioLevelConfig'] = function() {
    self.handle.funcReq(self.io.sysfsGpioLevelConfig, arguments, 'sysfsGpioLevelConfig');
  };

  map['sysfsGpioSetDrive'] = function() {
    self.handle.funcReq(self.io.sysfsGpioSetDrive, arguments, 'sysfsGpioSetDrive');
  };

  /****************************************
             i2c
  ****************************************/

  map['i2c_getadapter'] = function() {
    self.handle.funcReq(self.io.i2c_getadapter, arguments, 'i2c_getadapter');
  };

  map['i2c_openadapter'] = function() {
    self.handle.funcReq(self.io.i2c_openadapter, arguments, 'i2c_openadapter');
  };

  map['i2c_setslave'] = function() {
    self.handle.funcReq(self.io.i2c_setslave, arguments, 'i2c_setslave');
  };

  map['i2c_writebyte'] = function() {
    self.handle.funcReq(self.io.i2c_writebyte, arguments, 'i2c_writebyte');
  };

  map['i2c_writebytes'] = function() {
    self.handle.funcReq(self.io.i2c_writebytes, arguments, 'i2c_writebytes');
  };

  map['i2c_readbyte'] = function() {
    self.handle.funcReq(self.io.i2c_readbyte, arguments, 'i2c_readbyte');
  };

  map['i2c_readbytes'] = function() {
    self.handle.funcReq(self.io.i2c_readbytes, arguments, 'i2c_readbytes');
  };

  map['i2c_readwrite'] = function() {
    self.handle.funcReq(self.io.i2c_readwrite, arguments, 'i2c_readwrite');
  };

  map['i2c_add_to_buf'] = function() {
    self.handle.funcReq(self.io.i2c_add_to_buf, arguments, 'i2c_add_to_buf');
  };

  /****************************************
             version
  ****************************************/

  map['version'] = function() {
    self.handle.funcReq(self.io.version, arguments, 'version');
  };

  /****************************************
             variant_norm
  ****************************************/

  map['muxSelectDigitalPin'] = function() {
    self.handle.funcReq(self.io.muxSelectDigitalPin, arguments, 'muxSelectDigitalPin');
  };

  map['muxSelectAnalogPin'] = function() {
    self.handle.funcReq(self.io.muxSelectAnalogPin, arguments, 'muxSelectAnalogPin');
  };

  map['muxSelectUart'] = function() {
    self.handle.funcReq(self.io.muxSelectUart, arguments, 'muxSelectUart');
  };

  map['muxSelectSpi'] = function() {
    self.handle.funcReq(self.io.muxSelectSpi, arguments, 'muxSelectSpi');
  };

  map['muxSelectI2c'] = function() {
    self.handle.funcReq(self.io.muxSelectI2c, arguments, 'muxSelectI2c');
  };

  map['variantPinMode'] = function() {
    self.handle.funcReq(self.io.variantPinMode, arguments, 'variantPinMode');
  };

  map['variantPinModeIRQ'] = function() {
    self.handle.funcReq(self.io.variantPinModeIRQ, arguments, 'variantPinModeIRQ');
  };

  map['turnOffPWM'] = function() {
    self.handle.funcReq(self.io.turnOffPWM, arguments, 'turnOffPWM');
  };

  map['turnOnPWM'] = function() {
    self.handle.funcReq(self.io.turnOnPWM, arguments, 'turnOnPWM');
  };

  map['variantEnableFastGpio'] = function() {
    self.handle.funcReq(self.io.variantEnableFastGpio, arguments, 'variantEnableFastGpio');
  };

  map['variantEnablePullup'] = function() {
    self.handle.funcReq(self.io.variantEnablePullup, arguments, 'variantEnablePullup');
  };

  self.map = map;
};

module.exports =  methods;
