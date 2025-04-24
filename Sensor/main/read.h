/*
 * read.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef READ_H
#define READ_H

int8_t read_reflex(int reflex_high);			// Läser av 11 sensorer och returnerar tyngdpunkt för reglering.
uint8_t read_IR();								// Returnerar avstånd.
uint8_t read_gyro();							// Returnerar digitalt värde på vinkelhastigheten.
void reset_w();									// Nollställer w_int.

#endif