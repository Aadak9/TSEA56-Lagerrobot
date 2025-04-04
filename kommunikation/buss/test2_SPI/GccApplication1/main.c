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

volatile uint8_t receivedData = 0;

void SPI_init() {
	// sätt upp SPI i slavläge
	
	DDRB = (1 << DDB6); //MISO som utgång
	SPCR = (1 << SPE) | (1 << SPIE) | (0 << DORD) | (0 << CPOL) | (0 << CPHA); // Aktivera SPI
	sei(); // Aktivera globala avbrott
	
}

ISR(SPI_STC_vect) {
	// SPI interrupt: när data mottas, läs från SDPR (SPI Data Register)
	receivedData = SPDR;
	
	SPDR = receivedData;

}


char SPI_SlaveReceive(void)
{
	/* Wait for reception complete */
	while(!(SPSR & (1<<SPIF)))
	;
	/* Return Data Register */
	return SPDR;
}



int main(void)
{
	SPI_init();
	DDRA = 0b1;
    while (1) 
    {
		/*
		//char hej = SPI_SlaveReceive();
		if(hej == 0x42)
		{
			PORTA = 0b1;
			_delay_ms(1000);
			
		}
	
		PORTA = 0;
		*/
    }
}


