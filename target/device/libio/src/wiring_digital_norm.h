#include <variant.h>
#include <wiring_digital.h>

#ifdef IOLIB_OVERRIDE

#ifdef __cplusplus
extern "C" {
#endif

#define HIGH  0x1
#define LOW   0x0

#define NONE					0xFFFFFFFF
#define	FN_GPIO_FIXED_INPUT		0x01
#define FN_GPIO_FIXED_OUTPUT	0x02
#define FN_GPIO_OPENDRAIN		0x04
#define FN_PWM					0x08
#define FN_I2C					0x10
#define FN_ANALOG				0x20
#define FN_UART					0x40
#define FN_SPI					0x80
#define FN_PULLUP				0x100
#define FN_MUX					0x200	// Used to mux functions in/out
#define FN_RESERVED				0x400	// Reserved - not to be touched by sketch layer

#define GPIO_DRIVE_PULLUP			0
#define GPIO_DRIVE_STRONG			1
#define GPIO_DRIVE_HIZ				2

#define PIN_EINVAL 0xFFFFFFFF

#define MAX_GPIO_PATH 0x200

void pinInit(void);
void pinMode(uint8_t pin, uint8_t mode);
int pinModeIRQ(uint8_t pin, int8_t mode);
void digitalWrite(register uint8_t pin, register uint8_t val);
int digitalRead(uint8_t pin);

// interrupt.c dependencies
//int pin2handle(uint8_t pin);
int pinHandleReopen(uint8_t index);
int pinGetIndex(uint8_t pin);
char * pin2path(uint8_t pin);
int gpio2gpiohandle(uint32_t gpio);
int pin2gpiohandle(uint8_t pin);


#ifdef __cplusplus
}
#endif

#endif
 
