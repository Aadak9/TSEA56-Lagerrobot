/*
 * init.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include "init.h"


void init_IR()
{
	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1)|(0<<MUX0);
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}


void init_gyro()
{
	ADMUX = (0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1)|(1<<MUX0);
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}


void init_reflex()
{
	DDRA |= 0x1F;
	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(0<<MUX1)|(1<<MUX0); 
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}


void init_interrupt()
{
	EICRA |=(1<<ISC01)|(1<<ISC00);
	EIMSK |= (1<<INT0);
}


void init_SPI()
{
	//DDRB &= ~((1<<PORTB5)|(1<<PORTB7)|(1<<PORTB4));
	DDRB = (1 << DDB6);
	SPCR = (1 << SPIE) | (1 << SPE) | (0 << DORD) | (0 << CPOL) | (0 << CPHA); 
}


void init_timer()
{
	TCCR1B = (1 << WGM12);
	TIMSK1 = (1 << OCIE1A);
	TCNT1 = 0;
	OCR1A = 2499;
}