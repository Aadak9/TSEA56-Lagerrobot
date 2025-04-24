/*
 * init.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#define F_CPU 16000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "init.h"
#include "convert.h"


void init_IR()
{
	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1)|(0<<MUX0);							// AREF, v�nsterskift, ADC6.
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Aktiverar ADC, Prescaler 128.
}


void init_gyro()
{
	ADMUX = (0 << REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1)|(1<<MUX0);						// AREF, v�nsterskift, ADC7.
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Aktiverar ADC, Prescaler 128.
}


void init_reflex()
{
	DDRA |= 0x1F;																					// Portar f�r enable och val av sensor.
	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(0<<MUX1)|(1<<MUX0);							// AREF, v�nsterskift, ADC5.
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Aktiverar ADC, Prescaler 128.
}


void init_interrupt()
{
	EICRA |=(1<<ISC01)|(1<<ISC00);																	// Avbrott p� stigande flank.
	EIMSK |= (1<<INT0);																				// Aktivera INT0.
}


void init_SPI()
{
	
	DDRB = (1 << DDB6);																				// Pinne 7 (MISO) till utdata.
	SPCR = (1 << SPIE) | (1 << SPE) | (0 << DORD) | (0 << CPOL) | (0 << CPHA);						// Aktivera SPI-buss.
}


void init_timer()
{
	TCCR1B = (1 << WGM12);		// CTC-l�ge.
	TIMSK1 = (1 << OCIE1A);		// Timer 1 Compare A match.
	TCNT1 = 0;					// Klocka startar p� noll.
	OCR1A = 2499;				// Avbrott d� klockan r�knat upp till OCR1A, 10ms.
}


int init_reflex_calibrate()
{
	PORTA &= 0xF0;									// Nollst�ller de fyra LSB bitarna i PORT A.
	PORTA |= 2;										// S�tter Muxen till index 2.
	PORTA |= 0x10;									// Startar sensorn.
	
	is_active_reflex(3);							// L�s men kasta resultatet.
	 _delay_us(20);									// F�rsta l�sningen ger fel v�rde.
	
	volatile uint8_t indata_t = AD_convert();
	
	PORTA &= 0xEF;									// St�nger av sensorn.
	
	if (indata_t >= 200)							// Kalibrerar linjesensor f�r vad som �r tejp.
	{
		return 4;
	}
	else if (indata_t >= 140)
	{
		return 3;
	}
	else if (indata_t >= 100)
	{
		return 2;
	}
	else
	{
		return 1;
	}
}