#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "read.h"
#include "convert.h"

int test = 0;

uint8_t read_reflex()
{
	int i;
	volatile uint8_t data;
	volatile int array[11];
	
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
	
	volatile uint8_t indata_t = AD_convert(1);
	volatile int indata = convert_uint8_t(indata_t);
	volatile int dist = volt_to_dist(indata);
	
	if (dist > 250){									// Förhindrar integer overflow
		return data = 0xFF;
		} else {
		return data = (uint8_t)dist;
	}
}


uint8_t read_gyro()
{
	volatile uint8_t indata_MSB = AD_convert(1);
	volatile uint8_t indata_LSB = AD_convert(0);
	volatile uint16_t indata16_t = ((uint16_t)indata_MSB << 8) | indata_LSB;
	
	volatile int indata = convert_uint16_t(indata16_t);
	volatile float volt = digital_to_volt(indata);
	volatile float w = (volt - 2.5)/(2*volt) * 150;
	theta += w*dt;
	
	uint8_t result = 0;
	
	return  result;
	// Skicka dist till bussen
}