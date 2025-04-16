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
	cli();
	volatile uint8_t indata_t = 0;
	ADCSRA |= (1 << ADSC);
	
	while(ADCSRA & (1<<ADSC))
	{
	}
	
	sei();
	return indata_t = ADCH;
}


float digital_to_volt(int digital_out)
{
	volatile float volt_convert = digital_out*5.0/1023.0;				// Kalibrera intern spänning
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
	
	if (indata_volt > 2) {								// Ändra 2 till ett värde som kalibreras
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
	if (sum > 4) {									// Placeholder värde
		return 1;
		} else {
		return 0;
	}
}


int dist_table(int indata)
{
	if (indata >= 600){ 
		return 10;
	} else if (indata >= 470) {
		return 15;
	} else if (indata >= 390) {
		return 20;
	} else if (indata >= 307) {
		return 25;
	} else if (indata >= 256) { 
		return 30;
	} else if (indata >= 225) { 
		return 35;
	} else if (indata >= 200) { 
		return 40;
	} else if (indata >= 163) { 
		return 50;
	} else if (indata >= 133) { 
		return 60;
	} else if (indata >= 112) { 
		return 70;
	} else {
		return 80;
	}
}

int w_table(int indata)
{
	volatile int array_indata[11] = {936,851,766,681,596,511,426,341,256,171,86};
	volatile int array_output[11] = {63,50,38,25,12,0,-12,-25,-37,-50-63};
	
	for (int i = 0; i < 11; i++ )
	{
		if (indata > array_indata[i]){
			linear_interpolation(int indata,)
			return
		}
	}
		
		
	if (indata >= 936) {
		return 63;
	} else if (indata >= 851) {
		linear_interpolation()
		return w;
	} else if (indata >= 766) {
		return 38;
	} else if (indata >= 681) {
		return 25;
	} else if (indata >= 596) {
		return 12;
	} else if (indata >= 511) {
		return 0;
	} else if (indata >= 426) {
		return -12;
	} else if (indata >= 341) {
		return -25;
	} else if (indata >= 256) {
		return -37;
	} else if (indata >= 171) {
		return -50;
	} else if (indata >= 86) {
		return -62;
	}
	

}

int linear_interpolation(int indata)
{
	
}