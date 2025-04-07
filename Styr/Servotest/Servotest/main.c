/*
 * Servotest.c
 *
 * Created: 2025-04-02 08:15:43
 * Author : linfu930
 */ 

#include "init.h"
#include "Motorcontrol.h"
#include "Servocontrol.h"

#define FOSC 16000000 // Clock Speed
#define BAUD 1000000
#define MYUBRR FOSC/16/BAUD-1





int main(void)
{
	DDRA = 0b1010;
	PORTA = 0b0010;
	DDRD = 0b11000110; // Sätt TXD och TX enable till output och RXD till input
	USART_Init(MYUBRR);

	init_pwm();
	move_servo(3, 200);
	_delay_us(30);


	while (1)
	{
		
		rotate_left_maybe();
		_delay_ms(2000);
		rotate_right_maybe();
		_delay_ms(1000);
		stop();
		_delay_ms(1000);
		
		
		
	}
}