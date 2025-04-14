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

uint8_t AD_convert()
{
//	cli();
	volatile uint8_t indata_t = 0;
	ADCSRA |= (1 << ADSC);
	
	while(ADCSRA & (1<<ADSC))
	{
	}
	
//	sei();
	return indata_t = ADCH;
}


float digital_to_volt(int digital_out)
{
	volatile float volt_convert = digital_out*5.0/1023.0;				// Kalibrera intern sp�nning
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
		conversion += array[index]*(1 << (7 - index + 2));
	}
	
	return conversion;
}


int is_active_reflex()
{
	volatile uint8_t indata_t = AD_convert();
	volatile int indata_int = convert_uint8_t(indata_t);
	volatile int indata_volt = digital_to_volt(indata_int);
	
	if (indata_volt > 2) {								// �ndra 2 till ett v�rde som kalibreras
		return 1;
	} else {
		return 0;
	}
}


int volt_to_dist(int indata)
{
	volatile float volt_convert = digital_to_volt(indata);
	volatile int distance = 27/(pow(volt_convert,1.15));
	return distance;
}


int is_roadmark(int sum)
{
	if (sum > 4) {									// Placeholder v�rde
		return 1;
		} else {
		return 0;
	}
}