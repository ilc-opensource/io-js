/*
  Copyright (c) 2011 Arduino.  All right reserved.
  Copyright (c) 2013 Intel Corporation.

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

//////////////////////////// Galileo Fab C ////////////////////////////

#include <Arduino.h>
#include <errno.h>
#include <sysfs.h>
#include "variant.h"

//Bindings to Arduino
#include "RingBuffer.h"
#include "TTYUART.h"

#ifdef __cplusplus
extern "C" {
#endif

/*
 * MUX description
 *
 * TODO handle the interrupt-capable gpios
 */

int mux_sel_analog[NUM_ANALOG_INPUTS];

int mux_sel_uart[NUM_UARTS][MUX_DEPTH_UART];

int  mux_sel_spi[NUM_SPI][MUX_DEPTH_SPI];

#if 0
/*
 * Pins descriptions
 */
PinDescription g_APinDescription[]=
{
  // TODO:
  // ----------------------
  // 0/1 - UART (Serial)
  { 0, 2, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 1, 7, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 2, 4, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 3, 1, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 4, 0, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 5, 15, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 6, 14, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 7, 13, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 8, 12, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 9, 11, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 10, 10, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
  { 13, 3, GPIO_CYPRESS, PINTYPE_OPENDRAIN },
} ;
#endif

// Sorted by Linux GPIO ID
PinDescription g_APinDescription[]=
{
//	gpiolib	alias	fastid	ardid	Inital Mux id		tFixedState,	ptMuxDesc,				MuxCount										type					Handle
	{ 4, 	NONE,	NONE,	2, 	NONE, 				LOW, 			NULL, 					0,												FN_GPIO_OPENDRAIN,		-1 },
	{ 1, 	NONE,	NONE,	3, 	NONE, 				LOW, 			NULL, 					0,												FN_GPIO_OPENDRAIN,		-1 },
	{ 0, 	NONE,	NONE,	4, 	NONE, 				LOW, 			NULL, 					0,												FN_GPIO_OPENDRAIN,		-1 },
	{ 15, 	NONE,	NONE,	5, 	NONE, 				LOW, 			NULL, 					0,												FN_GPIO_OPENDRAIN,		-1 },
	{ 14, 	NONE,	NONE,	6, 	NONE, 				LOW, 			NULL, 					0,												FN_GPIO_OPENDRAIN,		-1 },
	{ 13, 	NONE,	NONE,	7,	NONE, 				LOW, 			NULL, 					0,										 		FN_GPIO_OPENDRAIN,		-1 },
	{ 12, 	NONE,	NONE,	8,	NONE, 				LOW, 			NULL, 					0,										 		FN_GPIO_OPENDRAIN,		-1 },
	{ 11, 	NONE,	NONE,	9, 	NONE, 				LOW, 			NULL,					0,												FN_GPIO_OPENDRAIN,		-1 },
	{ 10, 	NONE,	NONE,	10, 	NONE, 				LOW, 			NULL,					0,												FN_GPIO_OPENDRAIN,		-1 },
	{  3, 	NONE,	NONE,	13, 	NONE, 				LOW, 			NULL,					0,												FN_GPIO_OPENDRAIN,		-1 },
};

uint32_t sizeof_g_APinDescription;
uint32_t ardPin2DescIdx[GPIO_TOTAL];

// Sorted by Linux PWM ID
PwmDescription g_APwmDescription[] = {
};
uint32_t sizeof_g_APwmDescription;

// Sorted Arduino Pin ID
PinState g_APinState[]=
{
	/* Note PWM-capable pins are output by default */
	/* uCurrentPwm	uCurrentInput		*/
	{ 0,		1 },	/* 0		*/
	{ 0,		1 },	/* 1		*/
	{ 0,		1 },	/* 2		*/
	{ 0,		1 },	/* 3		*/
	{ 0,		1 },	/* 4 		*/
	{ 0,		1 },	/* 5	 	*/
	{ 0,		1 },	/* 6		*/
	{ 0,		1 },	/* 7 		*/
	{ 0,		1 },	/* 8 		*/
	{ 0,		1 },	/* 9		*/
	{ 0,		1 },	/* 10		*/
	{ 0,		1 },	/* 11		*/
	{ 0,		1 },	/* 12		*/
	{ 0,		1 },	/* 13		*/
	{ 0,		1 },	/* 14		*/
	{ 0,		1 },	/* 15		*/
	{ 0,		1 },	/* 16		*/
	{ 0,		1 },	/* 17		*/
	{ 0,		1 },	/* 18		*/
	{ 0,		1 },	/* 19		*/
};
uint32_t sizeof_g_APinState;

#ifdef __cplusplus
}
#endif


