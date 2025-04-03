import spidev

spi = spidev.SpiDev()
spi.open(0,0) #öppna spi-nussen (buss 0, device 0)
spi.max_speed_hz = 50000 #klockhast

response = spi.xfer2([0x42]) #skick abyte och få svar
print(response)
spi.close()