




void drive_and_turn(float turnvalue){	// turnvalue 0 sväng mycket vänster, 1 sväng mycket höger	OCR2A = turnvalue * 0xFE;	OCR2B = (1 - turnvalue) * 0xFE;	 		}void drive_fwd(){		// MÅSTE TESTA VILKEN DIR SOM ÄR FRAM OCH BAK	PORTA = 0b0010;	OCR2A = 0xFE; // Vänster kanske?	OCR2B = 0xFE;}void rotate_left_maybe(){		PORTA = 0b1010;	OCR2A = 0xFE; // Vänster kanske?	OCR2B = 0xFE; // Höger	}void rotate_right_maybe(){	PORTA = 0;	OCR2A = 0xFE; // Vänster kanske?	OCR2B = 0xFE; // Höger}void stop(){		OCR2A = 0x0;	OCR2B = 0x0;}