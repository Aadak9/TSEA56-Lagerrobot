/*
 * Servotest.c
 *
 * Created: 2025-04-02 08:15:43
 * Author : linfu930
 */ 

#include "init.h"
#include "Motorcontrol.h"
#include "Servocontrol.h"
#include "SPI.h"

#define FOSC 16000000 // Clock Speed
#define BAUD 1000000
#define MYUBRR FOSC/16/BAUD-1




/*
 * GccApplication1.c
 *
 * Created: 2025-04-04 08:57:51
 * Author : ebblu474
 */ 


#define F_CPU 16000000UL

#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>








int main(void)
{
	
	DDRA = 0b1010;
	PORTA = 0b0010;
	DDRD = 0b11000110; // Sätt TXD och TX enable till output och RXD till input
	USART_Init(MYUBRR);
	SPI_init();
	init_pwm();
	_delay_us(30);


	while (1)
	{
		
		if(current_action == 0x1)
		{
			drive_fwd();
		}
		else if(current_action == 0x2)
		{
			rotate_left_maybe();
		}
		else if(current_action == 0x3)
		{
			stop();
		}
	}}