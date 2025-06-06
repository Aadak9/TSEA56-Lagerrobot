def PDController(front_error, back_error, KP, KD):
	return KD * (front_error - back_error) + KP * back_error