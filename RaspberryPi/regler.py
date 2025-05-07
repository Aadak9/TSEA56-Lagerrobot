import time

def PDController(front_error, back_error, KP, KD):
	derivative = KD * (front_error - back_error)
	proportional = KP * back_error
	output = proportional + derivative
	return output

