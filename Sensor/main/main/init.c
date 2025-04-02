/*
 * main.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773
 */ 

#include <avr/io.h>


void init_IR();
{
	DDRD |= 0x04;
	PORTD &= 0xFB;
	
	ADMUX = (1<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1);
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(1<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}

void init_gyro();
{

}

void init_reflex();
{

}

void init_interrupt();
{
	EICRA |=(1<<ISC01)|(1<<ISC00);
	EIMSK |= (1<<INT0);
}
