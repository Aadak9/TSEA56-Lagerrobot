

#include "Kommunikations_Definitioner.h"

volatile enum {
	SPI_STATE_WAITING,
	SPI_STATE_RECEIVE_TECKEN,
	SPI_STATE_RECEIVE_HIGH,
	SPI_STATE_RECEIVE_LOW,
	
	SPI_STATE_RECIEVE_JOINT
} spi_state = SPI_STATE_WAITING;

volatile uint8_t reglerstyr_high = 0;
volatile uint8_t reglerstyr_low = 0;
volatile uint8_t reglertecken = 0; // 0 innebär positivt tal
volatile float reglerstyr = 0;
volatile uint8_t current_action = 0;
volatile uint8_t last_action = 0;

ISR(SPI_STC_vect) {
	uint8_t received = SPDR;
	switch (spi_state) {
		case SPI_STATE_WAITING:
			if (received == 0x30) {
				spi_state = SPI_STATE_RECEIVE_TECKEN;
				current_action = received;
			}
			else if(received == SET_JOINT)
			{
				spi_state = SPI_STATE_RECIEVE_JOINT;
			}
			else if(received == SEND_LEFT_GAS)
			{
				SPDR = OCR2A;	
			}
			else if(received == SEND_RIGHT_GAS)
			{
				SPDR = OCR2B;
			}
			else
			{
				current_action = received;
				
			}

			break;
		
		case SPI_STATE_RECEIVE_TECKEN:
			reglertecken = received;
			spi_state = SPI_STATE_RECEIVE_HIGH;
			break;
		


		case SPI_STATE_RECEIVE_HIGH:
			reglerstyr_high = received;
			spi_state = SPI_STATE_RECEIVE_LOW;
			break;



		case SPI_STATE_RECEIVE_LOW:
			reglerstyr_low = received;
			cli();
			reglerstyr = (float)((reglerstyr_high << 8) | reglerstyr_low);
			reglerstyr /= 100;
			sei();
			if(reglertecken == 1)
			{
				reglerstyr *= -1;
			}
			spi_state = SPI_STATE_WAITING; // Reset for next command
			break;



		case SPI_STATE_RECIEVE_JOINT:
			current_joint = SPDR;
			spi_state = SPI_STATE_WAITING;
			break;


		default:
			spi_state = SPI_STATE_WAITING; // Fail-safe reset
			break;
	}
} 