RingBuffer rx_buffer1;
RingBuffer rx_buffer2;
RingBuffer rx_buffer3;

TTYUARTClass Serial(&rx_buffer1, 0);		// ttyS0
TTYUARTClass Serial1(&rx_buffer2, 1);		// ttyGS0
TTYUARTClass Serial2(&rx_buffer3, 2);		// ttyS1

#if 0
const unsigned mapUnoPinToSoC(uint8_t pin)
{
	if (pin >= NUM_DIGITAL_PINS) {
		return -EINVAL;
	}
	return g_APinDescription[pin].ulPinId;
}

/*
 * Initialise the GPIO for execution.
 *
 * 1. Export all the Izmir's GPIOs to sysfs
 * 2. Initialise default pin routing on Arduino shield
 * 3. TODO reset pin
 *
 * XXX error reporting
 */
static int initGPIO(void)
{
	int i = 0;

	/*
	 * Export all Izmir GPIOs and initialise as input.
	 * Some GPIOs are restricted: let the setup routine fail in this
	 * case.
	 */
	for (i = 0; i < GPIO_TOTAL; i++) {
		sysfsGpioExport(i);
		sysfsGpioDirection(i, 0);
	}

	return 0;
}
#endif

// ----------------------------------------------------------------------------

int variantPinMode(uint8_t pin, uint8_t mode)
{
	return 0;
}

int variantPinModeIRQ(uint8_t pin, uint8_t mode)
{
	return 0;
}

void turnOnPWM(uint8_t pin)
{
}

void turnOffPWM(uint8_t pin)
{
}

void variantEnableFastGpio(int pin)
{
}

void variantEnablePullup(uint8_t pin, int enable)
{
}

void __libc_init_array(void);

#if 0
void init_mux(struct mux_sel ** mux, uint32_t idx, uint32_t jdx)
{
	uint32_t i, j;
	struct mux_sel * pmux = (struct mux_sel*)mux;

	for ( i = 0; i < idx; i++){
		for(j = 0; j <jdx; j++, pmux++){
			pmux->sel_id = MUX_SEL_NONE;
			pmux->sel_val = MUX_SEL_NONE;
		}
	}
}
#endif

void init( int argc, char * argv[] )
{
	// FAB C muxes nothing
	#if 0
	init_mux((struct mux_sel**)&mux_sel_analog, NUM_ANALOG_INPUTS, MUX_DEPTH_ANALOG);
	init_mux((struct mux_sel**)&mux_sel_uart, NUM_UARTS, MUX_DEPTH_UART);
	init_mux((struct mux_sel**)&mux_sel_spi, NUM_SPI, MUX_DEPTH_SPI);
	init_mux((struct mux_sel**)&mux_sel_i2c, NUM_I2C, MUX_DEPTH_I2C);
	#endif

	if(argc > 1)
		if(Serial.init_tty(argv[1]) != 0)
			return;
	if(argc > 2)
		if(Serial1.init_tty(argv[2]) != 0)
			return;
	if(argc > 3)
		if(Serial2.init_tty(argv[3]) != 0)
			return;

	sizeof_g_APinDescription = sizeof(g_APinDescription)/sizeof(struct _PinDescription);
	pinInit();
	sizeof_g_APwmDescription = sizeof(g_APwmDescription)/sizeof(struct _PwmDescription);
	pwmInit();
	sizeof_g_APinState = sizeof(g_APinState)/sizeof(struct _PinState);
}

