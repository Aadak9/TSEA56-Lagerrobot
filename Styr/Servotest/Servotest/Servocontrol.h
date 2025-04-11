
volatile unsigned int angle1 = 0;

volatile unsigned int currentID = 1;



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
	

	
}void USART_Recieve(unsigned char* buffer, unsigned int size) // DENNA MÅSTE LÖSAS ASAP{	PORTD &= ~(1 << 2);    for (unsigned int i = 0; i < size; i++)
    {
        // Wait until data is received
        while (!(UCSR0A & (1 << RXC0)))
		{
			//if (UCSR0A & (1 << DOR0)) {
            //    unsigned char temp = UDR0; // Clear the error
            //}
		}

        // Read the received data
        buffer[i] = UDR0;
    }		PORTD |= (1 << 2);		}void move_servo(unsigned int ID, unsigned int Angle){	Angle = 3.41*Angle;	unsigned int header = 0xFF; //Börja varje med 2st 0xFF
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
	USART_Transmit(data, data_size);	PORTD &= ~(1 << 2);}unsigned int get_angle(unsigned int ID)
{
	unsigned char header = 0xFF;
	unsigned char id = ID;
	unsigned char length = 0x04;
	unsigned char instruction = 0x02;
	unsigned char P1 = 36;
	unsigned char P2 = 0x2;
	unsigned int Checksum = ~(ID + length + instruction + P1 + P2);
	
	unsigned char data[] = {header, header, id, length, instruction, P1, P2, Checksum};
	unsigned char data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
	_delay_us(60);
	unsigned char angledata[7] = {0,0,0,0,0,0,0};
	USART_Recieve(angledata, 6);
	
	unsigned int angle = angledata[4] + (angledata[5] << 8);
	return angle;
}void action(){	unsigned char header = 0xFF;	unsigned char Instruction = 0x5;		unsigned char Length = 0x2; // 2 + antal P	unsigned char ID = 0xFE;	unsigned char Checksum = ~(ID + Length + Instruction);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, Checksum};
	unsigned char data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
	_delay_us(10);}void add1degree(unsigned int ID){	unsigned int angle = get_angle(ID);	if(angle < 300)
	{					
		angle += 1;
		move_servo(ID, angle);
	}}void sub1degree(unsigned int ID){	unsigned int angle = get_angle(ID);	if(angle > 0)
	{
		angle -= 1;
		move_servo(ID, angle);
	}
}

void add1degree2(unsigned int ID1, unsigned int ID2)
{
	if(angle1 < 300)
	{
		angle1 += 1;
		load_servo(ID1, angle1);
		load_servo(ID2, angle1);
		action();

	}	
	
}



void sub1degree2(unsigned int ID1, unsigned int ID2)
{

	if(angle1 > 0)
	{
		angle1 -= 1;
		load_servo(ID1, angle1);
		load_servo(ID2, angle1);
		action();

	}	
	
}



