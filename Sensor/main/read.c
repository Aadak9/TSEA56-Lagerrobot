#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "read.h"
#include "convert.h"


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
		
//		if (i == 0 && ) {
			
//		} 
		
	}
	
	roadmarkLeft = is_roadmarkLeft(sum_index);
	roadmarkRight = is_roadmarkRight(sum_index);						
	
	pivot = sum_index/sum;
	offset = (6 - pivot);
								
	return data = (int8_t)(offset);			//Dela upp i två array, offset negativt problem??
}


uint8_t read_IR()
{
	volatile uint8_t data;
	
	volatile uint8_t indata_t = AD_convert();
	volatile int indata = convert_uint8_t(indata_t);
	volatile int is_blocked = dist_table(indata);
	
	return data = (uint8_t)is_blocked;
}


int8_t read_gyro()
{		
	volatile uint8_t indata_t = AD_convert();
	volatile int indata = convert_uint8_t(indata_t);
	volatile int w = w_table(indata);
	return w;
}