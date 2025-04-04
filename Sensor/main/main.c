/*
 * main.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include <stdio.h>
#include "init.h"
#include "convert.h"


int dist = 0;
int sum = 0;
int data = 0;
int test = 0;
int indata_volt = 0;



void read_reflex()
{
	int i;
	uint8_t indata_digital;
	int indata_t = 0;
	sum = 0;
	
	for(i = 0; i < 11; i++)
	{
		
		PORTA &= 0xF0;									// Nollställer de fyra sista bitarna i PORT A 
		PORTA |= i;										// Sätter Muxen till index i
		PORTA |= 0x10;									// Startar sensorn
		
		indata_digital = AD_convert();
		PORTA &= 0xEF;									// Stänger av sensorn
		
		indata_t = convert_uint8_t(indata_digital);
		indata_volt = line_to_volt(indata_t);
		sum += indata_volt;
	}
	test = sum;
}

int main()
{
//	init_interrupt();
	
	DDRD |= 0x04;
	PORTD &= 1;
	
	sei();
	
	while (1)
	{
		//		init_IR();
		// READ IR
		// SEND IR
		
		//		init_gyro();
		// READ GYRO
		// SEND GYRO
		
		init_reflex();
		read_reflex();
		// SEND REFLEX
	}
}



/*
PORTB = indata_bin;
indata = convert_uint8_t(indata_bin);
dist = volt_to_dist(indata);
sei();





ISR(INT0_vect)
{
	ADCSRA |= (1 << ADSC);
}


ISR(ADC_vect)
{
	uint8_t indata_binary = ADCH;
}


*/