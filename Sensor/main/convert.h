/*
 * convert.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef CONVERT_H
#define CONVERT_H

uint8_t AD_convert();								// AD converting.
float digital_to_volt(int digital_out);				// Translate AD value to volt.					
int is_active_reflex(int reflex_high);				// Return 0 for no tape, 1 for tape.
int linear_interpolation(int indata);				// Linear interpolation to get distance from IR-sensor.

#endif