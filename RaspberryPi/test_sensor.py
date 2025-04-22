import spidev
import time

 
spi = spidev.SpiDev()
spi.open(0, 1) #Öppna SPI-bussen
spi.max_speed_hz = 1000000 #Ställ in klockhastighet
spi.mode = 0
spi.bits_per_word = 8
data = 0

address = None




while 1:	
		
	try:
		sensor_data = spi.xfer2([1])
		print(f"Sensorvärde: {sensor_data}")
		time.sleep(1)
	except:
		print("Felaktig data")
			

			

	
