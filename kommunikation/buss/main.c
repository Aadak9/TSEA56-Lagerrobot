/*
 * test_SPI.c
 *
 * Created: 2025-04-03 10:43:01
 * Author : ebblu474
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint8_t receivedData = 0;

void SPI_init() {
	// sätt upp SPI i slavläge
	
	DDRB = (1 << DDB4); //MISO som utgång
	SPCR = (1 << SPE); // Aktivera SPI
	sei(); // Aktivera globala avbrott
	
}

ISR(SPI_STC_vect) {
	// SPI interrupt: när data mottas, läs från SDPR (SPI Data Register)
	receivedData = SPDR;
	
	SPDR = receivedData;
}


int main(void)
{
	SPI_init();
	
    while (1) 
    {
		
    }
}

