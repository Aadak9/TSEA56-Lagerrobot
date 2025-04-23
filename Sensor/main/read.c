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

int8_t read_reflex()
{
	int i;
	volatile int8_t data;
	volatile uint8_t indata = 0;
	volatile int sum = 0;
	volatile int sum_index = 0;
	volatile int roadmarkLeft = 0;
	volatile int roadmarkRight = 0;
	volatile int pivot = 0;	
	
	for(i = 0; i < 11; i++)
	{
		PORTA &= 0xF0;									// Nollställer de fyra LSB bitarna i PORT A
		PORTA |= i;										// Sätter Muxen till index i
		PORTA |= 0x10;									// Startar sensorn
		
		 if (i == 0) {
			 is_active_reflex();						// Läs men kasta resultatet
			 _delay_us(20);								//Första läsningen från i = 0 ger fel värde
			 continue;
		 }
		
		indata = is_active_reflex();
		PORTA &= 0xEF;									// Stänger av sensorn
		
		sum += indata;									// 1 eller 0
		sum_index += (i+1)*indata;
		
		if ((i == 0) && (indata == 1)) {
			roadmarkLeft = 1;
		}
		if ((i == 10) && (indata == 1)) {
			roadmarkRight = 1;
		}
	}
	
	if (sum == 0)
	{
		pivot = 6;
	} else {
		pivot = sum_index/sum;
	}

	return data = (int8_t)(pivot + roadmarkLeft*128 + roadmarkRight*64);
}


uint8_t read_IR()
{	
	volatile uint8_t indata_t = AD_convert();
	volatile int distance_cm = linear_interpolation(indata_t);
	return (uint8_t)distance_cm;
}


uint8_t read_gyro()
{		
	volatile int8_t indata = AD_convert() - 129;							// värdet 125 måste kalibreras
	w_int += indata*4;
	w_send = abs(w_int/100);
 	volatile uint8_t w = (uint8_t)w_send;
	return w;
}


void reset_w()
{
	w_int = 0;
}