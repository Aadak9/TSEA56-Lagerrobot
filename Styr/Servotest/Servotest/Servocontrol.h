volatile unsigned int rotatespeed = 9;

volatile unsigned int current_joint = 1;





void USART_Transmit( unsigned char* data, unsigned int size )
{
	PORTD |= 0b100;
	
	;
	/* Put data into buffer, sends the data */
	for(unsigned int i = 0; i < size; i++)
	{
		while ( !( UCSR0A & (1<<UDRE0)) )
		;
		UDR0 = (unsigned char)data[i];
	}
	
	while ( !( UCSR0A & (1<<TXC0)) )
		;
	UCSR0A |= 1<<TXC0;
}void USART_Recieve(unsigned char* buffer, unsigned int size) // DENNA MÅSTE LÖSAS ASAP{	    for (unsigned int i = 0; i < size; i++)
    {
       
        while (!(UCSR0A & (1 << RXC0)))
		;

        buffer[i] = UDR0;
    }		PORTD |= (1 << 2);		//_delay_us(50);}void move_servo(unsigned int ID, unsigned int Angle){		unsigned int header = 0xFF; //Börja varje med 2st 0xFF
	unsigned int Length = 0x5; // 2 + antal P
	unsigned int Instruction = 0x03; // skriv
	unsigned int P1 = 30; // Address att skriva till
	unsigned char P2 = (unsigned char)Angle;	unsigned char P3 = (unsigned char)(Angle>>8);
	unsigned int Checksum = ~(ID + Length + Instruction + P1 + P2 + P3);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, P1, P2, P3, Checksum};
	unsigned int data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
}void load_servo(unsigned int ID, unsigned int Angle){				unsigned int header = 0xFF; //Börja varje med 2st 0xFF
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
	
	PORTD &= ~(1 << 2);
	
	unsigned char angledata[8] = {0,0,0,0,0,0,0,0};
	USART_Recieve(angledata, 8);
	
	volatile unsigned long angle = angledata[5] + ((unsigned int)angledata[6] << 8);
	return angle;
	}void action(){	unsigned char header = 0xFF;	unsigned char Instruction = 0x5;		unsigned char Length = 0x2; // 2 + antal P	unsigned char ID = 0xFE;	unsigned char Checksum = ~(ID + Length + Instruction);
	
	unsigned char data[] = {header, header, ID, Length, Instruction, Checksum};
	unsigned char data_size = sizeof(data) / sizeof(data[0]);
	USART_Transmit(data, data_size);
	_delay_us(10);}void move_2servo(unsigned int ID1, unsigned int ID2, unsigned int angle){	load_servo(ID1, angle);	load_servo(ID2, angle);	action();		}void add1degree(unsigned int ID){	unsigned int angle = get_angle(ID);	if(angle < 1023)
	{					
		angle += rotatespeed;
		move_servo(ID, angle);
		_delay_us(50);
	}}void sub1degree(unsigned int ID){	unsigned int angle = get_angle(ID);	if(angle > 0)
	{
		angle -= rotatespeed;
		move_servo(ID, angle);
	}
}

void add1degree2(unsigned int ID1, unsigned int ID2)
{
	unsigned int angle1 = get_angle(ID1);
	unsigned int angle2 = get_angle(ID2);
	if(angle1 < 1023)
	{
		angle1 += rotatespeed;
		angle2 += rotatespeed;
		load_servo(ID1, angle1);
		load_servo(ID2, angle2);
		action();

	}	
	
}

void sub1degree2(unsigned int ID1, unsigned int ID2)
{

	unsigned int angle1 = get_angle(ID1);
	unsigned int angle2 = get_angle(ID2);
	if(angle1 > 0)
	{
		angle1 -= rotatespeed;
		angle2 -= rotatespeed;
		load_servo(ID1, angle1);
		load_servo(ID2, angle2);
		action();

	}	
	
}
/*
void check_servos(unsigned int ID1, unsigned int ID2)
{
	unsigned int angle1 = get_angle(ID1);
	unsigned int angle2 = get_angle(ID2);
	
	if(fabs((int)angle1 - (int)angle2) > 0.1)
	{
		log_error("Servos not in sync");
	}
}
*/



void move_joint(unsigned int joint, unsigned int angle)
{
	if(joint == 1)
	{
		move_servo(1, angle);
	}
	else if(joint == 2)
	{
		move_2servo(2,3,angle);
	}
	else if(joint == 3)
	{
		move_2servo(4,5,angle);
	}
	else if(joint == 4)
	{
		move_servo(6, angle);
	}
	else if(joint == 5)
	{
		move_servo(7,angle);
	}
	else if(joint == 6)
	{
		move_servo(8, angle);
	}

}


void add1degree_joint(unsigned int joint)
{
	if(joint == 1)
	{
		add1degree(1);
	}
	else if(joint == 2)
	{
		add1degree2(2,3);
	}
	else if(joint == 3)
	{
		add1degree2(4,5);
	}
	else if(joint == 4)
	{
		add1degree(6);
	}
	else if(joint == 5)
	{
		add1degree(7);
	}
	else if(joint == 6)
	{
		add1degree(8);
	}
	
}


void sub1degree_joint(unsigned int joint)
{
	if(joint == 1)
	{
		sub1degree(1);
	}
	else if(joint == 2)
	{
		sub1degree2(2,3);
	}
	else if(joint == 3)
	{
		sub1degree2(4,5);
	}
	else if(joint == 4)
	{
		sub1degree(6);
	}
	else if(joint == 5)
	{
		sub1degree(7);
	}
	else if(joint == 6)
	{
		sub1degree(8);
	}
}