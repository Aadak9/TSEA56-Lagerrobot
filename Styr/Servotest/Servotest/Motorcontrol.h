

volatile uint8_t speed = 120;



void drive_and_turn(float turnvalue){	// turnvalue 0 sväng mycket vänster, 1 sväng mycket höger	OCR2A = turnvalue * 0xFE;	OCR2B = (1 - turnvalue) * 0xFE;	 		}void drive_fwd(){		PORTA = 0b1000;	OCR2A = speed; // Vänster	OCR2B = speed; // Höger}void reverse(){		PORTA = 0b0010;	OCR2A = speed; // Vänster	OCR2B = speed; //Höger}void rotate_left_maybe(){	PORTA = 0;	OCR2A = speed; // Vänster	OCR2B = speed; // Höger	}void rotate_right_maybe(){		PORTA = 0b1010;	OCR2A = speed; // Vänster	OCR2B = speed; // Höger}void stop(){		OCR2A = 0x0;	OCR2B = 0x0;}void increase_speed(){	if(speed < 120)	{		speed += 40;	}}void decrease_speed(){	if(speed > 40)	{		speed -= 40;	}		}