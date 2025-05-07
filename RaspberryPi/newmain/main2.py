import spi as spi
import bluetooth as bt
import autonom as auto
import time
import threading
from collections import deque


size = 1024

has_seen_roadmark = False

def autonomous_loop(spi_styr, spi_sensor, KP, KD, nav_plan):
    global has_seen_roadmark
    roadmark_status1 = auto.check_roadmark(spi_sensor)
    roadmark_status2 = auto.check_roadmark(spi_sensor)
    
    if (roadmark_status1 == 3 or roadmark_status2 == 3):
        roadmark_status = 3
    else:
        roadmark_status = roadmark_status2
	
    #print(has_seen_roadmark)
    if(roadmark_status == 0):
        has_seen_roadmark = False
        auto.control_loop(spi_styr, spi_sensor, KP, KD)
    elif(roadmark_status == 1): # and dags att plocka vara
        #stanna och plocka vara
        auto.drive_fwd(spi_styr) # Kör förbi plockstaion
    elif(roadmark_status == 2): # and dags att plocka vara
        #stanna och plocka vara
        has_seen_plockstation = True
        auto.drive_fwd(spi_styr) # Kör förbi plockstaion
    elif(roadmark_status == 3 and not has_seen_roadmark): #sväng utifrån planerad väg
        has_seen_roadmark = True
        time.sleep(0.15)
        if(nav_plan):
            next_move = nav_plan.popleft()
            #print(next_move)
        else:
            print("Slut på styrbeslut")
        #Kolla om vi ska svänga eller ej
        
        if(next_move == "rakt"):
            print("rakt")
            auto.drive_fwd(spi_styr)

        elif(next_move == "vänster"):
           auto.rotate_left(spi_styr, spi_sensor)
            
        elif(next_move == "höger"):
            auto.rotate_right(spi_styr, spi_sensor)

    else:
        #print(nav_plan)
        auto.drive_fwd(spi_styr)
        





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
    #global Automatic
    client, _ = s.accept()
    print("Bluetooth connected")
    while True:
        #print("bluetooth listener körs")
        try:
            data = client.recv(size).hex()
            if data == "99": #Växla körläge
                if auto.Automatic:
                    spi_styr.xfer2([0])
                auto.Automatic = not auto.Automatic
                continue
            else:
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
    #global Automatic
    s = bt.init_bluetooth()
    spi_styr, spi_sensor = spi.initspi()

    #skapa styrbeslutslistan

    nav_plan = deque(["vänster", "vänster", "vänster", "vänster", "vänster", "vänster", "vänster", "vänster"]) #hårdkodad för nu

    bt_thread = threading.Thread(target=bluetooth_listener, args=(s, spi_styr, spi_sensor), daemon=True)
    bt_thread.start()

    KP, KD = 90, 100

    while True:
        old_Automatic = auto.Automatic
        if auto.Automatic:
            autonomous_loop(spi_styr, spi_sensor, KP, KD, nav_plan)
            time.sleep(0.005)
        if(old_Automatic == True and auto.Automatic == False):
            spi_styr.xfer2([0])



if __name__ == "__main__":
    main()
