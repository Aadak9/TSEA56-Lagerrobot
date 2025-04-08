#ifndef CONVERT_H
#define CONVERT_H

uint8_t AD_convert();
int digital_to_volt(int digital_out);
int convert_uint8_t(uint8_t num1);
int is_active_reflex();
int volt_to_dist(int digital_out);

#endif