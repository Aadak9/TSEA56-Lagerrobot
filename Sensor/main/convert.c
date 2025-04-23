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
	volatile float volt_convert = digital_out*5.1/255.0;				// Kalibrera intern spänning
	return volt_convert;
}

/*
int convert_uint8_t(uint8_t num)
{
	//return (int)num;

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
*/

int is_active_reflex()
{
	volatile uint8_t indata_t = AD_convert();					//Första sensorläsning blir alltid 247
	//volatile int indata_int = convert_uint8_t(indata_t);
	volatile int indata_volt = digital_to_volt(indata_t);
	
	if (indata_volt >= 3) {																						
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

/*
int dist_table(int indata)
{
	if (indata <= 225) {
		return 0;
	} else {
		return 1;
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
*/

int linear_interpolation(int indata)
{
	int distances[] = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80};
	float voltages[] = {2.3, 1.65, 1.3, 0.98 , 0.9, 0.85, 0.73, 0.68, 0.6, 0.56, 0.5, 0.48, 0.45, 0.43, 0.4};
	
	float voltage = digital_to_volt(indata);
	
	for (int i = 0; i < 14; i++)
	{
		if (voltage <= voltages[i] && voltage >= voltages[i+1])
		{
			return distances[i] + (voltage - voltages[i]) * (distances[i+1] - distances[i]) / (voltages[i+1] - voltages[i]);
		}
	}
	if (voltage > voltages[0])
	{
		return  distances[0];
	}
	if (voltage < voltages[14])
	{
		return distances[14];
	}	
}