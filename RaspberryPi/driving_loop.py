import spidev
import time
import regler as r

last_error = 0
KP = -200
KD = 50	
#time1 = time.time()
status = 0

def driving_automatic():

	try:
		#start_gyro = spi_sensor.xfer2([2])
		#gyro_data = (spi_sensor.xfer2([4])[0]*500/255)*180/3.14
		#print(gyro_data)
		#if (gyro_data >= 80):
			#end_gyro = spi_sensor.xfer2([3])
			
		regler_error_front = 6 - (spi_sensor.xfer2([1])[0])/2
		print(f"Front: {regler_error_front}")
		time.sleep(0.01)
	except:
		print(f"reglererror")
		
		
	try:
		regler_error_back = 6 - (spi_sensor.xfer2([2])[0])/2 # skicka 1, få tillbaka reflexdata
		#print(f"Back + 6 : {regler_error_back}")
		time.sleep(0.01)
	except:
		print(f"reglererror")

	#time2 = time.time()
	output = r.PDController(regler_error_front, regler_error_back, KP, KD)
	#time1 = time.time()
	#last_error = regler_error_front
	
	

	output *= 100
	output = int(output) 
	if (output > 0):
		status = 1
		output = abs(output)
	
	high = (output >> 8) & 0xFF	
	low = output & 0xFF
	
	
	spi_styr.xfer2([0x30, status, high, low])
				



def driving_manual():

	try:
		data = client.recv(size)
		print(data)
		if(data == b' '): #Ändrar aktuell armled
			data = client.recv(size) 
			print(data)
			try:
				response = spi_styr.xfer2([0x20] + list(data))

			except:
				print("invalid data 1")		
		else:
			try:	
				response = spi_styr.xfer2(data)
				print(response)
			except:
				print("invalid data 2")
	except:
		print("Disconnected, looking for new socket")   
		client, address = s.accept()                                                               
		
