import spidev
import time
import regler as r
import spi as spi
Automatic = False

def check_roadmark(spi_sensor):
    time.sleep(0.001)
    roadmark_status = spi.send_spi(spi_sensor, 6)
    return roadmark_status

def check_obstacle(spi_sensor):
    time.sleep(0.001)
    distance = spi.send_spi(spi_sensor, 0)
    return (distance <= 10)


def control_loop(spi_styr, spi_sensor, KP, KD):
    try:
        time.sleep(0.001)
        regler_error_front = 6 - spi.send_spi(spi_sensor, 1)/2
        regler_error_back = 6 - spi.send_spi(spi_sensor, 2)/2
        
        output = r.PDController(regler_error_front, regler_error_back, KP, KD)
        output = int(output * 100)
        status = 1 if output > 0 else 0
        output = abs(output)

        high, low = (output >> 8) & 0xFF, output & 0xFF
        time.sleep(0.001)
        #spi_styr.xfer2([0x30, status, high, low])
        spi.send_spi(spi_styr, [0x30, status, high, low])
        time.sleep(0.001)
    except:
        print("Sensor error")

def rotate_left(spi_styr, spi_sensor):
    try:
        spi.send_spi(spi_sensor, 3)
        time.sleep(0.05)
        angle = 0
        while (angle < 60):
            angle = spi.send_spi(spi_sensor, 5)
            time.sleep(0.001)
            spi.send_spi(spi_styr, 0x2) #rotera vänster
            time.sleep(0.001)
            if not Automatic:
                break
        spi.send_spi(spi_sensor, 4)
    except:
        print("gyrofel")


def rotate_right(spi_styr, spi_sensor):	
    try:
        spi.send_spi(spi_sensor, 3)
        time.sleep(0.05)
        angle = 0
        while (angle < 60):
            angle = spi.send_spi(spi_sensor, 5)
            spi.send_spi(spi_styr, 0x4) #rotera höger
            time.sleep(0.001)
            if not Automatic:
                break            
        spi.send_spi(spi_sensor, 4)
    except:
        print("gyrofel")   


def drive_fwd(spi_styr):
	spi.send_spi(spi_styr, 0x1)
    
