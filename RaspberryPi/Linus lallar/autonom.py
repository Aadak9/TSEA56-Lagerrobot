import spidev
import time
import regler as r

def check_roadmark(spi_sensor):
    spi_sensor.xfer2([6])
    roadmark_status = spi_sensor.xfer2([6]) #Be om roadmark status
    return roadmark_status



def control_loop(spi_styr, spi_sensor, KP, KD):
    try:
        spi_sensor.xfer2([1])
        regler_error_front = 6 - (spi_sensor.xfer2([1])[0])/2
        time.sleep(0.01)
        spi_sensor.xfer2([2])        
        regler_error_back = 6 - (spi_sensor.xfer2([2])[0])/2
        output = r.PDController(regler_error_front, regler_error_back, KP, KD)
        output = int(output * 100)
        status = 1 if output > 0 else 0
        output = abs(output)

        high, low = (output >> 8) & 0xFF, output & 0xFF
        spi_styr.xfer2([0x30, status, high, low])
    except:
        print("Sensor error")

def rotate_left(spi_styr, spi_sensor):
    try:
        spi_sensor.xfer2([3])
        angle = 0
        while (angle < 60):
            time.sleep(0.01)
            angle = spi_sensor.xfer2([5])[0]
            time.sleep(0.01)
            angle = spi_sensor.xfer2([5])[0]
            time.sleep(0.01)
            spi_styr.xfer2([0x2]) #rotera vänster
            print(angle)
        spi_sensor.xfer2([4])
    except:
        print("gyrofel")


def rotate_right(spi_styr, spi_sensor):
    try:
        spi_sensor.xfer2([3])
        angle = 0
        while (angle < 60):
            time.sleep(0.01)
            angle = spi_sensor.xfer2([5])[0]
            time.sleep(0.01)
            angle = spi_sensor.xfer2([5])[0]
            time.sleep(0.01)
            spi_styr.xfer2([0x4]) #rotera höger
            print(angle)
        spi_sensor.xfer2([4])
    except:
        print("gyrofel")   


def drive_fwd(spi_styr):
    spi_styr.xfer2([0x1])
    