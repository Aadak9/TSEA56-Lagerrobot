/*
 * main.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include <stdio.h>
#include "init.c"
#include "convert.c"

int indata = 0;
int dist = 0;
int sensorValues[11] = {};
int data = 0;
int test = 0;



void read_reflex()
{
	int i;
	uint8_t indata_digital = 0;
	int indata = 0;
	
	for(i = 0; i < 11; i++)
	{
		
		PORTA &= 0xF0;									// Nollställer de fyra sista bitarna i PORT A 
		PORTA |= i;										// Sätter Muxen till index i
		PORTA |= 0x10;									// Startar sensorn
		
		indata_digital = AD_convert();
		PORTA &= 0xEF;									// Stänger av sensorn
	//	indata = indata_digitaconvert_uint8_t(indata_digital);
		
		sensorValues[i] = indata;
		
		test =2;
		
	}
	
//	return sensorValues;
}

int main()
{
	init_interrupt();
	
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
		read_reflex();
		// SEND REFLEX
	}
}


//PORTB = sensorValues;

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