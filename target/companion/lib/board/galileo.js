
(function(exports, global) {

/*********************************************
Generated with autogen tool
*********************************************/

var Board = function(options) {

  submit = options.submit;
  
  var self = this;
  
  self.submit = options.submit;
  
  self.config  = function(options) {
    submit.config(options);
  };
  

/****************************************
           fast_gpio_sc
****************************************/

  self.fastGpioSCInit = function() {
    return self.submit.funcReq('fastGpioSCInit', arguments);
  };

  self.fastGpioSCFini = function() {
    return self.submit.funcReq('fastGpioSCFini', arguments);
  };

  self.fastGpioDigitalWrite = function() {
    return self.submit.funcReq('fastGpioDigitalWrite', arguments);
  };

  self.fastGpioDigitalWriteDestructive = function() {
    return self.submit.funcReq('fastGpioDigitalWriteDestructive', arguments);
  };

  self.fastGpioDigitalLatch = function() {
    return self.submit.funcReq('fastGpioDigitalLatch', arguments);
  };

/****************************************
           pin_map_norm
****************************************/

  self.A0 = 0xE;

  self.A1 = 0xF;

  self.A2 = 0x10;

  self.A3 = 0x11;

  self.A4 = 0x12;

  self.A5 = 0x13;

  self.A6 = 0x14;

  self.A7 = 0x15;

/****************************************
           Arduino
****************************************/

  self.INPUT = 0x00;

  self.OUTPUT = 0x01;

  self.INPUT_PULLUP = 0x02;

  self.OUTPUT_FAST = 0x03;

  self.INPUT_FAST = 0x04;

  self.DEFAULT = 0;

  self.true = 0x1;

  self.false = 0x0;

  self.DEG_TO_RAD = 0.017453292519943295769236907684886;

  self.RAD_TO_DEG = 57.295779513082320876798154814105;

  self.SERIAL = 0x0;

  self.DISPLAY = 0x1;

  self.LSBFIRST = 0;

  self.MSBFIRST = 1;

  self.PA = 1;

  self.PB = 2;

  self.PC = 3;

  self.PD = 4;

  self.PE = 5;

  self.PF = 6;

  self.PG = 7;

  self.PH = 8;

  self.PJ = 10;

  self.PK = 11;

  self.PL = 12;

/****************************************
           Servo
****************************************/
  
  Servo = function() {
    return self.submit.classReq('Servo', arguments, this);
  };
  
  Servo.prototype.attach = function() {
    return self.submit.classMethodReq('Servo', 'attach', arguments, this);
  };
  
  Servo.prototype.detach = function() {
    return self.submit.classMethodReq('Servo', 'detach', arguments, this);
  };
  
  Servo.prototype.write = function() {
    return self.submit.classMethodReq('Servo', 'write', arguments, this);
  };
  
  Servo.prototype.writeMicroseconds = function() {
    return self.submit.classMethodReq('Servo', 'writeMicroseconds', arguments, this);
  };
  
  Servo.prototype.read = function() {
    return self.submit.classMethodReq('Servo', 'read', arguments, this);
  };
  
  Servo.prototype.readMicroseconds = function() {
    return self.submit.classMethodReq('Servo', 'readMicroseconds', arguments, this);
  };
  
  Servo.prototype.attached = function() {
    return self.submit.classMethodReq('Servo', 'attached', arguments, this);
  };
  
  Servo.prototype.set48hz = function() {
    return self.submit.classMethodReq('Servo', 'set48hz', arguments, this);
  };
  
  Servo.prototype.set188hz = function() {
    return self.submit.classMethodReq('Servo', 'set188hz', arguments, this);
  };
  
  self.Servo = Servo;

  self.MIN_ANGLE = 0;

  self.MAX_ANGLE = 180;

  self.MIN_PULSE_WIDTH = 544;

  self.MAX_PULSE_WIDTH = 2000;

  self.DEFAULT_PULSE_WIDTH = 1500;

  self.INVALID_SERVO = 255;

  self.GPORT0_BIT4_PWM7 = 0x10;

  self.GPORT0_BIT1_PWM5 = 0x02;

  self.GPORT1_BIT0_PWM6 = 0xff;

  self.GPORT0_BIT3_PWM1 = 0x08;

  self.GPORT0_BIT0_PWM7 = 0x01;

  self.GPORT1_BIT1_PWM4 = 0xff;

  self.CYPRESS_I2C_ADDRESS = 0x20;

  self.MAX_NUMBER_OF_SERVOS = 6;

  self.MY_TRACE_PREFIX = "ServoX86Lib";

/****************************************
           OSAbstract_norm
****************************************/

  self.initWithTty = function() {
    return self.submit.funcReq('initWithTty', arguments);
  };

/****************************************
           pins_arduino
****************************************/

  self.NUM_DIGITAL_PINS = 20;

  self.NUM_ANALOG_INPUTS = 6;

  self.NUM_UARTS = 0x03;

  self.NUM_SPI = 0x02;

  self.NUM_I2C = 0x01;

/****************************************
           wiring_digital_norm
****************************************/

  self.HIGH = 0x1;

  self.LOW = 0x0;

  self.NONE = 0xFFFFFFFF;

  self.FN_GPIO_FIXED_OUTPUT = 0x02;

  self.FN_GPIO_OPENDRAIN = 0x04;

  self.FN_PWM = 0x08;

  self.FN_I2C = 0x10;

  self.FN_ANALOG = 0x20;

  self.FN_UART = 0x40;

  self.FN_SPI = 0x80;

  self.FN_PULLUP = 0x100;

  self.FN_MUX = 0x200;

  self.FN_RESERVED = 0x400;

  self.GPIO_DRIVE_PULLUP = 0;

  self.GPIO_DRIVE_STRONG = 1;

  self.GPIO_DRIVE_HIZ = 2;

  self.PIN_EINVAL = 0xFFFFFFFF;

  self.MAX_GPIO_PATH = 0x200;

  self.pinInit = function() {
    return self.submit.funcReq('pinInit', arguments);
  };

  self.pinMode = function() {
    return self.submit.funcReq('pinMode', arguments);
  };

  self.pinModeIRQ = function() {
    return self.submit.funcReq('pinModeIRQ', arguments);
  };

  self.digitalWrite = function() {
    return self.submit.funcReq('digitalWrite', arguments);
  };

  self.digitalRead = function() {
    return self.submit.funcReq('digitalRead', arguments);
  };

  self.pinHandleReopen = function() {
    return self.submit.funcReq('pinHandleReopen', arguments);
  };

  self.pinGetIndex = function() {
    return self.submit.funcReq('pinGetIndex', arguments);
  };

  self.pin2path = function() {
    return self.submit.funcReq('pin2path', arguments);
  };

  self.gpio2gpiohandle = function() {
    return self.submit.funcReq('gpio2gpiohandle', arguments);
  };

  self.pin2gpiohandle = function() {
    return self.submit.funcReq('pin2gpiohandle', arguments);
  };

/****************************************
           AnalogIO
****************************************/

  self.pwmInit = function() {
    return self.submit.funcReq('pwmInit', arguments);
  };

  self.analogRead = function() {
    return self.submit.funcReq('analogRead', arguments);
  };

  self.analogReadResolution = function() {
    return self.submit.funcReq('analogReadResolution', arguments);
  };

  self.analogReference = function() {
    return self.submit.funcReq('analogReference', arguments);
  };

  self.analogWrite = function() {
    return self.submit.funcReq('analogWrite', arguments);
  };

  self.pin2pwmhandle_enable = function() {
    return self.submit.funcReq('pin2pwmhandle_enable', arguments);
  };

/****************************************
           sysfs
****************************************/

  self.sysfsPwmExport = function() {
    return self.submit.funcReq('sysfsPwmExport', arguments);
  };

  self.sysfsPwmEnable = function() {
    return self.submit.funcReq('sysfsPwmEnable', arguments);
  };

  self.sysfsPwmDisable = function() {
    return self.submit.funcReq('sysfsPwmDisable', arguments);
  };

  self.sysfsGpioSet = function() {
    return self.submit.funcReq('sysfsGpioSet', arguments);
  };

  self.sysfsGpioGet = function() {
    return self.submit.funcReq('sysfsGpioGet', arguments);
  };

  self.sysfsGpioExport = function() {
    return self.submit.funcReq('sysfsGpioExport', arguments);
  };

  self.sysfsGpioDirection = function() {
    return self.submit.funcReq('sysfsGpioDirection', arguments);
  };

  self.sysfsGpioEdgeConfig = function() {
    return self.submit.funcReq('sysfsGpioEdgeConfig', arguments);
  };

  self.sysfsGpioLevelConfig = function() {
    return self.submit.funcReq('sysfsGpioLevelConfig', arguments);
  };

  self.sysfsGpioSetDrive = function() {
    return self.submit.funcReq('sysfsGpioSetDrive', arguments);
  };

/****************************************
           i2c
****************************************/

  self.i2c_getadapter = function() {
    return self.submit.funcReq('i2c_getadapter', arguments);
  };

  self.i2c_openadapter = function() {
    return self.submit.funcReq('i2c_openadapter', arguments);
  };

  self.i2c_setslave = function() {
    return self.submit.funcReq('i2c_setslave', arguments);
  };

  self.i2c_writebyte = function() {
    return self.submit.funcReq('i2c_writebyte', arguments);
  };

  self.i2c_writebytes = function() {
    return self.submit.funcReq('i2c_writebytes', arguments);
  };

  self.i2c_readbyte = function() {
    return self.submit.funcReq('i2c_readbyte', arguments);
  };

  self.i2c_readbytes = function() {
    return self.submit.funcReq('i2c_readbytes', arguments);
  };

  self.i2c_readwrite = function() {
    return self.submit.funcReq('i2c_readwrite', arguments);
  };

  self.i2c_add_to_buf = function() {
    return self.submit.funcReq('i2c_add_to_buf', arguments);
  };

/****************************************
           version
****************************************/

  self.version = function() {
    return self.submit.funcReq('version', arguments);
  };

/****************************************
           variant_norm
****************************************/

  self.LINUX_BOOTLOADER_TTY = "/dev/ttyGS0";

  self.LINUX_SPIDEV = "/dev/spidev1.0";

  self.LINUX_EEPROM = "/sys/bus/i2c/devices/0-0050/eeprom";

  self.LINUX_ADC_FMT = "/sys/bus/iio/devices/iio:device0/in_voltage%d_raw";

  self.PLATFORM_ID = 0x06;

  self.ADC_RESOLUTION = 12;

  self.MAX_VARIANT_HPET_FREQ_HZ = 1000;

  self.MUX_SEL_NONE = -1;

  self.MUX_SEL_UART0_RXD = 0;

  self.MUX_SEL_UART0_TXD = 1;

  self.MUX_SEL_SPI1_SS_B = 10;

  self.MUX_SEL_SPI1_MOSI = 11;

  self.MUX_SEL_SPI1_MISO = 12;

  self.MUX_SEL_SPI1_SCK = 13;

  self.MUX_SEL_AD7298_VIN0 = 14;

  self.MUX_SEL_AD7298_VIN1 = 15;

  self.MUX_SEL_AD7298_VIN2 = 16;

  self.MUX_SEL_AD7298_VIN3 = 17;

  self.MUX_SEL_AD7298_VIN4 = 18;

  self.MUX_SEL_AD7298_VIN5 = 19;

  self.MUX_SEL_I2C = 18;

  self.MUX_DEPTH_DIGITAL = 0x02;

  self.MUX_DEPTH_ANALOG = 0x01;

  self.MUX_DEPTH_UART = 0x02;

  self.MUX_DEPTH_SPI = 0x03;

  self.MUX_DEPTH_I2C = 0x01;

  self.GPIO_TOTAL = 56;

  self.GPIO_FAST_IO2 = 0x40;

  self.GPIO_FAST_IO3 = 0x80;

  self.muxSelectDigitalPin = function() {
    return self.submit.funcReq('muxSelectDigitalPin', arguments);
  };

  self.muxSelectAnalogPin = function() {
    return self.submit.funcReq('muxSelectAnalogPin', arguments);
  };

  self.muxSelectUart = function() {
    return self.submit.funcReq('muxSelectUart', arguments);
  };

  self.muxSelectSpi = function() {
    return self.submit.funcReq('muxSelectSpi', arguments);
  };

  self.muxSelectI2c = function() {
    return self.submit.funcReq('muxSelectI2c', arguments);
  };

  self.variantPinMode = function() {
    return self.submit.funcReq('variantPinMode', arguments);
  };

  self.variantPinModeIRQ = function() {
    return self.submit.funcReq('variantPinModeIRQ', arguments);
  };

  self.turnOffPWM = function() {
    return self.submit.funcReq('turnOffPWM', arguments);
  };

  self.turnOnPWM = function() {
    return self.submit.funcReq('turnOnPWM', arguments);
  };

  self.variantEnableFastGpio = function() {
    return self.submit.funcReq('variantEnableFastGpio', arguments);
  };

  self.variantEnablePullup = function() {
    return self.submit.funcReq('variantEnablePullup', arguments);
  };


}; //end of Board class declare

exports.Board = Board;

})(typeof exports === 'object'? exports: this.IOLIB, this.IOLIB);
