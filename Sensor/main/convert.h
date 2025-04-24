/*
 * convert.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef CONVERT_H
#define CONVERT_H

uint8_t AD_convert();								//	AD-omvandlar.
float digital_to_volt(int digital_out);				//	Gör om AD-värdet till volt.					
int is_active_reflex(int reflex_high);				//	Returnerar 0 för icketejp, 1 för tejp.
int linear_interpolation(int indata);				//	Linjärinterpolerar för att få fram avstånd.

#endif