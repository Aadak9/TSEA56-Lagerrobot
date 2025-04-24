/*
 * init.h
 *
 * Created: 2025-04-02 15:58:02
 * Author : andno773, sigry751
 */

#ifndef INIT_H
#define INIT_H

void init_IR();							//	Initializing IR-sensor.
void init_gyro();						//	Initializing gyro.	
void init_reflex();						//	Initializing line sensor.
void init_interrupt();					//	Initializing interrupt.	
void init_SPI();						//	Initializing SPI-bus.
void init_timer();						//	Initializing gyro-timer.
int init_reflex_calibrate();			//	Initializing Calibrating tape value for line sensor.

#endif