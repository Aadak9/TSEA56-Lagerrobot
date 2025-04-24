#ifndef CONVERT_H
#define CONVERT_H

uint8_t AD_convert();
float digital_to_volt(int digital_out);
int convert_uint8_t(uint8_t num);
int is_active_reflex(int reflex_high);
int volt_to_dist(int digital_out);
int dist_table(int indata);
int w_table(int indata);
int linear_interpolation(int indata);

#endif