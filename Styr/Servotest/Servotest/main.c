/*
 * Servotest.c
 *
 * Created: 2025-04-02 08:15:43
 * Author : linfu930
 */ 
#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

#define FOSC 16000000 // Clock Speed
#define BAUD 1000000
#define MYUBRR FOSC/16/BAUD-1



void USART_Init( unsigned char ubrr)
{
	/* Set baud rate */
	UBRR0H = (unsigned char) (ubrr>>8);
	UBRR0L = (unsigned char) ubrr;
	/*Enable transmit och receive */
	UCSR0B = (1<<RXEN0) | (1<<TXEN0);
	/* Frame format 8 data 2 stop */
	UCSR0C = (1<<USBS0)|(3<<UCSZ00);
}


void USART_Transmit( unsigned char* data, unsigned int size )
{
	PORTD |= 0x6;
	
	;
	/* Put data into buffer, sends the data */
	for(unsigned int i = 0; i < size; i++)
	{
		while ( !( UCSR0A & (1<<UDRE0)) )
			;
		UDR0 = (unsigned char)data[i];
	}
	
	//PORTD = 0;
	
}void move_servo(unsigned int ID, unsigned int Angle){	Angle = 3.41*Angle;	unsigned char P2 = (unsigned char)Angle;	unsigned char P3 = (unsigned char)(Angle>>8);	unsigned int header = 0xFF; //Börja varje med 2st 0xFF
	//unsigned int ID = ID; // Vilken servo
	unsigned int Length = 0x5; // 2 + antal P
	unsigned int Instruction = 0x03; // skriv
	unsigned int P1 = 30; // Address att skriva till
	//unsigned int P2 = 0x00; // första byten i målpositionen, minst signifikant
	//unsigned int P3 = 0x00; // andra byten i målpositionen
	unsigned int Checksum = ~(ID + Length + Instruction + P1 + P2 + P3);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, P1, P2, P3, Checksum};
	unsigned int data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
}void load_servo(unsigned int ID, unsigned int Angle){		Angle = 3.41*Angle;	unsigned char P2 = (unsigned char)Angle;	unsigned char P3 = (unsigned char)(Angle>>8);	unsigned int header = 0xFF; //Börja varje med 2st 0xFF
	//unsigned int ID = ID; // Vilken servo
	unsigned int Length = 0x5; // 2 + antal P
	unsigned int Instruction = 0x04; // skriv
	unsigned int P1 = 30; // Address att skriva till
	//unsigned int P2 = 0x00; // första byten i målpositionen, minst signifikant
	//unsigned int P3 = 0x00; // andra byten i målpositionen
	unsigned int Checksum = ~(ID + Length + Instruction + P1 + P2 + P3);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, P1, P2, P3, Checksum};
	unsigned int data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);	}void action(){	unsigned char header = 0xFF;	unsigned char Instruction = 0x5;		unsigned char Length = 0x2; // 2 + antal P	unsigned char ID = 0xFE;	unsigned char Checksum = ~(ID + Length + Instruction);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, Checksum};
	unsigned char data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
	_delay_us(10);}void init_pwm(){			}void drive_fwd(){			}int main(void)
{
	DDRD = 0b110; // Sätt TXD och TX enable till output och RXD till input
	USART_Init(MYUBRR);
	//USART_Init(0);




	/*
	unsigned int header = 0xFF; //Börja varje med 2st 0xFF
	unsigned int ID = 0x3; // Vilken servo
	unsigned int Length = 0x4; // 2 + antal P
	unsigned int Instruction = 0x02; // läs
	unsigned int P1 = 0x2B; // Address att skriva till
	unsigned int P2 = 0x01; // läs temp
	unsigned int P3 = 0x00; // andra byten i målpositionen
	unsigned int Checksum = ~(ID + Length + Instruction + P1 + P2 + P3);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, P1, P2, Checksum};
	*/
	//unsigned int data_size = sizeof(data) / sizeof(data[0]);
	
	//checksum = ~()
	//data[] = {0xFF, 0xFF, 0x3, ,
	/* Replace with your application code */
	while (1)
	{
		/*
		move_servo(3, 10);
		_delay_ms(2000);
		move_servo(3, 40);
		_delay_ms(2000);
		move_servo(3, 140);
		_delay_ms(2000);
		move_servo(3, 280);
		_delay_ms(2000);
		*/
		load_servo(2, 140);
		_delay_ms(2000);
		load_servo(3, 140);
		_delay_ms(1000);
		action();
		
		
		load_servo(2, 230);
		_delay_ms(2000);
		load_servo(3, 230);
		_delay_ms(1000);
		action();
		
	}
}