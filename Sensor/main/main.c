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
volatile uint8_t reflex_send;

extern volatile int theta;


int main()
{
	volatile uint8_t IR_send = 0;
	volatile uint8_t gyro_send = 0;
	volatile uint8_t reflex_send = 0;
	
	init_interrupt();
	init_SPI();
	init_timer();
	
	theta = 0;
	sei();
	
	while (1)
	{
		init_IR();
		IR_send = read_IR();

		init_reflex();
		reflex_send = read_reflex();
	}
}

ISR(TIMER1_COMPA_vect)
{
	read_gyro();
	
	if (theta > 90 || theta < -90)
	{
		theta = 0;
		TCCR1B &= ~((1 << CS12) | (1 << CS11) | (1 << CS10)); // Stänger av alla prescaler-bitar

	}
}

ISR(SPI_STC_vect)
{
	SPDR = IR_send;
	SPDR = gyro_send;
	SPDR = reflex_send;
}
