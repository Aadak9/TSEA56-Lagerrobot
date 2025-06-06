import spidev
import time
import regler as r
import spi as spi
Automatic = False


def check_roadmark(spi_sensor):
	time.sleep(0.001)
	roadmark_status = spi.send_spi(spi_sensor, 6)
	return roadmark_status


def check_obstacle(spi_sensor):
	time.sleep(0.001)
	distance = spi.send_spi(spi_sensor, 0)
	return (distance <= 10)


def control_loop(spi_styr, spi_sensor, KP, KD):
	global old_output
	try:
		time.sleep(0.001)
		regler_error_front = 6 - spi.send_spi(spi_sensor, 1)/2
		if(regler_error_front > 1):
			regler_error_front = 1
		elif(regler_error_front < -1):
			regler_error_front = -1
		regler_error_back = 6 - spi.send_spi(spi_sensor, 2)/2
		if(regler_error_back > 3):
			regler_error_back = 3
		elif(regler_error_back < -3):
			regler_error_back = -3
			
		output = r.PDController(regler_error_front, regler_error_back, KP, KD)
		output = int(output * 100)
		status = 1 if output > 0 else 0
		output = abs(output)

		high, low = (output >> 8) & 0xFF, output & 0xFF
		time.sleep(0.001)
		spi.send_spi(spi_styr, [0x30, status, high, low])
		time.sleep(0.001)
	except:
		print("Sensor error")


def rotate_left(spi_styr, spi_sensor):
	try:
		spi.send_spi(spi_sensor, 3)
		time.sleep(0.1)
		angle = 0
		while (angle < 60):
			angle = spi.send_spi(spi_sensor, 5)
			time.sleep(0.001)
			spi.send_spi(spi_styr, 0x2) #rotera vänster
			time.sleep(0.001)
			if not Automatic:
				break
		spi.send_spi(spi_sensor, 4)
	except:
		print("Gyrofel vänster rotation")


def rotate_right(spi_styr, spi_sensor):	
	try:
		spi.send_spi(spi_sensor, 3)
		time.sleep(0.1)
		angle = 0
		while (angle < 60):
			angle = spi.send_spi(spi_sensor, 5)
			spi.send_spi(spi_styr, 0x4) #rotera höger
			time.sleep(0.001)
			if not Automatic:
				break            
		spi.send_spi(spi_sensor, 4)
	except:
		print("Gyrofel höger rotation")   


def rotate_right_180(spi_styr, spi_sensor):
	try:
		rotate_right(spi_styr, spi_sensor)
		time.sleep(0.001)
		rotate_right(spi_styr, spi_sensor)
		
	except:
		print("Gyrofel höger rotation 180")  


def drive_fwd(spi_styr):
	spi.send_spi(spi_styr, 0x1)
	
def drive_bwd(spi_styr):
	spi.send_spi(spi_styr, 0x3)


def load_all_angles(spi_styr):
	angles = []
	with (open("sparade_vinklar.txt", "a")) as file:
		for i in range(1,9):
			angle = spi.load_angle(spi_styr, i)
			angles.append(str(angle))
			angles.append(" ")
		file.writelines(angles)
		file.write("\n")
	

def move_joint(spi_styr, joint, angle):
	spi_styr.xfer2([0x60])
	anglehigh = (angle >> 8) & 0xFF
	anglelow = angle & 0xFF
	spi_styr.xfer2([joint])
	time.sleep(0.001)
	spi_styr.xfer2([anglehigh])
	time.sleep(0.001)
	spi_styr.xfer2([anglelow])
	
	

	
	
	
def empty_basket3(spi_styr):
	
	time.sleep(0.5)
	move_joint(spi_styr, 4, 500)
	time.sleep(0.5)
	### OVANFÖRKORG ###
	

	move_joint(spi_styr, 1, 237)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 437)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 488)
	time.sleep(0.08)
	move_joint(spi_styr, 4, 874)
	time.sleep(0.5)
	move_joint(spi_styr, 5, 691)
	time.sleep(0.08)
	move_joint(spi_styr, 6, 512)
	time.sleep(1)
	
	move_joint(spi_styr, 4, 738)
	time.sleep(0.2)
	move_joint(spi_styr, 1, 228)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 464)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 391)
	time.sleep(0.5)
	move_joint(spi_styr, 5, 702)
	time.sleep(0.08)
	move_joint(spi_styr, 6, 512)
	time.sleep(0.4)
	
	
	move_joint(spi_styr, 1, 233)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 475)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 366)
	time.sleep(0.08)
	move_joint(spi_styr, 4, 711)
	time.sleep(0.08)
	move_joint(spi_styr, 5, 696)
	time.sleep(0.4)
	move_joint(spi_styr, 6, 100)
	time.sleep(0.9)
	
	move_joint(spi_styr, 1, 237)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 411)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 420)
	time.sleep(0.5)
	move_joint(spi_styr, 4, 733)
	time.sleep(0.08)
	move_joint(spi_styr, 5, 708)
	time.sleep(0.08)
	move_joint(spi_styr, 6, 100)
	time.sleep(0.3)
	
	
	move_joint(spi_styr, 1, 293)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 583)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 620)
	time.sleep(0.3)
	move_joint(spi_styr, 4, 789)
	time.sleep(0.08)
	move_joint(spi_styr, 5, 759)
	time.sleep(0.08)
	move_joint(spi_styr, 6, 100)
	time.sleep(1)
	
	
	
	move_joint(spi_styr, 1, 308)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 699)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 636)
	time.sleep(0.08)
	move_joint(spi_styr, 4, 766)
	time.sleep(0.08)
	move_joint(spi_styr, 5, 783)
	time.sleep(0.6)
	move_joint(spi_styr, 6, 512)
	time.sleep(0.3)
	
	
	move_joint(spi_styr, 1, 308)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 441)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 408)
	time.sleep(0.08)
	move_joint(spi_styr, 4, 300)
	time.sleep(0.08)
	move_joint(spi_styr, 5, 508)
	time.sleep(0.08)
	move_joint(spi_styr, 6, 512)
	time.sleep(1)
	
	move_joint(spi_styr, 1, 347)
	time.sleep(0.08)
	move_joint(spi_styr, 2, 190)
	time.sleep(0.08)
	move_joint(spi_styr, 3, 201)
	time.sleep(0.08)
	move_joint(spi_styr, 5, 508)
	time.sleep(0.08)
	move_joint(spi_styr, 6, 512)
	time.sleep(1)
	move_joint(spi_styr, 4, 671)
	time.sleep(2)
	
	
