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
#include "Kommunikations_Definitioner.h"

#define FOSC 16000000 // Clock Speed
#define BAUD 1000000
#define MYUBRR FOSC/16/BAUD-1

volatile unsigned long counter = 0;   

volatile unsigned long timertime = 8000;



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
			reverse();
		}
		else if(current_action == 0x4 )
		{
			rotate_right_maybe();
		}
		else if(current_action == FWD_LEFT)
		{
			fwd_left();
		}
		else if(current_action == FWD_RIGHT) 
		{
			fwd_right();
		}
		else if(current_action == 0)
		{
			stop();
		}
		else if(current_action == 0x14 && current_action != last_action)
		{
			decrease_speed();
		}
		else if(current_action == 0x15 && current_action != last_action)
		{
			increase_speed();
		}

		
		// Reglering
		
		
		else if(current_action == 0x30)
		{
			float reglercopy;
			cli();
			reglercopy = reglerstyr;
			sei();
			
			drive_and_turn(reglercopy);
			
		}

		
			
			
		// Servon	
		else if(current_action == 0x31)
		{
			counter += 1;
			if(counter >= timertime)
			{
				add1degree_joint(current_joint);
				counter = 0;
			}
		}
		else if(current_action == 0x32)
		{
			counter +=1;
			if(counter >= timertime)
			{
				sub1degree_joint(current_joint);
				counter = 0;
			}
		}

		
		
		
		
		
		
		

		
		last_action = current_action;
	}}