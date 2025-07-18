/*
 * read.c
 *
 * Created: 2025-04-03 11:25:46
 * Author : andno773, sigry751
 */

#define F_CPU 16000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include <util/delay.h>
#include "read.h"
#include "convert.h"

volatile int w_int;
volatile int w_send;

int8_t read_line_front(int reflex_high)
{
	int i;
	volatile int8_t data;
	volatile uint8_t indata = 0;
	volatile int sum = 0;
	volatile int sum_index = 0;
	volatile int roadmarkLeft = 0;
	volatile int roadmarkRight = 0;
	volatile int pivot = 0;	
	
	for(i = 1; i < 12; i++)
	{
		PORTA &= 0xF0;														// Resets the 4 LSB bits in PORT A.
		PORTA |= i;															// Set multiplexer to index i.
		PORTD |= 0x20;														// Start sensor.
		

		indata = is_active_reflex(reflex_high);								// 1 if current sensor sees tape, 0 otherwise.
		PORTD &= 0xDF;														// Turn off sensor.
		
		sum += indata;									
		sum_index += (i)*indata;

		if ((i == 1) && (indata == 1)) {									// Sees left turn.
			roadmarkLeft = 1;
		}
		if ((i == 11) && (indata == 1)) {									// Sees right turn.
			roadmarkRight = 1;
		}
	}

	if (sum == 0)															// Sees no tape.
	{
		pivot = 12;
	} else {
		pivot = (sum_index*2)/sum;											// Center of mass calculation, multiply with 2 to get decimals.
	}

	return data = (int8_t)(pivot + roadmarkLeft*128 + roadmarkRight*64);	// Center of mass calculation on bit 0-6, 7 bit for right turn, 8 bit for left turn.
}

int8_t read_line_back(int reflex_high)
{
	int i;
	volatile int8_t data;
	volatile uint8_t indata = 0;
	volatile int sum = 0;
	volatile int sum_index = 0;
	volatile int pivot = 0;	
	
	for(i = 1; i < 12; i++)
	{
		PORTD &= 0xF0;														// Resets the 4 LSB bits in PORT A.
		PORTD |= i;															// Set multiplexer to index i.
		PORTD |= 0x10;														// Start sensor.
		

		indata = is_active_reflex(reflex_high);								// 1 if current sensor sees tape, 0 otherwise.
		PORTD &= 0xEF;														// Turn off sensor.
		
		sum += indata;									
		sum_index += (i)*indata;
	}

	if (sum == 0)															// Sees no tape.
	{
		pivot = 12;
	} else {
		pivot = (sum_index*2)/sum;											// Center of mass calculation, multiply with 2 to get decimals.
	}

	return data = (int8_t)(pivot);											// Center of mass calculation 
}

uint8_t read_IR()
{	
	volatile uint8_t indata_t = AD_convert();
	volatile int distance_cm = linear_interpolation(indata_t);
	return (uint8_t)distance_cm;
}


uint8_t read_gyro()
{			
		volatile int8_t indata = AD_convert() - 126;						// 126 is digital voltage with 0 rotation.
		w_int += indata*4;													// Looses the two MSB, multiply with 4.
		w_send = abs(w_int/100);											// Absolute value to avoid negative numbers over bus, divide by 100 since the value is big.
		volatile uint8_t w = (uint8_t)w_send;
		return w;
}


void reset_w()
{
	w_int = 0;																// Resets w_int after gyro is done.
}

