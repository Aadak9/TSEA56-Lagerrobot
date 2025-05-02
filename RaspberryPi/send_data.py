import spidev
import time
import socket
#from bluetooth_server import *


import regler

hostMACaddress = 'B8:27:EB:E9:12:27'
port = 4
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACaddress, port))
s.listen(1)

spi = spidev.SpiDev()
spi.open(0, 1) #Öppna SPI-bussen
spi.max_speed_hz = 1000000 #Ställ in klockhastighet
spi.mode = 0
spi.bits_per_word = 8
data = 0

address = None
Automatic = False

####
# kod för att skicka data till pc från dess begäran
def receive_and_send_data():
	
	while True:
		
		
		try:
				
			client, address = s.accept()
			print("Ansluten till", address)
			
			while True:
				data = client.recv(size)
				print(data)
				
				if not data:
					print("inget data mottaget")
					client.close()
					break
					
				try:
					received_value = data[0]
					print("Mottagen data: ", received_value)
				
				except Exception as e:
					print("Kunde inte avkoda", e)
					continue
					
					
				if received_value == 0:  #IR
					response = spi.xfer([0])[0]
					print(response)
				elif received_value == 1: #Reflex
					response = 1
					print(response)
				elif received_value == 2:  #Gyro
					response = 2
				else:
					response = "3"
					print(response)
						
				client.send(response.to_bytes(1, 'big'))	
				#client.send(response.encode('utf-8'))
				
		
							
						
		except Exception as e:
			print("Disconnected, looking for new socket", e)

def close_connection():
	client.close()
	spi.close()
	sys.exit()
	
#######
		
