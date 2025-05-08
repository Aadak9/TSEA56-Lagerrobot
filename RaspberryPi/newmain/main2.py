import spi as spi
import bluetooth as bt
import autonom as auto
import time
import threading
from collections import deque
import handle_map as hm


size = 1024

has_seen_roadmark = False

def autonomous_loop(spi_styr, spi_sensor, KP, KD, nav_plan):
    global has_seen_roadmark
    roadmark_status = auto.check_roadmark(spi_sensor)
    
    if(auto.check_obstacle(spi_sensor)):
        auto.rotate_left(spi_styr, spi_sensor)
        auto.rotate_left(spi_styr, spi_sensor)

    if(roadmark_status == 0):
        has_seen_roadmark = False
        auto.control_loop(spi_styr, spi_sensor, KP, KD)
    elif(roadmark_status == 1): # and dags att plocka vara
        #stanna och plocka vara
        auto.drive_fwd(spi_styr) # Kör förbi plockstaion
    elif(roadmark_status == 2): # and dags att plocka vara
        #stanna och plocka vara
        auto.drive_fwd(spi_styr) # Kör förbi plockstaion
    elif(roadmark_status == 3 and not has_seen_roadmark): #sväng utifrån planerad väg
        has_seen_roadmark = True
        time.sleep(0.14)
        if(nav_plan):
            next_move = nav_plan.popleft()
        else:
            print("Slut på styrbeslut")
        #Kolla om vi ska svänga eller ej
        
        if(next_move == "rakt"):
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
        if(data == "20"): #Ändrar aktuell armled
            data = client.recv(size) 
            try:
                spi.send_spi(spi_styr, [0x20] + list(data))
            except:
                print("invalid data 1")
                
        elif data == "60": #IR
            response = spi.send_spi(spi_sensor, 0)
            print(f"avstånd {response}")
            client.send(response.to_bytes(1, 'big'))
        elif data == "61": #Reflex
            response = spi.send_spi(spi_sensor, 1)
            print(f"reflex {response}")
            client.send(response.to_bytes(1, 'big'))
        elif data == "67": #kalibrera linjesensor
            spi.send_spi(spi_sensor, 7)
            time.sleep(0.01)
        
        elif data == "63": #Starta gyro
            spi.send_spi(spi_sensor, 3)
            time.sleep(0.01)
        elif data == "62": #Gyro
            response = spi.send_spi(spi_sensor, 5)
            client.send(response.to_bytes(1, 'big'))
        elif data == "64": #Stoppa gyro
            spi.send_spi(spi_sensor, 4)
            time.sleep(0.01)
            
        elif data == "65": #gaspådrag höger
            response = spi.send_spi(spi_styr, 0x41)
            print(f"gas höger {response}")
            client.send(response.to_bytes(1, 'big'))
            
        elif data == "66": #gaspådrag vänster
            response = spi.send_spi(spi_styr, 0x40)
            print(f"gas vänster {response}")
            client.send(response.to_bytes(1, 'big'))
            
        
        else:
            try:
                response = spi.send_spi(spi_styr, int(data, 16))	
            except:
                print("invalid data 2")
    except:
        print("Disconnected, looking for new socket")            




def bluetooth_listener(s, spi_styr, spi_sensor):
    #global Automatic
    global nav_plan
    client, _ = s.accept()
    print("Bluetooth connected")
    while True:
        #print("bluetooth listener körs")
        try:
            data = client.recv(1).hex()
            if data == "99": #Växla körläge
                if auto.Automatic:
                    spi.send_spi(spi_styr, 0)
                else:
                    nav_plan = hm.update_path(client)
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
    global nav_plan
    s = bt.init_bluetooth()
    spi_styr, spi_sensor = spi.initspi()

    #skapa styrbeslutslistan

    nav_plan = deque(["vänster", "rakt", "höger", "höger", "vänster", "vänster", "vänster", "vänster" , "höger", "vänster", "höger", "vänster" ]) #hårdkodad för nu

    bt_thread = threading.Thread(target=bluetooth_listener, args=(s, spi_styr, spi_sensor), daemon=True)
    bt_thread.start()

    KP, KD = 100, 100

    while True:
        old_Automatic = auto.Automatic
        if auto.Automatic:
            autonomous_loop(spi_styr, spi_sensor, KP, KD, nav_plan)
            time.sleep(0.005)
        if(old_Automatic == True and auto.Automatic == False):
            spi.send_spi(spi_styr, 0)



if __name__ == "__main__":
    main()
