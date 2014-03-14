/*
 * arduiPIA.h - Arduino Wiring library wrapper
 */
#ifndef _ARDUIPIA_H_
#define _ARDUIPIA_H_

/*********************************************************************
 * INCLUDES
 */

#include <stdint.h>
#include <string.h>
#include "pia_adaptor.h"
#include "pia_device.h"
#include "pia_iolib.h"
#include "pia_arduino_map.h" // Pin mapping

#include "wire/wire.h"

#ifdef __cplusplus
extern "C" {
#endif

/*********************************************************************
 * CONSTANTS
 */
// Pin modes
#define	INPUT           0
#define	OUTPUT          1
#define	INPUT_PULLUP    2
#define	LOW             0
#define	HIGH            1
#define MAX_PWM_LEVEL   4096

// arduino specfic type definition
typedef uint8_t boolean;
typedef uint8_t byte;
typedef uint16_t word;
typedef uint32_t dword;

extern int argc;
extern char **argv;

/*********************************************************************
 * FUNCTIONS
 */

// ArduiPIA Function prototypes

/*
 * arduino internal setup function, called when the first program initialization
 */
extern void setup(void);

/*
 * arduino internal service function, loop service called after setup
 */
extern void loop(void);

// arduino Digital and analog IO interface
extern void pinMode             (int pin, int mode);
extern int  digitalRead         (int pin);
extern void digitalWrite        (int pin, int value);
extern void setPWMFreq          (int pin, int freq);
extern void pwmWrite            (int pin, int value);
extern int  analogRead          (int pin);
extern void analogWrite         (int pin, int value);

//Misc, timing function
extern void delay               (unsigned int msec);

#ifdef __cplusplus
}

#endif // __cplusplus
#endif // _ARDUIPIA_H_

