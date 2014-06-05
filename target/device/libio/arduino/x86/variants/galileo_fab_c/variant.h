/*
 * Copyright(c) 2013 Intel Corporation. All rights reserved.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of version 2 of the GNU General Public License as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St - Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Contact Information:
 * Intel Corporation
 */

#ifndef __VARIANT_H__
#define __VARIANT_H__

#include <stdint.h>
#include <unistd.h>

#include <AnalogIO.h>
#include <wiring_digital.h>
#include "pins_arduino.h"

#ifdef __cplusplus
extern "C" {
#endif

#ifdef __cplusplus
#include "TTYUART.h"
extern TTYUARTClass Serial;
extern TTYUARTClass Serial1;
extern TTYUARTClass Serial2;
#endif

#define LINUX_BOOTLOADER_TTY		"/dev/ttyGS0"
#define LINUX_SPIDEV			"/dev/spidev1.0"
#define LINUX_EEPROM			"/sys/bus/i2c/devices/0-0050/eeprom"
#define LINUX_ADC_FMT			"/sys/bus/iio/devices/iio:device0/in_voltage%d_raw"
#define PLATFORM_ID			0x03	// Fab C platform id

#define ADC_RESOLUTION			12

#define MAX_VARIANT_HPET_FREQ_HZ	1000

//#define VARIANT_TRACE_LEVEL TRACE_LEVEL_DEBUG	// default trace level
#define VARIANT_TRACE_LEVEL TRACE_LEVEL_INFO	// default trace level

/* Mux selector definition */
struct mux_sel {
	uint32_t sel_id;			// GPIOLib ID
	uint32_t sel_val;
};

/* Mux selects (GPIOLib ID).  Sorted by board pinout.  */
#define MUX_SEL_NONE				-1
#define MUX_SEL_UART0_RXD			40
#define MUX_SEL_UART0_TXD			41
#define MUX_SEL_SPI1_SS_B			42
#define MUX_SEL_SPI1_MOSI			43
#define MUX_SEL_SPI1_MISO			54
#define MUX_SEL_SPI1_SCK			55
#define MUX_SEL_AD7298_VIN0			37
#define MUX_SEL_AD7298_VIN1			36
#define MUX_SEL_AD7298_VIN2			23
#define MUX_SEL_AD7298_VIN3			22
#define MUX_SEL_AD7298_VIN4			21
#define MUX_SEL_AD7298_VIN5			20
#define MUX_SEL_I2C				29

/* Pins table to be instanciated into variant.cpp */

#define MUX_DEPTH_DIGITAL			0x02
#define MUX_DEPTH_ANALOG			0x02
#define MUX_DEPTH_UART				0x02
#define MUX_DEPTH_SPI				0x04
#define MUX_DEPTH_I2C				0x01
#define GPIO_TOTAL				0x10

extern PinDescription g_APinDescription[] ;
extern uint32_t sizeof_g_APinDescription;
extern PwmDescription g_APwmDescription[] ;
extern uint32_t sizeof_g_APwmDescription;
extern uint32_t ardPin2DescIdx[GPIO_TOTAL];
extern PinState g_APinState[] ;
extern uint32_t sizeof_g_APinState;

extern int mux_sel_analog[NUM_ANALOG_INPUTS];
extern int mux_sel_uart[NUM_UARTS][MUX_DEPTH_UART];
extern int mux_sel_spi[NUM_SPI][MUX_DEPTH_SPI];
extern int mux_sel_i2c[NUM_I2C][MUX_DEPTH_I2C];

int muxSelectDigitalPin(uint8_t pin);
int muxSelectAnalogPin(uint8_t pin);
int muxSelectUart(uint8_t interface);
int muxSelectSpi(uint8_t interface);
int muxSelectI2c(uint8_t interface);

const unsigned mapUnoPinToSoC(uint8_t pin);

int variantPinMode(uint8_t pin, uint8_t mode);
int variantPinModeIRQ(uint8_t pin, uint8_t mode);

void turnOnPWM(uint8_t pin);
void turnOffPWM(uint8_t pin);

void variantEnableFastGpio(int pin);

void variantEnablePullup(uint8_t pin, int enable);

#ifdef __cplusplus
}
#endif


#endif /* __VARIANT_H__ */

