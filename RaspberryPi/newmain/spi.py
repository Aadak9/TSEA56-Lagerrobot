import spidev
import threading
import time
spi_lock = threading.Lock()


def initspi():
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
	return spi_styr, spi_sensor
    
    
def send_spi(spi, data):
	with spi_lock:
		if (type(data) == list):           
			spi.writebytes(data)
			time.sleep(0.001)
			response = spi.xfer2(data)[0]
		else:
			spi.writebytes([data])
			time.sleep(0.001)
			response = spi.xfer2([data])[0]
	return response


def load_angle(spi_styr, joint):
	with spi_lock:
		spi_styr.xfer2([0x50])
		time.sleep(0.001)
		spi_styr.xfer2([joint])
		time.sleep(0.001)
		spi_styr.xfer2([0x00])
		time.sleep(0.001)
		anglehigh = spi_styr.xfer2([0x00])[0]
		time.sleep(0.001)
		anglelow = spi_styr.xfer2([0x00])[0]
		angle = (anglehigh << 8) + anglelow
		return angle
		

