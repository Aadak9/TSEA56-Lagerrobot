#ifndef CONVERT_H
#define CONVERT_H

uint8_t AD_convert();
int convert_uint8_t(uint8_t num1);
int is_active_reflex();
int line_to_volt(int digital_out);
int volt_to_dist(int digital_out);

#endif