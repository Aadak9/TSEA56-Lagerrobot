/*
 * main.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
#include <stdio.h>
#include "init.h"
#include "read.h"
#include "convert.h"


volatile uint8_t IR_send;
volatile uint8_t gyro_send;
volatile int8_t reflex;
volatile int8_t reflex_send;
volatile int8_t roadmark_send;
volatile int start_gyro;
volatile int reflex_high;


int main()
{
	IR_send = 0;
	gyro_send = 0;
	reflex_send = 0;
	reflex = 0;
	roadmark_send = 0;
	reflex_high = 3;
	TCCR1B &= ~(1 << CS11) | (1 << CS10);				// Stänger av timern och gyrot.		
	reset_w();
	
	init_interrupt();
	init_SPI();
	init_timer();
	
	sei();
	
//	TCCR1B |= (1 << CS11) | (1 << CS10);
	
	while (1)
	{
		init_IR();
		IR_send = read_IR();

		init_reflex();
		reflex = read_reflex(reflex_high);
		
		roadmark_send = reflex >> 6;				// Lägger de två roadmarkbitarna längst åt höger.
		reflex_send = reflex & (0x3F);				// Sätter de mest signifikanta bitar till noll. 
	}
}

// Avbrottsrutin för gyroskopet när roboten svänger.
ISR(TIMER1_COMPA_vect)
{
	init_gyro();
	gyro_send = read_gyro();
}

// Avbrottsrutin för SPI-avbrott. Choose sensor väljs av Rasperryn.
ISR(SPI_STC_vect)
{
	uint8_t volatile choose_sensor = SPDR;
	
	if(choose_sensor == 0) {
		SPDR = IR_send;
	} 
	else if(choose_sensor == 1) 
	{
		SPDR = reflex_send;
	}
	else if(choose_sensor == 2) 
	{
		TCCR1B |= (1 << CS11) | (1 << CS10);		// Sätter på timern och gyrot
	} 
	else if(choose_sensor == 3) 
	{
		cli();
		TCCR1B &= ~(1 << CS11) | (1 << CS10);		// Stänger av timern och gyrot
		reset_w();
		sei();
	} 
	else if(choose_sensor == 4) 
	{
		SPDR = gyro_send;
	} 
	else if(choose_sensor == 5) 
	{
		SPDR = roadmark_send;						// Roadmark är på formen 0b000000LR. L = left, R = right.
	}
	else if(choose_sensor == 6)
	{
		reflex_high = init_reflex_calibrate();
	}
}