/*
 * main.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include <stdio.h>
#include "init.c"
#include "convert.c"

int indata = 0;
int dist = 0;

int main()
{
    init_IR();
	init_gyro();
	init_reflex();
	init_interrupt();
	
	sei();
	
    while (1) 
    {
    }
}

ISR(INT0_vect)
{
	ADCSRA |= (1 << ADSC);
}


ISR(ADC_vect)
{
	uint8_t indata_bin = ADCH;
	PORTB = indata_bin;
	indata = convert_uint8_t(indata_bin);
	dist = volt_to_dist(indata);
	sei();
}