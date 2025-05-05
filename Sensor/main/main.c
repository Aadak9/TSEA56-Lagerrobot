/*
 * main.c
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <math.h>
//#include <stdio.h>
#include "init.h"
#include "read.h"
#include "convert.h"


volatile uint8_t IR_send;
volatile uint8_t gyro_send;
volatile int8_t line_front;
volatile int8_t line_front_send;
volatile int8_t line_back_send;
volatile int8_t roadmark_send;
volatile int start_gyro;
volatile int reflex_high;


int main()
{
	IR_send = 0;
	gyro_send = 0;
	line_front_send = 0;
	line_back_send = 0;
	line_front = 0;
	roadmark_send = 0;
	reflex_high = 3;
	TCCR1B &= ~(1 << CS11) | (1 << CS10);				// Turn off timer and gyro.		
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

		init_line_front();
		line_front = read_line_front(reflex_high);
		
		roadmark_send = (line_front >> 6) & (0x03);					// Roadmark bits to the right.
		line_front_send = line_front & (0x3F);				// MSB to 0. 

		init_line_back();
		line_back_send = read_line_back(reflex_high);

	}
}

// Interrupt for gyro when robot is turning.
ISR(TIMER1_COMPA_vect)
{
	init_gyro();
	gyro_send = read_gyro();
}

// Interrupt for SPI-interrupt. Choose sensor comes from Raspberry PI.
ISR(SPI_STC_vect)
{
	uint8_t volatile choose_sensor = SPDR;
	
	if(choose_sensor == 0) {
		SPDR = IR_send;
	} 
	else if(choose_sensor == 1) 
	{
		SPDR = line_front_send;
	}
	else if(choose_sensor == 2) 
	{
		SPDR = line_back_send;
	}
	else if(choose_sensor == 3) 
	{
		reset_w();
		TCCR1B |= (1 << CS11) | (1 << CS10);			// Start timer and gyro.
	} 
	else if(choose_sensor == 4) 
	{
		cli();
		TCCR1B &= ~((1 << CS11) | (1 << CS10));			// Turn off timer and gyro.
		reset_w();
		sei();
	} 
	else if(choose_sensor == 5)							// On the Raspberry PI, check for 80 which is 90 degrees or 160 which is 180 degrees.
	{
		SPDR = gyro_send;
	} 
	else if(choose_sensor == 6) 
	{
		SPDR = roadmark_send;							// Roadmark is in the form of 0b000000LR. L = left, R = right.
	}
	else if(choose_sensor == 7)
	{
		reflex_high = init_reflex_calibrate();
	}
}