import threading
import time

import driving_loop as dl
import send_data as sd
import mode

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
Automatic = False

def driving_mode():
	while True:
		print("Loop 1 kör...")
		Automatic = mode.active_mode()
		time.sleep(0.01)
		
		
def driving():
	while True:
		print("Loop 2 kör...")
		sd.receive_and_send_data()
		if Automatic:
			dl.driving_automatic()
		else:
			dl.driving_manual()
		time.sleep(0.001)
		
#def handle_data():
#	while True:
#		with slave_lock:
#			print("Loop 3 kör..")
#			sd.receive_and_send_data()
#		time.sleep(1)
		
t1 = threading.Thread(target=driving_mode)
t2 = threading.Thread(target=driving)
#t3 = threading.Thread(target=handle_data)

t1.start()
t2.start()
#t3.start()


