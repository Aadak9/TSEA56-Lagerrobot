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

spi = spidev.SpiDev()
spi.open(0, 0) #Öppna SPI-bussen
spi.max_speed_hz = 1000000 #Ställ in klockhastighet
spi.mode = 0
spi.bits_per_word = 8
data = 0

address = None
Automatic = False

####
# kod för att skicka data till pc från dess begäran
while True:
	
	
	try:
			
		client, address = s.accept()
		print("Ansluten till", address)
		
		while True:
			data = client.recv(size)
			print(data)
			
			if not data:
				print("inget data mottaget")
				break
				
			try:
				received_value = data[0]
				print("Mottagen data: ", received_value)
			
			except UnicodeDecodeError:
				print("Kunde inte avkoda")
				continue
				
				
			if received_value == 255:  ##ändra sen, endast grundläggande
				response = spi.xfer2(0)
				print(response)
			elif recieve_value == 0:
				response = "0"
				client.send(response.encode('utf-8'))
				break
			else:
				response = "3"
				print(response)
					
					
			client.send(response.encode('utf-8'))
			
		close_connection()
						
					
	except:
		print("Disconnected, looking for new socket")
		s.close()

def close_connection():
	client.close()
	s.close()
	spi.close()
	sys.exit()
	
#######
		
