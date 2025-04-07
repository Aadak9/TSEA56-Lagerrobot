#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>





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



void init_pwm(){		
	TCCR2A |= (1 << COM2A1) | (0 << COM2A0) | (1 << COM2B1) | (0 << COM2B0) | (1 << WGM21) | (1 << WGM20);
	TCCR2B |= (0 << WGM22) | (0 << CS22) | (1 << CS21) | (0 << CS20);
	

	
	TCCR2B |= (1 << CS21);

	OCR2A = 0x0;
	OCR2B = 0x0;	}void SPI_init() {
	// sätt upp SPI i slavläge
	
	DDRB = (1 << DDB6); //MISO som utgång
	SPCR = (1 << SPE) | (1 << SPIE) | (0 << DORD) | (0 << CPOL) | (0 << CPHA); // Aktivera SPI
	sei(); // Aktivera globala avbrott
	
}