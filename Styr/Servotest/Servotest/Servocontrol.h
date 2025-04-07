




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
	

	
}void move_servo(unsigned int ID, unsigned int Angle){	Angle = 3.41*Angle;	unsigned int header = 0xFF; //Börja varje med 2st 0xFF
	unsigned int Length = 0x5; // 2 + antal P
	unsigned int Instruction = 0x03; // skriv
	unsigned int P1 = 30; // Address att skriva till
	unsigned char P2 = (unsigned char)Angle;	unsigned char P3 = (unsigned char)(Angle>>8);
	unsigned int Checksum = ~(ID + Length + Instruction + P1 + P2 + P3);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, P1, P2, P3, Checksum};
	unsigned int data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
}void load_servo(unsigned int ID, unsigned int Angle){		Angle = 3.41*Angle;		unsigned int header = 0xFF; //Börja varje med 2st 0xFF
	unsigned int Length = 0x5; // 2 + antal P
	unsigned int Instruction = 0x04; // skriv
	unsigned int P1 = 30; // Address att skriva till
	unsigned char P2 = (unsigned char)Angle; // första byten i målpositionen, minst signifikant	unsigned char P3 = (unsigned char)(Angle>>8); // andra byten i målpositionen
	unsigned int Checksum = ~(ID + Length + Instruction + P1 + P2 + P3);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, P1, P2, P3, Checksum};
	unsigned int data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);	}void read_temp(unsigned int ID){		unsigned int header = 0xFF; //Börja varje med 2st 0xFF	unsigned int length = 0x04;	unsigned int instruction = 0x02;	unsigned int P1 = 43;	unsigned int P2 = 0x01;	unsigned int Checksum = ~(ID + length + instruction + P1 + P2);		unsigned char data[] = {header, header, ID, length, instruction, P1, P2, Checksum};
	unsigned int data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);	PORTD &= ~(1 << 2);}void action(){	unsigned char header = 0xFF;	unsigned char Instruction = 0x5;		unsigned char Length = 0x2; // 2 + antal P	unsigned char ID = 0xFE;	unsigned char Checksum = ~(ID + Length + Instruction);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, Checksum};
	unsigned char data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
	_delay_us(10);}