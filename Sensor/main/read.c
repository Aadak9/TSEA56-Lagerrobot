#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "read.h"

int test = 0;
volatile uint8_t indata_t;
volatile int indata = 0;

// Avståndssensor
volatile int dist = 0;

// Reflexsensor
volatile int array[11];
volatile int sum = 0;
volatile int roadmark = 0;

// Gyro
volatile uint8_t indata_MSB;
volatile uint8_t indata_LSB;
volatile uint16_t indata16_t;
volatile float volt = 0;
volatile float w = 0;

uint8_t read_reflex()
{
	int i;
	uint8_t data;
	
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
	
	roadmark = is_roadmark(array[11]);
	
	return data = (uint8_t)(roadmark*16 + sum);
}


uint8_t read_IR()
{
	uint8_t data;
	
	indata_t = AD_convert(1);
	indata = convert_uint8_t(indata_t);
	dist = volt_to_dist(indata);
	
	if (dist > 250){									// Förhindrar integer overflow
		return data = 0xFF;
		} else {
		return data = (uint8_t)dist;
	}
}


uint8_t read_gyro()
{
	indata_MSB = AD_convert(1);
	indata_LSB = AD_convert(0);
	indata16_t = ((uint16_t)indata_MSB << 8) | indata_LSB;
	
	indata = convert_uint16_t(indata16_t);
	volt = digital_to_volt(indata);
	w = (volt - 2.5)/(2*volt) * 150;
	
	
	// Skicka dist till bussen
}