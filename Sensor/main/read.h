/*
 * read.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef READ_H
#define READ_H

int8_t read_reflex(int reflex_high);			// L�ser av 11 sensorer och returnerar tyngdpunkt f�r reglering.
uint8_t read_IR();								// Returnerar avst�nd.
uint8_t read_gyro();							// Returnerar digitalt v�rde p� vinkelhastigheten.
void reset_w();									// Nollst�ller w_int.

#endif