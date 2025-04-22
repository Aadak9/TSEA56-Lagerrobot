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
volatile int8_t gyro_send;
volatile int8_t reflex_send;


int main()
{
	volatile uint8_t IR_send = 0;
	volatile int8_t gyro_send = 0;
	volatile uint8_t reflex_send = 0;
	
	init_interrupt();
	init_SPI();
	
	sei();
	
	while (1)
	{
		init_IR();
		IR_send = read_IR();

		init_reflex();
		reflex_send = read_reflex();
		
		init_gyro();
		gyro_send = read_gyro();
		
	}
}


uint8_t fetch_IR()
{
	return IR_send;
}


int8_t fetch_gyro()
{
	return gyro_send;
}


int8_t fetch_reflex()
{
	return reflex_send;
}


ISR(SPI_STC_vect)
{

	uint8_t choose_sensor = (uint8_t)SPDR;
	
	if(choose_sensor == 0)
	{
		SPDR = fetch_IR();
	} else if(choose_sensor == 1) {
		SPDR = fetch_reflex();
	} else if(choose_sensor == 2) {
		SPDR = fetch_gyro();
	}

}

