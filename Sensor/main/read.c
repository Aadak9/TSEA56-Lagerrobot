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
		PORTA &= 0xF0;														// Nollst�ller de fyra LSB bitarna i PORT A.
		PORTA |= i;															// S�tter Muxen till index i.
		PORTA |= 0x10;														// Startar sensorn.
		
		 if (i == 1) {
			 is_active_reflex(reflex_high);									// L�s men kasta resultatet.
			 _delay_us(20);													// F�rsta l�sningen fr�n i = 0 ger fel v�rde.
		 }

		indata = is_active_reflex(reflex_high);								// 1 om aktuell sensor ser tejp, 0 annars.
		PORTA &= 0xEF;														// St�nger av sensorn.
		
		sum += indata;									
		sum_index += (i)*indata;

		if ((i == 0) && (indata == 1)) {									// Ser v�nstersv�ng.
			roadmarkLeft = 1;
		}
		if ((i == 10) && (indata == 1)) {									// Ser h�gersv�ng.
			roadmarkRight = 1;
		}
	}

	if (sum == 0)															//Ser ingen tejp.
	{
		pivot = 12;
	} else {
		pivot = (sum_index*2)/sum;											//Tyngdpunktsber�kning, multiplicerar med tv� f�r att f� decimaler.
	}

	return data = (int8_t)(pivot + roadmarkLeft*128 + roadmarkRight*64);	// Tygndpunktber�kning p� bit 0-6, 7 bit f�r h�ger, 8 bit f�r v�nster.
}


uint8_t read_IR()
{	
	volatile uint8_t indata_t = AD_convert();
	volatile int distance_cm = linear_interpolation(indata_t);
	return (uint8_t)distance_cm;
}


uint8_t read_gyro()
{		
	volatile int8_t indata = AD_convert() - 129;							// 129 �r digitala sp�nningen vid noll rotation.
	w_int += indata*4;														// Tappar de tv� minst signifikanta bitar, multiplicerar med 4.
	w_send = abs(w_int/100);												// Absolutbelopp s� vi slipper att skicka negativa tal �ver bussen, delar med 100 f�r att talet �r stort.
 	volatile uint8_t w = (uint8_t)w_send;
	return w;
}


void reset_w()
{
	w_int = 0;																// �terst�ller w_int efter att gyrot �r klar.
}