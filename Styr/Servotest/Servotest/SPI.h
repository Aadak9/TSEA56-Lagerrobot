
volatile uint8_t current_action = 0;
volatile uint8_t last_action = 0;
volatile float reglerstyr = 0;

ISR(SPI_STC_vect) {
	// SPI interrupt: n�r data mottas, l�s fr�n SDPR (SPI Data Register)
	current_action = SPDR;
	if(current_action == 0x30)
	{
		reglerstyr = SPDR;
	}
}
