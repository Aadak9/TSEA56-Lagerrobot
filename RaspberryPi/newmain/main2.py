import spi as spi
import bluetooth as bt
import autonom as auto
import time
import threading
from collections import deque
import handle_map as hm
import json
import fastest_way3 as fw

global next_move
next_move = None
global new_plan
new_plan = False
global goal_collected
goal_collected = False
global nodeorder
nodeorder = []
size = 1024

has_seen_roadmark = False
global obstacles
obstacles = []

def autonomous_loop(spi_styr, spi_sensor, KP, KD):
    global nav_plan
    global new_plan
    global goal_collected
    global has_seen_roadmark
    global nodeorder
    global obstacles
    roadmark_status = auto.check_roadmark(spi_sensor)
    next_move = nav_plan[0]
    målnoder = hm.get_målnoder()
    print("målnoder", målnoder)
    if(auto.check_obstacle(spi_sensor)):
        spi.send_spi(spi_styr, 0)#stanna
        
        current_node, next_node = fw.find_location(nav_plan, nodeorder) #current_node = den noden man åker tillbaka till efter påkommet hinder, next_node = den man inte kom till
        print("currentnode", current_node)
        print("nextnode", next_node)  
        obstacles.append([current_node, next_node])
        print(obstacles)
        målnoder[1] = [current_node]
        print("målnoder efter hinder", målnoder)
        
        nav_plan, nodeorder = hm.update_path_obstacles(obstacles, målnoder) #måste komma åt målnoder på nåt sätt
        print("navplan ny", nav_plan)        
        new_plan = True
        auto.rotate_right_180(spi_styr, spi_sensor)
        
    if(roadmark_status == 0):
        has_seen_roadmark = False
        auto.control_loop(spi_styr, spi_sensor, KP, KD)
    elif(roadmark_status == 1): # dags att plocka vara åt höger
        if(next_move == "plocka"):
			goal_collected = True
            spi.send_spi(spi_styr, 0) #stanna och plocka vara
            time.sleep(2) #här ska den plocka upp ist för att stanna sen
            current_node, next_node = fw.find_location(nav_plan, nodeorder) 
            hm.remove_goal_node(current_node, next_node)
            next_move = nav_plan.popleft()
            if(nav_plan[0] == "vänd"):
                auto.rotate_right_180(spi_styr, spi_sensor)
                nav_plan.popleft()
        else:
	        auto.drive_fwd(spi_styr) # Kör förbi plockstaion
    elif(roadmark_status == 2): # dags att plocka vara åt vänster
        if(next_move == "plocka"):
			goal_collected = True 
            spi.send_spi(spi_styr, 0) #stanna och plocka vara
            time.sleep(2)
            current_node, next_node = fw.find_location(nav_plan, nodeorder) 
            hm.remove_goal_node(current_node, next_node)
            next_move = nav_plan.popleft()
            if(nav_plan[0] == "vänd"):
                auto.rotate_right_180(spi_styr, spi_sensor)
                nav_plan.popleft()
        else:
	        auto.drive_fwd(spi_styr) # Kör förbi plockstaion
    elif(roadmark_status == 3 and not has_seen_roadmark): #sväng utifrån planerad väg
        has_seen_roadmark = True
        time.sleep(0.125)
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
        elif(next_move == "lämna"):
            spi.send_spi(spi_styr, 0)
			

    else:
        #print(nav_plan)
        auto.drive_fwd(spi_styr)
        





def bluetooth_control_loop(data, client, spi_styr, spi_sensor):
    global new_plan
    global nav_plan
    global målnoder
    global goal_collected
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
            auto.load_all_angles(spi_styr)
            #spi.send_spi(spi_sensor, 7)
            #time.sleep(0.01)
        
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
            
        elif data == "80": #skicka styrbeslut
            print("hej1")
            print(new_plan)
            
            if new_plan:
                print("4" + str(nav_plan))
                client.send(b'\x01')
                print("hej2")
                hm.send_map(client)
                print("skickat all data")
                new_plan = False
            else:
                client.send(b'\x00')
        elif data == "81":
			if goal_collected:
				client.send(b'\x01')
				goal_collected = False
			else:
				client.send(b'\x00')
        
        else:
            try:
                response = spi.send_spi(spi_styr, int(data, 16))	
            except:
                print("invalid data 2")
    except:
        print("Disconnected, looking for new socket")            




def bluetooth_listener(s, spi_styr, spi_sensor):
    #global Automatic
    global new_plan
    global nav_plan
    global nodeorder
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
                    nav_plan, nodeorder = hm.update_path(client)
                    new_plan = True
                    print(nav_plan)
                    
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
    nav_plan = 0
    s = bt.init_bluetooth()
    spi_styr, spi_sensor = spi.initspi()

    #skapa styrbeslutslistan

    #nav_plan = deque(["vänster", "höger", "rakt", "höger", "höger", "rakt", "vänster" ,"rakt" ,"rakt","rakt"]) #hårdkodad för nu

    bt_thread = threading.Thread(target=bluetooth_listener, args=(s, spi_styr, spi_sensor), daemon=True)
    bt_thread.start()

    KP, KD = 100, 100

    """
    auto.move_joint(spi_styr, 3, 500)
    time.sleep(0.001)
    auto.move_joint(spi_styr, 1, 0)
    time.sleep(0.001)
    auto.move_joint(spi_styr, 5, 0)
    time.sleep(2)
    auto.move_joint(spi_styr, 2, 500)
    time.sleep(0.001)
    auto.move_joint(spi_styr, 6, 100)
    time.sleep(0.001)
    auto.move_joint(spi_styr, 4, 900)
    """
   
    while True:
        old_Automatic = auto.Automatic
        if auto.Automatic:
            autonomous_loop(spi_styr, spi_sensor, KP, KD)
            time.sleep(0.005)
        if(old_Automatic == True and auto.Automatic == False):
            spi.send_spi(spi_styr, 0)
        



if __name__ == "__main__":
    main()
