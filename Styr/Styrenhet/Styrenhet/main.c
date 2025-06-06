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

volatile unsigned long timertime = 14000;


#define F_CPU 16000000UL

#include <util/delay.h>
#include <avr/io.h>
#include <avr/interrupt.h>





int main(void)
{
	
	DDRA = 0b1010;
	PORTA = 0b0010;
	DDRD = 0b11000110; // S�tt TXD och TX enable till output och RXD till input
	USART_Init(MYUBRR);
	SPI_init();
	init_pwm();
	
	_delay_ms(200);
	for(unsigned int i=1; i <= 7; i++)
	{
		set_speed(i, 80); // Sätter alla servon utom gripklon till en långsam hastighet
	}
	
	set_speed(8, 500); // Sätter gripklons hastighet.

	while (1)
	{
	
		if(current_action == DRIVE_FWD)
		{
			drive_fwd();
		
		}
		else if(current_action == ROTATE_LEFT)
		{
			rotate_left();
		}
		else if(current_action == REVERSE)
		{
			reverse();
		}
		else if(current_action == ROTATE_RIGHT)
		{
			rotate_right();
		}
		else if(current_action == FWD_LEFT)
		{
			fwd_left();
		}
		else if(current_action == FWD_RIGHT) 
		{
			fwd_right();
		}
		else if(current_action == STOP)
		{
			stop();
		}
		else if(current_action == DECREASE_SPEED && current_action != last_action)
		{
			decrease_speed();
		}
		else if(current_action == INCREASE_SPEED && current_action != last_action)
		{
			increase_speed();
		}

		
		// Reglering
		
		
		else if(current_action == FOLLOW_LINE)
		{
			float reglercopy;
			cli();
			reglercopy = reglerstyr;
			sei();
			
			drive_and_turn(reglercopy);
			
		}

		
			
			
		// Servon	
		else if(current_action == CCW_SERVO)
		{
			counter += 1;
			if(counter >= timertime)
			{
				add1degree_joint(current_joint);
				counter = 0;
				_delay_ms(50);
			}
		}
		else if(current_action == CW_SERVO)
		{
			counter +=1;
			if(counter >= timertime)
			{
				sub1degree_joint(current_joint);
				counter = 0;
				_delay_ms(50);
			}
		}
		
		last_action = current_action;
	}
}

