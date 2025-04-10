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

volatile uint8_t IR_send = 0;
volatile uint8_t gyro_send = 0;
volatile uint8_t reflex_send = 0;


int main()
{
	init_interrupt();
	init_SPI();
	sei();
	
	while (1)
	{
		init_IR();
		IR_send = read_IR();
		
		init_gyro();
		gyro_send = read_gyro();
		
		init_reflex();
		reflex_send = read_reflex();
	}
}

ISR(TIMER1_COMPA_vect)
{
	read_gyro();
}

ISR(SPI_STC_vect)
{
	SPDR = IR_send;
	SPDR = gyro_send;
	SPDR = reflex_send;
}
