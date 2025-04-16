import spidev
import time
import socket
#from bluetooth_server import *
import test_sensor

import regler

hostMACaddress = 'B8:27:EB:E9:12:27'
port = 4
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACaddress, port))
s.listen(1)

spi_styr = spidev.SpiDev()
spi_sensor = spidev.SpiDev()

spi_styr.open(1, 0)
spi_sensor.open(0, 0) #Öppna SPI-bussen

spi_styr.max_speed_hz = 1000000 #Ställ in klockhastighet
spi_sensor.max_speed_hz = 1000000 #Ställ in klockhastighet

spi_styr.mode = 0
spi_sensor.mode = 0

spi_styr.bits_per_word = 8
spi_sensor.bits_per_word = 8

data = 0


address = None
Automatic = False

last_error = 0
KP = 0.5
KD = 1
time1 = time.time()

####
# kod för att skicka data till pc från dess begäran
while True:
	if Automatic:
		reflex_data = spi_sensor.xfer2(1) # skicka 1, få tillbaka reflexdata
		regler_error = reflex_data and 0b11111
		if(regler_error == 0):
			spi_styr.xfer2(1)
			
		else:
			time2 = time.time()
			output = PDController(regler_error, last_error, KP, KD, time2 - time1)
			time1 = time.time()
			last_error = regler_error
			
			spi_styr.xfer2(b'\x30')
			spi_styr.xfer2(output.to_bytes(1, 'big'))
			
			
		
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
		

