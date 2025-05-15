

#include "Kommunikations_Definitioner.h"

volatile enum {
	SPI_STATE_WAITING,
	SPI_STATE_RECEIVE_TECKEN,
	SPI_STATE_RECEIVE_HIGH,
	SPI_STATE_RECEIVE_LOW,
	
	SPI_STATE_RECEIVE_JOINT_SEND_HIGH_ANGLE,
	SPI_STATE_SEND_HIGH_ANGLE,
	SPI_STATE_SEND_LOW_ANGLE,
	SPI_STATE_RECIEVE_JOINT,
	
	SPI_STATE_RECEIVE_JOINT_MOVE_SERVO,
	SPI_STATE_RECEIVE_ANGLE_HIGH,
	SPI_STATE_RECEIVE_ANGLE_LOW
	
	
	
	
} spi_state = SPI_STATE_WAITING;

volatile uint8_t reglerstyr_high = 0;
volatile uint8_t reglerstyr_low = 0;
volatile uint8_t reglertecken = 0; // 0 innebär positivt tal
volatile float reglerstyr = 0;
volatile uint8_t current_action = 0;
volatile uint8_t last_action = 0;
volatile uint8_t target_joint = 0;
volatile uint16_t angle = 0;
volatile uint8_t angle_low = 0;
volatile uint8_t angle_high = 0;

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
			else if(received == SEND_ANGLE)
			{
				spi_state = SPI_STATE_RECEIVE_JOINT_SEND_HIGH_ANGLE;

				
			}
			else if(received == 0x70)
			{
				SPDR = 45;
			}
			else if(received == MOVE_SERVO)
			{
				spi_state = SPI_STATE_RECEIVE_JOINT_MOVE_SERVO;
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
			reglerstyr = (float)((reglerstyr_high << 8) | reglerstyr_low);
			reglerstyr /= 100;
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


		case SPI_STATE_RECEIVE_JOINT_SEND_HIGH_ANGLE:
			target_joint = received;
			angle = get_angle(target_joint);
			angle_low = angle & 0xFF;
			angle_high = (angle >> 8) & 0xFF;
			//SPDR = angle_high;
			spi_state = SPI_STATE_SEND_HIGH_ANGLE;
			break;
			
		case SPI_STATE_SEND_HIGH_ANGLE:
			SPDR = angle_high;
			spi_state = SPI_STATE_SEND_LOW_ANGLE;
			break;
			
		case SPI_STATE_SEND_LOW_ANGLE:
			SPDR = angle_low;
			spi_state = SPI_STATE_WAITING;
			break;
			
			
		case SPI_STATE_RECEIVE_JOINT_MOVE_SERVO:
			target_joint = received;
			spi_state = SPI_STATE_RECEIVE_ANGLE_HIGH;
			break;
			
		case SPI_STATE_RECEIVE_ANGLE_HIGH:
			angle_high = received;
			spi_state = SPI_STATE_RECEIVE_ANGLE_LOW;
			break;
		
		case SPI_STATE_RECEIVE_ANGLE_LOW:
			angle_low = received;
			angle = angle_low + (angle_high << 8);
			move_joint(target_joint, angle);
			
			spi_state = SPI_STATE_WAITING;
			
			
			
			
			
			
		default:
			spi_state = SPI_STATE_WAITING; // Fail-safe reset
			break;
	}
} 
