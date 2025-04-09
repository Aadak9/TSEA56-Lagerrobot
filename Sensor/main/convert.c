/*
 * convert.c
 *
 * Created: 2025-04-02 08:19:26
 * Author : andno773, sigry751
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "convert.h"

volatile uint8_t indata_t = 1000;
volatile int indata_int = 0;
volatile int indata_volt = 0;
volatile int volt_convert = 0;
volatile int distance = 0;
volatile int sum_t = 0;

uint8_t AD_convert(int is_MSB)
{
	ADCSRA |= (1 << ADSC);
	
	while(ADCSRA & (1<<ADSC))
	{
	}
	
	if (is_MSB){
		return indata_t = ADCH;
	} else {
		return indata_t = ADCL;
	}
}


float digital_to_volt(int digital_out)
{
	volt_convert = digital_out*5.1/1023;				// Kalibrera intern spänning
	return volt_convert;
}


int convert_uint8_t(uint8_t num)
{
	// Konverterar en uint8_t variabel till int
	
	int array[8];
	for (int i = 0; i <8; i++ )
	{
		array[i] = (num >>(7-i)) & 1;	
	}
	
	int conversion = 0;
	
	for (int index = 0; index < 8; index++)
	{	
		conversion += array[index]*(1 << (7-index+2));
	}
	
	return conversion;
}


int convert_uint16_t(uint16_t num)
{
	int array[16];
	for (int i = 0; i < 16; i++ )
	{
		array[i] = (num >>(15-i)) & 1;
	}
	
	int conversion = 0;
	
	for (int index = 0; index < 16; index++)
	{
		conversion += array[index]*(1 << (15-index+2));
	}
	
	return conversion;
}


int is_active_reflex()
{
	indata_t = AD_convert(1);
	indata_int = convert_uint8_t(indata_t);
	indata_volt = digital_to_volt(indata_int);
	
	if (indata_volt > 2) {								// Ändra 2 till ett värde som kalibreras
		return 1;
	} else {
		return 0;
	}
}


int volt_to_dist(int digital_out)
{
	distance = 27/pow(digital_to_volt(digital_out),1.15);
	return distance;
}


int is_roadmark(int array[11])
{
	for (int index = 0; index < 11; index++)
	{
		sum_t += array[index];
	}
	
	if (sum_t > 4) {									// Placeholder värde
		return 1;
		} else {
		return 0;
	}
}
