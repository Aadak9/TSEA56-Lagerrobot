#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "read.h"
#include "convert.h"


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
	
	pivot = sum_index/sum;
	offset = (6 - pivot);
								
	return data = (uint8_t)(roadmark*16 + offset);			//Dela upp i två array, offset negativt problem??
}


uint8_t read_IR()
{
	volatile uint8_t data;
	
	volatile uint8_t indata_t = AD_convert();
	volatile int indata = convert_uint8_t(indata_t);
	volatile int dist = dist_table(indata);
	
	return data = (uint8_t)dist;
}


int8_t read_gyro()
{		
	volatile uint8_t indata_t = AD_convert();
	volatile int indata = convert_uint8_t(indata_t);
	volatile float volt = digital_to_volt(indata);
	volatile int8_t w = (volt - 2.5)/0.033;
	return w;
}