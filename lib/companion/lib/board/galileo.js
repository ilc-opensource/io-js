
(function(exports, global) {

/*********************************************
Generated with autogen tool
*********************************************/

var submit = undefined;

var Board = function(options) {
  var Submit;
  if(typeof require === 'function' && typeof module === 'object') {
    Submit = require(options.submitPath).Submit;
  } else {
    Submit = global.Submit;
  }

  submit = new Submit(options);

};

exports.Board = Board;

Board.prototype.config = function(options) {
  submit.config(options);
};


/****************************************
           AnalogIO
****************************************/

Board.prototype.pwmInit = function() {
  return submit.funcReq('pwmInit', arguments);
};

Board.prototype.analogRead = function() {
  return submit.funcReq('analogRead', arguments);
};

Board.prototype.analogReadResolution = function() {
  return submit.funcReq('analogReadResolution', arguments);
};

Board.prototype.analogReference = function() {
  return submit.funcReq('analogReference', arguments);
};

Board.prototype.analogWrite = function() {
  return submit.funcReq('analogWrite', arguments);
};

Board.prototype.pin2pwmhandle_enable = function() {
  return submit.funcReq('pin2pwmhandle_enable', arguments);
};

/****************************************
           i2c
****************************************/

Board.prototype.i2c_getadapter = function() {
  return submit.funcReq('i2c_getadapter', arguments);
};

Board.prototype.i2c_openadapter = function() {
  return submit.funcReq('i2c_openadapter', arguments);
};

Board.prototype.i2c_setslave = function() {
  return submit.funcReq('i2c_setslave', arguments);
};

Board.prototype.i2c_writebyte = function() {
  return submit.funcReq('i2c_writebyte', arguments);
};

Board.prototype.i2c_writebytes = function() {
  return submit.funcReq('i2c_writebytes', arguments);
};

Board.prototype.i2c_readbyte = function() {
  return submit.funcReq('i2c_readbyte', arguments);
};

Board.prototype.i2c_readbytes = function() {
  return submit.funcReq('i2c_readbytes', arguments);
};

Board.prototype.i2c_readwrite = function() {
  return submit.funcReq('i2c_readwrite', arguments);
};

Board.prototype.i2c_add_to_buf = function() {
  return submit.funcReq('i2c_add_to_buf', arguments);
};

/****************************************
           pins_arduino
****************************************/

Board.prototype.NUM_DIGITAL_PINS = 20;

Board.prototype.NUM_ANALOG_INPUTS = 6;

Board.prototype.NUM_UARTS = 0x03;

Board.prototype.NUM_SPI = 0x02;

Board.prototype.NUM_I2C = 0x01;

/****************************************
           version
****************************************/

Board.prototype.version = function() {
  return submit.funcReq('version', arguments);
};

/****************************************
           wiring_digital_norm
****************************************/

Board.prototype.HIGH = 0x1;

Board.prototype.LOW = 0x0;

Board.prototype.NONE = 0xFFFFFFFF;

Board.prototype.FN_GPIO_FIXED_OUTPUT = 0x02;

Board.prototype.FN_GPIO_OPENDRAIN = 0x04;

Board.prototype.FN_PWM = 0x08;

Board.prototype.FN_I2C = 0x10;

Board.prototype.FN_ANALOG = 0x20;

Board.prototype.FN_UART = 0x40;

Board.prototype.FN_SPI = 0x80;

Board.prototype.FN_PULLUP = 0x100;

Board.prototype.FN_MUX = 0x200;

Board.prototype.FN_RESERVED = 0x400;

Board.prototype.GPIO_DRIVE_PULLUP = 0;

Board.prototype.GPIO_DRIVE_STRONG = 1;

Board.prototype.GPIO_DRIVE_HIZ = 2;

Board.prototype.PIN_EINVAL = 0xFFFFFFFF;

Board.prototype.MAX_GPIO_PATH = 0x200;

Board.prototype.pinInit = function() {
  return submit.funcReq('pinInit', arguments);
};

Board.prototype.pinMode = function() {
  return submit.funcReq('pinMode', arguments);
};

Board.prototype.pinModeIRQ = function() {
  return submit.funcReq('pinModeIRQ', arguments);
};

Board.prototype.digitalWrite = function() {
  return submit.funcReq('digitalWrite', arguments);
};

Board.prototype.digitalRead = function() {
  return submit.funcReq('digitalRead', arguments);
};

Board.prototype.pinHandleReopen = function() {
  return submit.funcReq('pinHandleReopen', arguments);
};

Board.prototype.pinGetIndex = function() {
  return submit.funcReq('pinGetIndex', arguments);
};

Board.prototype.pin2path = function() {
  return submit.funcReq('pin2path', arguments);
};

Board.prototype.gpio2gpiohandle = function() {
  return submit.funcReq('gpio2gpiohandle', arguments);
};

Board.prototype.pin2gpiohandle = function() {
  return submit.funcReq('pin2gpiohandle', arguments);
};

/****************************************
           sysfs
****************************************/

Board.prototype.sysfsPwmExport = function() {
  return submit.funcReq('sysfsPwmExport', arguments);
};

Board.prototype.sysfsPwmEnable = function() {
  return submit.funcReq('sysfsPwmEnable', arguments);
};

Board.prototype.sysfsPwmDisable = function() {
  return submit.funcReq('sysfsPwmDisable', arguments);
};

Board.prototype.sysfsGpioSet = function() {
  return submit.funcReq('sysfsGpioSet', arguments);
};

Board.prototype.sysfsGpioGet = function() {
  return submit.funcReq('sysfsGpioGet', arguments);
};

Board.prototype.sysfsGpioExport = function() {
  return submit.funcReq('sysfsGpioExport', arguments);
};

Board.prototype.sysfsGpioDirection = function() {
  return submit.funcReq('sysfsGpioDirection', arguments);
};

Board.prototype.sysfsGpioEdgeConfig = function() {
  return submit.funcReq('sysfsGpioEdgeConfig', arguments);
};

Board.prototype.sysfsGpioLevelConfig = function() {
  return submit.funcReq('sysfsGpioLevelConfig', arguments);
};

Board.prototype.sysfsGpioSetDrive = function() {
  return submit.funcReq('sysfsGpioSetDrive', arguments);
};

/****************************************
           fast_gpio_sc
****************************************/

Board.prototype.fastGpioSCInit = function() {
  return submit.funcReq('fastGpioSCInit', arguments);
};

Board.prototype.fastGpioSCFini = function() {
  return submit.funcReq('fastGpioSCFini', arguments);
};

Board.prototype.fastGpioDigitalWrite = function() {
  return submit.funcReq('fastGpioDigitalWrite', arguments);
};

Board.prototype.fastGpioDigitalWriteDestructive = function() {
  return submit.funcReq('fastGpioDigitalWriteDestructive', arguments);
};

Board.prototype.fastGpioDigitalLatch = function() {
  return submit.funcReq('fastGpioDigitalLatch', arguments);
};

/****************************************
           OSAbstract_norm
****************************************/

Board.prototype.initWithTty = function() {
  return submit.funcReq('initWithTty', arguments);
};

/****************************************
           version_export
****************************************/

Board.prototype.version_addon = function() {
  return submit.funcReq('version_addon', arguments);
};

/****************************************
           UtilTime
****************************************/

Board.prototype.millis = function() {
  return submit.funcReq('millis', arguments);
};

Board.prototype.micros = function() {
  return submit.funcReq('micros', arguments);
};

Board.prototype.delay = function() {
  return submit.funcReq('delay', arguments);
};

Board.prototype.delayMicroseconds = function() {
  return submit.funcReq('delayMicroseconds', arguments);
};

/****************************************
           variant_norm
****************************************/

Board.prototype.LINUX_BOOTLOADER_TTY = "/dev/ttyGS0";

Board.prototype.LINUX_SPIDEV = "/dev/spidev1.0";

Board.prototype.LINUX_EEPROM = "/sys/bus/i2c/devices/0-0050/eeprom";

Board.prototype.LINUX_ADC_FMT = "/sys/bus/iio/devices/iio:device0/in_voltage%d_raw";

Board.prototype.PLATFORM_ID = 0x06;

Board.prototype.ADC_RESOLUTION = 12;

Board.prototype.MAX_VARIANT_HPET_FREQ_HZ = 1000;

Board.prototype.MUX_SEL_NONE = -1;

Board.prototype.MUX_SEL_UART0_RXD = 0;

Board.prototype.MUX_SEL_UART0_TXD = 1;

Board.prototype.MUX_SEL_SPI1_SS_B = 10;

Board.prototype.MUX_SEL_SPI1_MOSI = 11;

Board.prototype.MUX_SEL_SPI1_MISO = 12;

Board.prototype.MUX_SEL_SPI1_SCK = 13;

Board.prototype.MUX_SEL_AD7298_VIN0 = 14;

Board.prototype.MUX_SEL_AD7298_VIN1 = 15;

Board.prototype.MUX_SEL_AD7298_VIN2 = 16;

Board.prototype.MUX_SEL_AD7298_VIN3 = 17;

Board.prototype.MUX_SEL_AD7298_VIN4 = 18;

Board.prototype.MUX_SEL_AD7298_VIN5 = 19;

Board.prototype.MUX_SEL_I2C = 18;

Board.prototype.MUX_DEPTH_DIGITAL = 0x02;

Board.prototype.MUX_DEPTH_ANALOG = 0x01;

Board.prototype.MUX_DEPTH_UART = 0x02;

Board.prototype.MUX_DEPTH_SPI = 0x03;

Board.prototype.MUX_DEPTH_I2C = 0x01;

Board.prototype.GPIO_TOTAL = 56;

Board.prototype.GPIO_FAST_IO2 = 0x40;

Board.prototype.GPIO_FAST_IO3 = 0x80;

Board.prototype.muxSelectDigitalPin = function() {
  return submit.funcReq('muxSelectDigitalPin', arguments);
};

Board.prototype.muxSelectAnalogPin = function() {
  return submit.funcReq('muxSelectAnalogPin', arguments);
};

Board.prototype.muxSelectUart = function() {
  return submit.funcReq('muxSelectUart', arguments);
};

Board.prototype.muxSelectSpi = function() {
  return submit.funcReq('muxSelectSpi', arguments);
};

Board.prototype.muxSelectI2c = function() {
  return submit.funcReq('muxSelectI2c', arguments);
};

Board.prototype.variantPinMode = function() {
  return submit.funcReq('variantPinMode', arguments);
};

Board.prototype.variantPinModeIRQ = function() {
  return submit.funcReq('variantPinModeIRQ', arguments);
};

Board.prototype.turnOffPWM = function() {
  return submit.funcReq('turnOffPWM', arguments);
};

Board.prototype.turnOnPWM = function() {
  return submit.funcReq('turnOnPWM', arguments);
};

Board.prototype.variantEnableFastGpio = function() {
  return submit.funcReq('variantEnableFastGpio', arguments);
};

Board.prototype.variantEnablePullup = function() {
  return submit.funcReq('variantEnablePullup', arguments);
};

/****************************************
           pin_map_norm
****************************************/

Board.prototype.A0 = 0xE;

Board.prototype.A1 = 0xF;

Board.prototype.A2 = 0x10;

Board.prototype.A3 = 0x11;

Board.prototype.A4 = 0x12;

Board.prototype.A5 = 0x13;

Board.prototype.A6 = 0x14;

Board.prototype.A7 = 0x15;

/****************************************
           Arduino
****************************************/

Board.prototype.INPUT = 0x00;

Board.prototype.OUTPUT = 0x01;

Board.prototype.INPUT_PULLUP = 0x02;

Board.prototype.OUTPUT_FAST = 0x03;

Board.prototype.INPUT_FAST = 0x04;

Board.prototype.DEFAULT = 0;

Board.prototype.true = 0x1;

Board.prototype.false = 0x0;

Board.prototype.DEG_TO_RAD = 0.017453292519943295769236907684886;

Board.prototype.RAD_TO_DEG = 57.295779513082320876798154814105;

Board.prototype.SERIAL = 0x0;

Board.prototype.DISPLAY = 0x1;

Board.prototype.LSBFIRST = 0;

Board.prototype.MSBFIRST = 1;

Board.prototype.PA = 1;

Board.prototype.PB = 2;

Board.prototype.PC = 3;

Board.prototype.PD = 4;

Board.prototype.PE = 5;

Board.prototype.PF = 6;

Board.prototype.PG = 7;

Board.prototype.PH = 8;

Board.prototype.PJ = 10;

Board.prototype.PK = 11;

Board.prototype.PL = 12;

/****************************************
           Servo
****************************************/

Servo = function() {
  return submit.classReq('Servo', arguments, this);
};

Servo.prototype.attach = function() {
  return submit.classMethodReq('Servo', 'attach', arguments, this);
};

Servo.prototype.detach = function() {
  return submit.classMethodReq('Servo', 'detach', arguments, this);
};

Servo.prototype.write = function() {
  return submit.classMethodReq('Servo', 'write', arguments, this);
};

Servo.prototype.writeMicroseconds = function() {
  return submit.classMethodReq('Servo', 'writeMicroseconds', arguments, this);
};

Servo.prototype.read = function() {
  return submit.classMethodReq('Servo', 'read', arguments, this);
};

Servo.prototype.readMicroseconds = function() {
  return submit.classMethodReq('Servo', 'readMicroseconds', arguments, this);
};

Servo.prototype.attached = function() {
  return submit.classMethodReq('Servo', 'attached', arguments, this);
};

Servo.prototype.set48hz = function() {
  return submit.classMethodReq('Servo', 'set48hz', arguments, this);
};

Servo.prototype.set188hz = function() {
  return submit.classMethodReq('Servo', 'set188hz', arguments, this);
};

Board.prototype.Servo = Servo;

Board.prototype.MIN_ANGLE = 0;

Board.prototype.MAX_ANGLE = 180;

Board.prototype.MIN_PULSE_WIDTH = 544;

Board.prototype.MAX_PULSE_WIDTH = 2000;

Board.prototype.DEFAULT_PULSE_WIDTH = 1500;

Board.prototype.INVALID_SERVO = 255;

Board.prototype.GPORT0_BIT4_PWM7 = 0x10;

Board.prototype.GPORT0_BIT1_PWM5 = 0x02;

Board.prototype.GPORT1_BIT0_PWM6 = 0xff;

Board.prototype.GPORT0_BIT3_PWM1 = 0x08;

Board.prototype.GPORT0_BIT0_PWM7 = 0x01;

Board.prototype.GPORT1_BIT1_PWM4 = 0xff;

Board.prototype.CYPRESS_I2C_ADDRESS = 0x20;

Board.prototype.MAX_NUMBER_OF_SERVOS = 6;

Board.prototype.MY_TRACE_PREFIX = "ServoX86Lib";

})(typeof exports === 'object'? exports: this, this);
