

volatile uint8_t speed = 120;



void drive_and_turn(float turnvalue){	// turnvalue 0 sv�ng mycket v�nster, 1 sv�ng mycket h�ger	OCR2A = turnvalue * 0xFE;	OCR2B = (1 - turnvalue) * 0xFE;	 		}void drive_fwd(){		PORTA = 0b1000;	OCR2A = speed; // V�nster	OCR2B = speed; // H�ger}void reverse(){		PORTA = 0b0010;	OCR2A = speed; // V�nster	OCR2B = speed; //H�ger}void rotate_left_maybe(){	PORTA = 0;	OCR2A = speed; // V�nster	OCR2B = speed; // H�ger	}void rotate_right_maybe(){		PORTA = 0b1010;	OCR2A = speed; // V�nster	OCR2B = speed; // H�ger}void stop(){		OCR2A = 0x0;	OCR2B = 0x0;}void increase_speed(){	if(speed < 120)	{		speed += 40;	}}void decrease_speed(){	if(speed > 40)	{		speed -= 40;	}		}