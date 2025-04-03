/*
 * Avstnd_test.c
 *
 * Created: 2025-04-02 08:19:26
 * Author : andno773
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>



int convert_uint8_t(uint8_t num1)
{
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

int volt_to_dist(int digital_out)
{
	float volt = digital_out*5.1/1023;
	int distance = 27/pow(volt,1.15);
	return distance;
}


uint8_t AD_convert()
{
	ADCSRA |= (1 << ADSC);
	
	while(ADCSRA & (1<<ADSC)) // FEL TAR SIG ALDRIG UT
	{
	}
	
	uint8_t indata = ADCH;
	return indata;
}

