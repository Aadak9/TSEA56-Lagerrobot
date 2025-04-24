/*
 * init.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef INIT_H
#define INIT_H

void init_IR();							//	Initierar ir-sensor.
void init_gyro();						//	Initierar gyro.	
void init_reflex();						//	Initierar linjesensor.
void init_interrupt();					//	Initierar avbrott.	
void init_SPI();						//	Initierar SPI-bussen.
void init_timer();						//	Initierar gyro-timer.
int init_reflex_calibrate();			//	Initierar kalibreringsfunktion för linjesensor.

#endif