def pick_left(spi_styr):
	### Till varan ###
	time.sleep(0.5)
	move_joint(spi_styr, 4, 450)
	time.sleep(0.25)
	move_joint(spi_styr, 1, 657)
	time.sleep(1.5)
	move_joint(spi_styr, 2, 600)
	time.sleep(0.25)
	move_joint(spi_styr, 3, 380)
	time.sleep(0.5)
	move_joint(spi_styr, 6, 512)
	time.sleep(0.25)
	move_joint(spi_styr, 4, 575)
	time.sleep(0.5)
	move_joint(spi_styr, 5, 502)
	time.sleep(0.25)

	
	time.sleep(2)
	
	### PLOCK ###
	
	move_joint(spi_styr, 6, 150)
	time.sleep(0.5)
	
	### Delsteg 2 ###
	
	move_joint(spi_styr, 2, 370)
	time.sleep(0.4)
	move_joint(spi_styr, 3, 390)
	time.sleep(0.25)
	move_joint(spi_styr, 4, 800)
	time.sleep(0.25)
	move_joint(spi_styr, 5, 531)
	time.sleep(0.2)
	move_joint(spi_styr, 6, 150)
	time.sleep(0.25)	
	move_joint(spi_styr, 1, 359)
	time.sleep(1.6)
	
	
	### Släpp ###
	move_joint(spi_styr, 6, 512)
	time.sleep(0.2)
	move_joint(spi_styr, 4, 600)
	time.sleep(0.7)
	### Tillbaka till start ###
	
	move_joint(spi_styr, 1, 347)
	time.sleep(0.25)
	move_joint(spi_styr, 2, 190)
	time.sleep(0.25)
	move_joint(spi_styr, 3, 201)
	time.sleep(0.5)
	move_joint(spi_styr, 5, 508)
	time.sleep(0.25)
	move_joint(spi_styr, 6, 512)
	time.sleep(1)
	move_joint(spi_styr, 4, 671)
	time.sleep(0.25)
	
	
def pick_right(spi_styr):
	### Till varan ###
	time.sleep(0.5)
	move_joint(spi_styr, 4, 450)
	time.sleep(0.25)
	move_joint(spi_styr, 1, 46)
	time.sleep(1.5)
	move_joint(spi_styr, 2, 600)
	time.sleep(0.25)
	move_joint(spi_styr, 3, 380)
	time.sleep(0.5)
	move_joint(spi_styr, 6, 512)
	time.sleep(0.25)
	move_joint(spi_styr, 4, 575)
	time.sleep(0.5)
	move_joint(spi_styr, 5, 502)
	time.sleep(0.25)

	
	time.sleep(2)
	
	### PLOCK ###
	
	move_joint(spi_styr, 6, 150)
	time.sleep(0.5)
	
	### Delsteg 2 ###
	
	move_joint(spi_styr, 2, 370)
	time.sleep(0.25)
	move_joint(spi_styr, 3, 390)
	time.sleep(0.25)
	move_joint(spi_styr, 4, 800)
	time.sleep(0.25)
	move_joint(spi_styr, 5, 531)
	time.sleep(0.2)
	move_joint(spi_styr, 6, 150)
	time.sleep(0.25)	
	move_joint(spi_styr, 1, 359)
	time.sleep(1.6)
	
	
	### Släpp ###
	move_joint(spi_styr, 6, 512)
	time.sleep(0.2)
	move_joint(spi_styr, 4, 600)
	time.sleep(0.7)
	### Tillbaka till start ###
	
	move_joint(spi_styr, 1, 347)
	time.sleep(0.25)
	move_joint(spi_styr, 2, 190)
	time.sleep(0.25)
	move_joint(spi_styr, 3, 201)
	time.sleep(0.5)
	move_joint(spi_styr, 5, 508)
	time.sleep(0.25)
	move_joint(spi_styr, 6, 512)
	time.sleep(1)
	move_joint(spi_styr, 4, 671)
	time.sleep(0.25)
	
	
