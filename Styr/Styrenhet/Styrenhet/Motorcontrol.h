




#define basespeed 60
#define reglerspeed 85
#define driveturnspeed 170
#define turnspeed 125

volatile uint8_t speed = basespeed;

void drive_and_turn(float turnvalue)
{
	PORTA = 0b1000;
	speed = reglerspeed;
	if(speed + turnvalue < 0xFF && speed + turnvalue > 0) // testa att bara �ka en sida ist�llet f�r att �ka och minska 
	{
		if(turnvalue > 0)
		{
			OCR2A = speed + turnvalue;
		}
		else if(turnvalue < 0)
		{
			OCR2A = speed + turnvalue * 1.25;
		} 
		else
		{
			OCR2A = speed;
		}
	}
	else if(speed + turnvalue > 0xFE)
	{
		OCR2A = 0xFE;
	}
	else if(speed + turnvalue < 0)
	{
		OCR2A = 0;
	}
	
	
	
	if(speed - turnvalue < 0xFF && speed - turnvalue > 0)
	{
		if(turnvalue < 0)
		{
			OCR2B = speed - turnvalue;
		} 
		else if(turnvalue > 0)
		{
			OCR2B = speed - turnvalue * 1.25;
		}
		else
		{
			OCR2B = speed;
		}
		
	}
	else if(speed - turnvalue > 0xFE)
	{
		OCR2B = 0xFE;
	}
	else if(speed - turnvalue < 0)
	{
		OCR2B = 0;
	}
	
}



void drive_fwd()
{
	speed = basespeed;
	PORTA = 0b1000;

	OCR2A = speed; // V�nster
	OCR2B = speed; // H�ger

}


void fwd_right()
{
	speed = driveturnspeed;
	PORTA = 0b1000;
	
	OCR2A = speed;
	OCR2B = 2/3 * speed;
	
	
}


void fwd_left()
{
	speed = driveturnspeed;
	PORTA = 0b1000;
	
	OCR2A = 2/3*speed;
	OCR2B = speed;
	
}


void reverse()
{
	speed = basespeed;
	PORTA = 0b0010;

	OCR2A = speed; // V�nster
	OCR2B = speed; //H�ger

}


void rotate_left()
{
	speed = turnspeed;
	PORTA = 0;
	OCR2A = speed; // V�nster
	OCR2B = speed; // H�ger
	
}


void rotate_right()
{

	speed = turnspeed;
	PORTA = 0b1010;
	OCR2A = speed; // V�nster
	OCR2B = speed; // H�ger
}


void stop()
{
	
	OCR2A = 0x0;
	OCR2B = 0x0;
}



void increase_speed()
{
	if(speed < 120)
	{
		speed += 40;
	}
}


void decrease_speed()
{
	if(speed > 40)
	{
		speed -= 40;
	}
	
	
}

