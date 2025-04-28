/*
 * read.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef READ_H
#define READ_H

int8_t read_line_front(int reflex_high);			// Reads 11 sensors and returns the center of mass for control and roadmarks.
int8_t read_line_back(int reflex_high);             // Reads 11 sensors and returns the center of mass for control.
uint8_t read_IR();								    // Return distance in cm.
int8_t read_gyro();							        // Return digital value from angle velocity.
void reset_w();									    // Resets w_int.

#endif