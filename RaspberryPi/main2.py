
import spi as spi
import bluetooth as bt
import regler as r
import time
import threading

Automatic = False
size = 1024

def autonomous_loop(spi_styr, spi_sensor, KP, KD):
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


def bluetooth_control_loop(data, client, spi_styr, spi_sensor):
    try:
        time.sleep(0.01)
        if(data == "20"): #Ändrar aktuell armled
            data = client.recv(size) 
            try:
                response = spi_styr.xfer2([0x20] + list(data))
            except:
                print("invalid data 1")
                
        elif data == "60": #IR
            spi_sensor.xfer2([0])[0]
            time.sleep(0.01)
            response = spi_sensor.xfer2([0])[0]
            print(f"avstånd {response}")
            client.send(response.to_bytes(1, 'big'))
        elif data == "61": #Reflex
            spi_sensor.xfer2([1])[0]
            time.sleep(0.01)
            response = spi_sensor.xfer2([1])[0]
            print(f"reflex {response}")
            client.send(response.to_bytes(1, 'big'))
        elif data == "67": #kalibrera linjesensor
            response = spi_sensor.xfer2([7])
            time.sleep(0.01)
        
        elif data == "63": #Starta gyro
            spi_sensor.xfer2([3])
            time.sleep(0.01)
        elif data == "62": #Gyro
            response = spi_sensor.xfer2([5])[0]
            time.sleep(0.01)
            response = spi_sensor.xfer2([5])[0]
            client.send(response.to_bytes(1, 'big'))
        elif data == "64": #Stoppa gyro
            spi_sensor.xfer2([4])
            time.sleep(0.01)
            
        elif data == "65": #gaspådrag höger
            spi_styr.xfer2([0x41])[0]
            time.sleep(0.01)
            response = spi_styr.xfer2([0x41])[0]
            print(f"gas höger {response}")
            client.send(response.to_bytes(1, 'big'))
            
        elif data == "66": #gaspådrag vänster
            spi_styr.xfer2([0x40])[0]
            time.sleep(0.01)
            response = spi_styr.xfer2([0x40])[0]
            print(f"gas vänster {response}")
            client.send(response.to_bytes(1, 'big'))
            
        
        else:
            try:	
                response = spi_styr.xfer2(bytes.fromhex(data))
                print(response)
            except:
                print("invalid data 2")
        time.sleep(0.01)
    except:
        print("Disconnected, looking for new socket")            





def bluetooth_listener(s, spi_styr, spi_sensor):
    global Automatic
    client, _ = s.accept()
    print("Bluetooth connected")
    while True:
        try:
            data = client.recv(size).hex()
            if data == "99": #Växla körläge
                Automatic = not Automatic
                continue
            if not Automatic:
                bluetooth_control_loop(data, client, spi_styr, spi_sensor)
        except Exception as e:
            print(f"Bluetooth error: {e}")
            try:
                client.close()
            except:
                pass
            print("Waiting for connection...")
            client, _ = s.accept()
            print("Connected!")

def main():
    global Automatic
    s = bt.init_bluetooth()
    spi_styr, spi_sensor = spi.initspi()

    bt_thread = threading.Thread(target=bluetooth_listener, args=(s, spi_styr, spi_sensor), daemon=True)
    bt_thread.start()

    KP, KD = -200, 50

    while True:
        if Automatic:
           autonomous_loop(spi_styr, spi_sensor, KP, KD)
           time.sleep(0.005)


if __name__ == "__main__":
    main()
