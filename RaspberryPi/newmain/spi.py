import spidev

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