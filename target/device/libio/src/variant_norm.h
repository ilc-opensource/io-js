#include <variant.h>

#ifdef IOLIB_OVERRIDE

#define LINUX_BOOTLOADER_TTY		"/dev/ttyGS0"
#define LINUX_SPIDEV			"/dev/spidev1.0"
#define LINUX_EEPROM			"/sys/bus/i2c/devices/0-0050/eeprom"
#define LINUX_ADC_FMT			"/sys/bus/iio/devices/iio:device0/in_voltage%d_raw"
#define PLATFORM_ID			0x06	// Fab D platform id

#define ADC_RESOLUTION			12

#define MAX_VARIANT_HPET_FREQ_HZ	1000

//#define VARIANT_TRACE_LEVEL TRACE_LEVEL_DEBUG	// default trace level
#define VARIANT_TRACE_LEVEL TRACE_LEVEL_INFO	// default trace level

/* Mux selects (Arduino Pin ID).  */
#define MUX_SEL_NONE			-1
#define MUX_SEL_UART0_RXD		 0
#define MUX_SEL_UART0_TXD		 1
#define MUX_SEL_SPI1_SS_B		10
#define MUX_SEL_SPI1_MOSI		11
#define MUX_SEL_SPI1_MISO		12
#define MUX_SEL_SPI1_SCK		13
#define MUX_SEL_AD7298_VIN0		14
#define MUX_SEL_AD7298_VIN1		15
#define MUX_SEL_AD7298_VIN2		16
#define MUX_SEL_AD7298_VIN3		17
#define MUX_SEL_AD7298_VIN4		18
#define MUX_SEL_AD7298_VIN5		19
#define MUX_SEL_I2C			18	// Uses pin 19 as well but this should do

/* Pins table to be instanciated into variant.cpp */

#define MUX_DEPTH_DIGITAL			0x02
#define MUX_DEPTH_ANALOG			0x01
#define MUX_DEPTH_UART				0x02
#define MUX_DEPTH_SPI				0x03
#define MUX_DEPTH_I2C				0x01
#define GPIO_TOTAL				56

#define GPIO_FAST_IO2				0x40
#define GPIO_FAST_IO3				0x80

int muxSelectDigitalPin(uint8_t pin);
int muxSelectAnalogPin(uint8_t pin);
int muxSelectUart(uint8_t interface);
int muxSelectSpi(uint8_t interface);
int muxSelectI2c(uint8_t interface);

//No implementation
//const unsigned mapUnoPinToSoC(uint8_t pin);

int variantPinMode(uint8_t pin, uint8_t mode);
int variantPinModeIRQ(uint8_t pin, uint8_t mode);
void turnOffPWM(uint8_t pin);
void turnOnPWM(uint8_t pin);

void variantEnableFastGpio(int pin);

void variantEnablePullup(uint8_t pin, int enable);

#endif
