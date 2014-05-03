
  /****************************************
             AnalogIO
  ****************************************/

  'pwmInit': function() {
    handle.funcReq(io.pwmInit, arguments, 'pwmInit');
  },

  'analogRead': function() {
    handle.funcReq(io.analogRead, arguments, 'analogRead');
  },

  'analogReadResolution': function() {
    handle.funcReq(io.analogReadResolution, arguments, 'analogReadResolution');
  },

  'analogReference': function() {
    handle.funcReq(io.analogReference, arguments, 'analogReference');
  },

  'analogWrite': function() {
    handle.funcReq(io.analogWrite, arguments, 'analogWrite');
  },

  'pin2pwmhandle_enable': function() {
    handle.funcReq(io.pin2pwmhandle_enable, arguments, 'pin2pwmhandle_enable');
  },

  /****************************************
             i2c
  ****************************************/

  'i2c_getadapter': function() {
    handle.funcReq(io.i2c_getadapter, arguments, 'i2c_getadapter');
  },

  'i2c_openadapter': function() {
    handle.funcReq(io.i2c_openadapter, arguments, 'i2c_openadapter');
  },

  'i2c_setslave': function() {
    handle.funcReq(io.i2c_setslave, arguments, 'i2c_setslave');
  },

  'i2c_writebyte': function() {
    handle.funcReq(io.i2c_writebyte, arguments, 'i2c_writebyte');
  },

  'i2c_writebytes': function() {
    handle.funcReq(io.i2c_writebytes, arguments, 'i2c_writebytes');
  },

  'i2c_readbyte': function() {
    handle.funcReq(io.i2c_readbyte, arguments, 'i2c_readbyte');
  },

  'i2c_readbytes': function() {
    handle.funcReq(io.i2c_readbytes, arguments, 'i2c_readbytes');
  },

  'i2c_readwrite': function() {
    handle.funcReq(io.i2c_readwrite, arguments, 'i2c_readwrite');
  },

  'i2c_add_to_buf': function() {
    handle.funcReq(io.i2c_add_to_buf, arguments, 'i2c_add_to_buf');
  },

  /****************************************
             pins_arduino
  ****************************************/

  /****************************************
             version
  ****************************************/

  'version': function() {
    handle.funcReq(io.version, arguments, 'version');
  },

  /****************************************
             wiring_digital_norm
  ****************************************/

  'pinInit': function() {
    handle.funcReq(io.pinInit, arguments, 'pinInit');
  },

  'pinMode': function() {
    handle.funcReq(io.pinMode, arguments, 'pinMode');
  },

  'pinModeIRQ': function() {
    handle.funcReq(io.pinModeIRQ, arguments, 'pinModeIRQ');
  },

  'digitalWrite': function() {
    handle.funcReq(io.digitalWrite, arguments, 'digitalWrite');
  },

  'digitalRead': function() {
    handle.funcReq(io.digitalRead, arguments, 'digitalRead');
  },

  'pinHandleReopen': function() {
    handle.funcReq(io.pinHandleReopen, arguments, 'pinHandleReopen');
  },

  'pinGetIndex': function() {
    handle.funcReq(io.pinGetIndex, arguments, 'pinGetIndex');
  },

  'pin2path': function() {
    handle.funcReq(io.pin2path, arguments, 'pin2path');
  },

  'gpio2gpiohandle': function() {
    handle.funcReq(io.gpio2gpiohandle, arguments, 'gpio2gpiohandle');
  },

  'pin2gpiohandle': function() {
    handle.funcReq(io.pin2gpiohandle, arguments, 'pin2gpiohandle');
  },

  /****************************************
             sysfs
  ****************************************/

  'sysfsPwmExport': function() {
    handle.funcReq(io.sysfsPwmExport, arguments, 'sysfsPwmExport');
  },

  'sysfsPwmEnable': function() {
    handle.funcReq(io.sysfsPwmEnable, arguments, 'sysfsPwmEnable');
  },

  'sysfsPwmDisable': function() {
    handle.funcReq(io.sysfsPwmDisable, arguments, 'sysfsPwmDisable');
  },

  'sysfsGpioSet': function() {
    handle.funcReq(io.sysfsGpioSet, arguments, 'sysfsGpioSet');
  },

  'sysfsGpioGet': function() {
    handle.funcReq(io.sysfsGpioGet, arguments, 'sysfsGpioGet');
  },

  'sysfsGpioExport': function() {
    handle.funcReq(io.sysfsGpioExport, arguments, 'sysfsGpioExport');
  },

  'sysfsGpioDirection': function() {
    handle.funcReq(io.sysfsGpioDirection, arguments, 'sysfsGpioDirection');
  },

  'sysfsGpioEdgeConfig': function() {
    handle.funcReq(io.sysfsGpioEdgeConfig, arguments, 'sysfsGpioEdgeConfig');
  },

  'sysfsGpioLevelConfig': function() {
    handle.funcReq(io.sysfsGpioLevelConfig, arguments, 'sysfsGpioLevelConfig');
  },

  'sysfsGpioSetDrive': function() {
    handle.funcReq(io.sysfsGpioSetDrive, arguments, 'sysfsGpioSetDrive');
  },

  /****************************************
             fast_gpio_sc
  ****************************************/

  'fastGpioSCInit': function() {
    handle.funcReq(io.fastGpioSCInit, arguments, 'fastGpioSCInit');
  },

  'fastGpioSCFini': function() {
    handle.funcReq(io.fastGpioSCFini, arguments, 'fastGpioSCFini');
  },

  'fastGpioDigitalWrite': function() {
    handle.funcReq(io.fastGpioDigitalWrite, arguments, 'fastGpioDigitalWrite');
  },

  'fastGpioDigitalWriteDestructive': function() {
    handle.funcReq(io.fastGpioDigitalWriteDestructive, arguments, 'fastGpioDigitalWriteDestructive');
  },

  'fastGpioDigitalLatch': function() {
    handle.funcReq(io.fastGpioDigitalLatch, arguments, 'fastGpioDigitalLatch');
  },

  /****************************************
             OSAbstract_norm
  ****************************************/

  'initWithTty': function() {
    handle.funcReq(io.initWithTty, arguments, 'initWithTty');
  },

  /****************************************
             version_export
  ****************************************/

  'version_addon': function() {
    handle.funcReq(io.version_addon, arguments, 'version_addon');
  },

  /****************************************
             UtilTime
  ****************************************/

  'millis': function() {
    handle.funcReq(io.millis, arguments, 'millis');
  },

  'micros': function() {
    handle.funcReq(io.micros, arguments, 'micros');
  },

  'delay': function() {
    handle.funcReq(io.delay, arguments, 'delay');
  },

  'delayMicroseconds': function() {
    handle.funcReq(io.delayMicroseconds, arguments, 'delayMicroseconds');
  },

  /****************************************
             variant_norm
  ****************************************/

  'muxSelectDigitalPin': function() {
    handle.funcReq(io.muxSelectDigitalPin, arguments, 'muxSelectDigitalPin');
  },

  'muxSelectAnalogPin': function() {
    handle.funcReq(io.muxSelectAnalogPin, arguments, 'muxSelectAnalogPin');
  },

  'muxSelectUart': function() {
    handle.funcReq(io.muxSelectUart, arguments, 'muxSelectUart');
  },

  'muxSelectSpi': function() {
    handle.funcReq(io.muxSelectSpi, arguments, 'muxSelectSpi');
  },

  'muxSelectI2c': function() {
    handle.funcReq(io.muxSelectI2c, arguments, 'muxSelectI2c');
  },

  'variantPinMode': function() {
    handle.funcReq(io.variantPinMode, arguments, 'variantPinMode');
  },

  'variantPinModeIRQ': function() {
    handle.funcReq(io.variantPinModeIRQ, arguments, 'variantPinModeIRQ');
  },

  'turnOffPWM': function() {
    handle.funcReq(io.turnOffPWM, arguments, 'turnOffPWM');
  },

  'turnOnPWM': function() {
    handle.funcReq(io.turnOnPWM, arguments, 'turnOnPWM');
  },

  'variantEnableFastGpio': function() {
    handle.funcReq(io.variantEnableFastGpio, arguments, 'variantEnableFastGpio');
  },

  'variantEnablePullup': function() {
    handle.funcReq(io.variantEnablePullup, arguments, 'variantEnablePullup');
  },

  /****************************************
             pin_map_norm
  ****************************************/

  /****************************************
             Arduino
  ****************************************/

  /****************************************
             Servo
  ****************************************/

  'Servo': function() {
    handle.classReq(io.Servo, arguments, 'Servo');
  },

  'Servo.attach': function() {
    handle.classMethodReq(arguments, 'Servo', 'attach');
  },

  'Servo.detach': function() {
    handle.classMethodReq(arguments, 'Servo', 'detach');
  },

  'Servo.write': function() {
    handle.classMethodReq(arguments, 'Servo', 'write');
  },

  'Servo.writeMicroseconds': function() {
    handle.classMethodReq(arguments, 'Servo', 'writeMicroseconds');
  },

  'Servo.read': function() {
    handle.classMethodReq(arguments, 'Servo', 'read');
  },

  'Servo.readMicroseconds': function() {
    handle.classMethodReq(arguments, 'Servo', 'readMicroseconds');
  },

  'Servo.attached': function() {
    handle.classMethodReq(arguments, 'Servo', 'attached');
  },

  'Servo.set48hz': function() {
    handle.classMethodReq(arguments, 'Servo', 'set48hz');
  },

  'Servo.set188hz': function() {
    handle.classMethodReq(arguments, 'Servo', 'set188hz');
  },
