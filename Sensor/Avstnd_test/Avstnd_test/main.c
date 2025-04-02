/*
 * Avstnd_test.c
 *
 * Created: 2025-04-02 08:19:26
 * Author : andno773
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include "Math.c"
#include <stdio.h>

int indata = 0;
int dist = 0;
int test = 0;


int main(void)
{
    DDRB = 0xff;
	DDRD = 0x00;
	PORTD = 0x00;
	
	ADMUX = (1<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1);
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(1<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
	
	EICRA |=(1<<ISC01)|(1<<ISC00);
	EIMSK |= (1<<INT0);
	
	sei();
	
    while (1) 
    {
		//sei();
    }
}


ISR(INT0_vect)
{
	//cli();
	ADCSRA |= (1 << ADSC);
}


ISR(ADC_vect)
{
	uint8_t indata_bin = ADCH;
	PORTB = indata_bin;
	indata = convert_uint8_t(indata_bin);
	dist = volt_to_dist(indata);
	test = 4;
	sei();
}