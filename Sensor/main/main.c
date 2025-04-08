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

int test = 0;

// Avståndssensor
uint8_t indata_t;
int indata = 0;
int dist = 0;

// Reflexsensor
int array[11];
int sum = 0;


void read_reflex()
{
	int i;
	indata = 0;
	sum = 0;
	
	
	for(i = 0; i < 11; i++)
	{
		PORTA &= 0xF0;									// Nollställer de fyra LSB bitarna i PORT A 
		PORTA |= i;										// Sätter Muxen till index i
		PORTA |= 0x10;									// Startar sensorn
		
		indata = is_active_reflex();
		PORTA &= 0xEF;									// Stänger av sensorn
		
		array[i] = indata;
		sum += indata;
		
	}
	// Lägg till funktion som konverterar array till information om potentiell korsning
}


void read_IR()
{
	indata_t = AD_convert();
	indata = convert_uint8_t(indata_t);
	dist = volt_to_dist(indata);
	// Skicka dist till bussen
}


void read_gyro()
{
	
}


int main()
{
	init_interrupt();	
	sei();
	
	while (1)
	{
		init_IR();
		read_IR();
		// SEND IR
		
		init_gyro();
		read_gyro();
		// SEND GYRO
		
		init_reflex();
		read_reflex();
		// SEND REFLEX
	}
}



/*

	DDRD |= 0x04;	// Aktiverar PORT PD2 för att möjligöra avbrott via att dess PIN aktiveras manuellt
	PORTD &= 1;

ISR(INT0_vect)
{
	ADCSRA |= (1 << ADSC);
}


ISR(ADC_vect) 
{
	uint8_t indata_binary = ADCH;
}

*/