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
	
	while(ADCSRA & (1<<ADSC))					// Vänta tills AD-omvandling är klar.
	{
	}
	
	sei();
	return indata_t = ADCH;
}


float digital_to_volt(int digital_out)
{
	volatile float volt_convert = digital_out*5.1/255.0;				// 5.1 är uppmätt spänningsvärde.
	return volt_convert;
}


int is_active_reflex(int reflex_high)
{
	volatile uint8_t indata_t = AD_convert();					
	volatile int indata_volt = digital_to_volt(indata_t);
	
	if (indata_volt >= reflex_high) {					// Är spänningen från linjesensor högre än referensvärde för tejp => returnera 1.																
		return 1;										
	} else {
		return 0;
	}
}


int linear_interpolation(int indata)
{
	int distances[] = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80};								// Avstånd från databladet.
	float voltages[] = {2.3, 1.65, 1.3, 0.98 , 0.9, 0.85, 0.73, 0.68, 0.6, 0.56, 0.5, 0.48, 0.45, 0.43, 0.4};	// Spänning från databladet.
	
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