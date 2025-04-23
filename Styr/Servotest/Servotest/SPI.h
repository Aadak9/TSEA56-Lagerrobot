/*
volatile uint8_t current_action = 0;
volatile uint8_t last_action = 0;
volatile uint8_t second_last_action = 0;
volatile uint8_t reglerstyr_high = 0;
volatile uint8_t reglerstyr_low = 0;
volatile float reglerstyr = 0;

ISR(SPI_STC_vect) {
	// SPI interrupt: när data mottas, läs från SDPR (SPI Data Register)
	if(last_action == 0x30)
	{
		reglerstyr_high = SPDR;
		
		second_last_action = last_action;
		
	}
	else if(second_last_action == 0x30)
	{
		reglerstyr_low = SPDR;
		reglerstyr = (float)(reglerstyr_high << 8) | reglerstyr_low
	}
	else
	{
		current_action = SPDR;
		
	}
}
*/

volatile enum {
	SPI_STATE_WAITING,
	SPI_STATE_RECEIVE_TECKEN,
	SPI_STATE_RECEIVE_HIGH,
	SPI_STATE_RECEIVE_LOW
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
		}
		else
		{
			current_action = received;	
		}
		break;
		
		case SPI_STATE_RECEIVE_TECKEN:
		reglertecken = SPDR;
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

		default:
		spi_state = SPI_STATE_WAITING; // Fail-safe reset
		break;
	}
}
