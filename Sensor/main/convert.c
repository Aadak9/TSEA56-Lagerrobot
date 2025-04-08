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

// Reflexsensor
uint8_t indata_t = 0;
int indata_int = 0;
int indata_volt = 0;

uint8_t AD_convert()
{
	ADCSRA |= (1 << ADSC);
	
	while(ADCSRA & (1<<ADSC))
	{
	}
	
	uint8_t indata_t = ADCH;
	return indata_t;
}

int digtal_to_volt(int digital_out)
{
	int volt = digital_out*5.1/1023;
	return volt;
}


int convert_uint8_t(uint8_t num1)
{
	// Konverterar en uint8_t variabel till int
	
	int array[8];
	for (int i = 0; i <8; i++ )
	{
		array[i] = (num1 >>(7-i)) & 1;	
	}
	
	int conversion = 0;
	
	for (int index = 0; index < 8; index++)
	{	
		conversion += array[index]*(1 << (7-index+2));
	}
	
	return conversion;
}


int is_active_reflex()
{
	indata_t = AD_convert();
	indata_int = convert_uint8_t(indata_t);
	indata_volt = digtal_to_volt(indata_int);
	
	if (indata_volt > 2) {						// Ändra 2 till ett värde som kalibreras
		return 1;
	} else {
		return 0;
	}
}


int volt_to_dist(int digital_out)
{
	float volt = digtal_to_volt(digital_out);
	int distance = 27/pow(volt,1.15);
	return distance;
}

