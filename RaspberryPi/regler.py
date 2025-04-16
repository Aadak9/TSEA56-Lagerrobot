import time

def PDController(error, previous_error, KP, KD, dt):
	proportional = KP * error
	derivative = KD *(error - previous_error) / dt
	output = proportional + derivative
	return output

