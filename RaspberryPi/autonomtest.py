import spidev
import time
import socket
#from bluetooth_server import *
#import test_sensor

import regler as r

hostMACaddress = 'B8:27:EB:E9:12:27'
port = 4
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACaddress, port))
s.listen(1)

spi_styr = spidev.SpiDev()
spi_sensor = spidev.SpiDev()

spi_styr.open(0, 0)
spi_sensor.open(0, 1) #Öppna SPI-bussen

spi_styr.max_speed_hz = 1000000 #Ställ in klockhastighet
spi_sensor.max_speed_hz = 1000000 #Ställ in klockhastighet

spi_styr.mode = 0
spi_sensor.mode = 0

spi_styr.bits_per_word = 8
spi_sensor.bits_per_word = 8

data = 0


address = None
Automatic = True

last_error = 0
KP = 0.5
KD = 1
time1 = time.time()
status = 0

####
# kod för att skicka data till pc från dess begäran
while True:
	if Automatic:
		try:
			
			regler_error = 6 - spi_sensor.xfer2([1])[0] # skicka 1, få tillbaka reflexdata
			time.sleep(0.001)
		except:
			regler_error1 = 10
		print(f"reglererror: {regler_error}")
		if(regler_error == 0):
			
			spi_styr.xfer2([1])
			
		else:
			
			time2 = time.time()
			
			output = r.PDController(regler_error, last_error, KP, KD, time2 - time1)
			time1 = time.time()
			last_error = regler_error
			
			
		
			output *= 100
			output = int(output)
			if (output < 0):
				status = 1
				output = abs(output)
			
			high = (output >> 8) & 0xFF
			
			low = output & 0xFF
			
			
			response = spi_styr.xfer2([0x30, status, high, low])
			print(response)
			#spi_styr.xfer2([status, high, low])
			
			
		
	else:


		try:
			client, address = s.accept()
			while True:
				data = client.recv(size)		
				print(data)			
				try:	
					spi.xfer2(data)
				except:
					print("invalid data")
		except:
			print("Disconnected, looking for new socket")
		

def close_connection():
	client.close()
	s.close()
	spi.close()
	sys.exit()
	
#######
		

