




void drive_and_turn(unsigned float turnvalue){	// turnvalue 0 sv�ng mycket v�nster, 1 sv�ng mycket h�ger	OCR2A = turnvalue * 0xFE;	OCR2B = (1 - turnvalue) * 0xFE;	 		}void drive_fwd(){		// M�STE TESTA VILKEN DIR SOM �R FRAM OCH BAK		OCR2A = 0xFE; // V�nster kanske?	OCR2B = 0xFE; // H�ger}void rotate_left_maybe(){		PORTA = 0b1010;	drive_fwd();	}void rotate_right_maybe(){	PORTA = 0;	drive_fwd();}void stop(){		OCR2A = 0x0;	OCR2B = 0x0;}