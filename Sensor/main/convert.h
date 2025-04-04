#ifndef CONVERT_H
#define CONVERT_H

int convert_uint8_t(uint8_t num1);
int line_to_volt(int digital_out);
int volt_to_dist(int digital_out);
uint8_t AD_convert();

#endif