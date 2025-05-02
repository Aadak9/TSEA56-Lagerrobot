import spidev
import time

 
spi = spidev.SpiDev()
spi.open(0, 1) #Öppna SPI-bussen
spi.max_speed_hz = 1000000 #Ställ in klockhastighet
spi.mode = 0
spi.bits_per_word = 8
data = 0

address = None

try:
	sensor_data = spi.xfer2([3])
		
except:
	print("Felaktig data")


while 1:	
		
	try:
		sensor_data1 = spi.xfer2([5])
		print(f"Sensorvärde: {sensor_data1}")
		time.sleep(0.01)
		
	except:
		print("Felaktig data")
	
		
			

			
#while 1:	
		
#	try:
#		start_gyro = spi.xfer2([2])
#		gyro_data = spi.xfer([4])
#		if (gyro_data >= 80):
#			end_gyro = spi.xfer([3])
#		
#		print(f"Sensorvärde: {sensor_data}")
#		time.sleep(0.01)
#	except:
#		print("Felaktig data")
	
