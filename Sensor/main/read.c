#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "read.h"
#include "convert.h"

volatile float theta;


uint8_t read_reflex()
{
	int i;
	volatile uint8_t data;
	volatile uint8_t indata = 0;
	volatile int sum = 0;
	volatile int sum_index = 0;
	volatile int roadmark = 0;
	volatile int pivot = 0;
	volatile int offset = 0;
	
	for(i = 0; i < 11; i++)
	{
		PORTA &= 0xF0;									// Nollställer de fyra LSB bitarna i PORT A
		PORTA |= i;										// Sätter Muxen till index i
		PORTA |= 0x10;									// Startar sensorn
		
		indata = is_active_reflex();
		PORTA &= 0xEF;									// Stänger av sensorn
		
		sum += indata;
		sum_index += i*indata;
		
	}
	
	roadmark = is_roadmark(sum);						
	
	if (roadmark == 1)									//Starta timer här?
	{
		TCCR1B |=  (1 << CS11) | (1 << CS10);
	}
	
	pivot = sum_index/sum;
	offset = (6 - pivot);
								
	return data = (uint8_t)(roadmark*16 + offset);			//Dela upp i två array, offset negativt problem??
}


uint8_t read_IR()
{
	volatile uint8_t data;
	
	volatile uint8_t indata_t = AD_convert();
	volatile int indata = convert_uint8_t(indata_t);
	volatile int dist = volt_to_dist(indata);
	
	if (dist > 250){									// Förhindrar integer overflow
		return data = 0xFF;
		} else {
		return data = (uint8_t)dist;
	}
}


int read_gyro()
{
	init_gyro();
	volatile float dt = 0.01;
	
	volatile uint8_t indata_t = AD_convert();
	volatile int indata = convert_uint8_t(indata_t);
	volatile float volt = digital_to_volt(indata);
	
	volatile float w_degree = (volt - 2.4)/0.033;
	theta += w_degree*dt;
	
	return theta;
}