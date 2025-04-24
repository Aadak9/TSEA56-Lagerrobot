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

int8_t read_reflex(int reflex_high)
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
		PORTA &= 0xF0;														// Nollställer de fyra LSB bitarna i PORT A.
		PORTA |= i;															// Sätter Muxen till index i.
		PORTA |= 0x10;														// Startar sensorn.
		
		 if (i == 1) {
			 is_active_reflex(reflex_high);									// Läs men kasta resultatet.
			 _delay_us(20);													// Första läsningen från i = 0 ger fel värde.
		 }

		indata = is_active_reflex(reflex_high);								// 1 om aktuell sensor ser tejp, 0 annars.
		PORTA &= 0xEF;														// Stänger av sensorn.
		
		sum += indata;									
		sum_index += (i)*indata;

		if ((i == 0) && (indata == 1)) {									// Ser vänstersväng.
			roadmarkLeft = 1;
		}
		if ((i == 10) && (indata == 1)) {									// Ser högersväng.
			roadmarkRight = 1;
		}
	}

	if (sum == 0)															//Ser ingen tejp.
	{
		pivot = 12;
	} else {
		pivot = (sum_index*2)/sum;											//Tyngdpunktsberäkning, multiplicerar med två för att få decimaler.
	}

	return data = (int8_t)(pivot + roadmarkLeft*128 + roadmarkRight*64);	// Tygndpunktberäkning på bit 0-6, 7 bit för höger, 8 bit för vänster.
}


uint8_t read_IR()
{	
	volatile uint8_t indata_t = AD_convert();
	volatile int distance_cm = linear_interpolation(indata_t);
	return (uint8_t)distance_cm;
}


uint8_t read_gyro()
{		
	volatile int8_t indata = AD_convert() - 129;							// 129 är digitala spänningen vid noll rotation.
	w_int += indata*4;														// Tappar de två minst signifikanta bitar, multiplicerar med 4.
	w_send = abs(w_int/100);												// Absolutbelopp så vi slipper att skicka negativa tal över bussen, delar med 100 för att talet är stort.
 	volatile uint8_t w = (uint8_t)w_send;
	return w;
}


void reset_w()
{
	w_int = 0;																// Återställer w_int efter att gyrot är klar.
}