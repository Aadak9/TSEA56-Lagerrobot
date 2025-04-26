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
	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1)|(0<<MUX0);							// AREF, left-shift, ADC6.
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Activate ADC, Prescaler 128.
}


void init_gyro()
{
	ADMUX = (0 << REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(1<<MUX1)|(1<<MUX0);						// AREF, left-shift, ADC7.
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Activate ADC, Prescaler 128.
}


void init_line_front()
{
	DDRA |= 0x0F;																					// Ports choice of sensor. Might change
	DDRD |= 0x20;																					// Port for enable

	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(0<<MUX1)|(1<<MUX0);							// AREF, left-shift, ADC5.
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Activate ADC, Prescaler 128.
}

void init_line_back()
{
	DDRD |= 0x1F;																					// Ports for enable and choice of sensor.
	ADMUX = (0<<REFS1)|(0<<REFS0)|(1<<ADLAR)|(1<<MUX2)|(0<<MUX1)|(0<<MUX0);							// AREF, left-shift, ADC4. VIRA TILL 36
	ADCSRA = (1<<ADEN)|(0<<ADSC)|(0<<ADATE)|(0<<ADIF)|(0<<ADIE)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);	// Activate ADC, Prescaler 128.
}


void init_interrupt()
{
	EICRA |=(1<<ISC01)|(1<<ISC00);																	// Interrupt on rising edge.
	EIMSK |= (1<<INT0);																				// ACtivate INT0.
}


void init_SPI()
{
	
	DDRB = (1 << DDB6);																				// Pin 7 (MISO) to output.
	SPCR = (1 << SPIE) | (1 << SPE) | (0 << DORD) | (0 << CPOL) | (0 << CPHA);						// Activate SPI-buss.
}


void init_timer()
{
	TCCR1B = (1 << WGM12);		// CTC-mode.
	TIMSK1 = (1 << OCIE1A);		// Timer 1 Compare A match.
	TCNT1 = 0;					// Timer start on 0.
	OCR1A = 2499;				// Interrupt when TCNT1 has counted up to OCR1A, 10ms.
}


int init_reflex_calibrate()
{
	PORTA &= 0xF0;									// Resets the four LSB bits in PORT A.
	PORTA |= 2;										// Set multiplexer to index 2. 2 is arbitrary.
	PORTA |= 0x10;									// Start sensor.
	
	is_active_reflex(3);							// Read but throwaway result.
	 _delay_us(20);									// First read gives faulty value.
	
	volatile uint8_t indata_t = AD_convert();
	
	PORTA &= 0xEF;									// Turn off sensor.
	
	if (indata_t >= 200)							// Calibrate line sensor for what tape.
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