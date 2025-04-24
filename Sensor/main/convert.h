/*
 * convert.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef CONVERT_H
#define CONVERT_H

uint8_t AD_convert();								//	AD-omvandlar.
float digital_to_volt(int digital_out);				//	G�r om AD-v�rdet till volt.					
int is_active_reflex(int reflex_high);				//	Returnerar 0 f�r icketejp, 1 f�r tejp.
int linear_interpolation(int indata);				//	Linj�rinterpolerar f�r att f� fram avst�nd.

#endif