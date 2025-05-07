import time

def PDController(front_error, back_error, KP, KD):
	proportional = KP * (front_error - back_error)
	derivative = KD * front_error
	output = proportional + derivative
	return output

