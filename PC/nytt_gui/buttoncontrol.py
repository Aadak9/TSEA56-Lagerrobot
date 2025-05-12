import bluetooth as bt
import draw_gui as dg
import time

global pressed_keys
pressed_keys = list()
global autonom_active
autonom_active = False
global current_joint
current_joint = 1
global gather_data
gather_data = False


def update_action():
    global current_joint
    global servo
    button = pressed_keys[-1]
    try:
        button2 = pressed_keys[-2]
    except:
        button2 = button
    if((button == "W" and button2 == "A") or (button == "A" and button2 == "W")):
        print("test2")
        bt.sendbyte(5)
    elif((button == "W" and button2 == "D") or (button == "D" and button2 == "W")):
        bt.sendbyte(6)
    elif(button=="W"):
        bt.sendbyte(1)
    elif(button=="A"):
        bt.sendbyte(2)
    elif(button=="S"):
        bt.sendbyte(3)
    elif(button=="D"):
        bt.sendbyte(4)
    elif(button=="Y"):
        if(current_joint < 6):
            current_joint += 1
            dg.update_joint(current_joint)
            bt.sendbyte(0x20)
            bt.sendbyte(current_joint)
    elif(button=="H"):
        if(current_joint > 1):
            current_joint -= 1
            dg.update_joint(current_joint)
            bt.sendbyte(0x20)
            bt.sendbyte(current_joint)
    elif(button=="Z"):
        bt.sendbyte(0x31)
    elif(button=="C"):
        bt.sendbyte(0x32)
    else:
        pass
    return






def on_key_press(event):
    global autonom_active, pressed_keys
    if autonom_active:
        return #ej möjliggöra knapptryck i autonomt läge
    key = event.keysym.upper()
    if key in ["W", "A", "S", "D", "Q", "E", "Y", "H", "Z", "C"] and (key not in pressed_keys):
        pressed_keys.append(key)
        update_action()
    
    
    

def on_key_release(event): #Manuell styrning höger+framåt osv löses säkert här
    global autonom_active, pressed_keys
    if autonom_active:
        return #får inte knappa om autonom
    key = event.keysym.upper()
    if key in pressed_keys:
        pressed_keys.remove(key)
        if(len(pressed_keys) > 0):
            update_action()
        else:
            all_keys_released()
    
    if not pressed_keys:
        all_keys_released()


# Simulated key event for press/release
def simulate_key_event(key, action):
    event = type('Event', (object,), {'keysym': key})
    if action == 'press':
        on_key_press(event)
    elif action == 'release':
        on_key_release(event)







def all_keys_released():
    bt.sendbyte(0)



def increase_lager_width():
    #global lagerbredd, lagerhöjd
    global Canvas
    dg.lagerbredd += 1
    dg.draw_lager()
    dg.textW.config(text=dg.lagerbredd)

def decrease_lager_width():
    #global lagerbredd, lagerhöjd
    global Canvas
    if(dg.lagerbredd > 1):
        dg.lagerbredd -= 1
    dg.draw_lager()
    dg.textW.config(text=dg.lagerbredd)

def increase_lager_height():
    #global lagerbredd, lagerhöjd
    global Canvas
    dg.lagerhöjd += 1
    dg.draw_lager()
    dg.textH.config(text=dg.lagerhöjd)

def decrease_lager_height():
    #global lagerbredd, lagerhöjd
    global Canvas
    if(dg.lagerhöjd > 1):
        dg.lagerhöjd -= 1
    dg.draw_lager()
    dg.textH.config(text=dg.lagerhöjd)

    
def reset_lager():
    global Canvas
    dg.lagerhöjd = 3
    dg.lagerbredd = 3
    dg.draw_lager()
    dg.textH.config(text=dg.lagerhöjd)
    dg.textW.config(text=dg.lagerbredd)


def auto_pressed():
    global autonom_active
    #global buttonManuell, buttonAuto, Kontrollruta, Lager, Canvas, ruta1, ruta3, buttonStartdata
    auto_active_color = dg.buttonAuto.cget("bg")
    if auto_active_color == "grey":
        autonom_active = True

        dg.buttonAuto.config(bg="green")
        dg.buttonManuell.config(bg="grey")
        dg.Lager.config(highlightbackground="green", highlightcolor ="green")
        dg.Lagerknapp.config(highlightbackground="green", highlightcolor ="green")
        dg.Kontrollruta.config(highlightbackground="grey", highlightcolor ="grey")
        dg.Lager.config(bg="SystemButtonFace")
        dg.Canvas.config(bg="SystemButtonFace")
        dg.Lagerknapp.config(bg="SystemButtonFace")

        for widget in dg.Lager.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

        for widget in dg.Lagerknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass
       
        for ruta in [dg.ruta1, dg.ruta3]:
            ruta.config(bg="#d3d3d3")
            for widget in ruta.winfo_children():
                try:
                    widget.config(state="disabled")
                except:
                    pass

        

        dg.buttonStart.pack(fill="both", expand=True, padx=1, pady=1)            
        dg.buttonStart.lift()
        dg.buttonStart.config(bg="green")
        dg.buttonStartdata.pack_forget()


    elif (auto_active_color == "green"):
        autonom_active = False
        dg.buttonAuto.config(bg="green")
        dg.buttonManuell.config(bg="grey")
    
    return

def manuell_pressed():
    global autonom_active
    autonom_active = False

    manuell_active_color = dg.buttonManuell.cget("bg")
    if manuell_active_color == "grey":
        dg.buttonAuto.config(bg="grey")
        dg.buttonManuell.config(bg="green")
        dg.Lager.config(highlightbackground="grey", highlightcolor ="grey")
        dg.Lagerknapp.config(highlightbackground="grey", highlightcolor ="grey")
        dg.Kontrollruta.config(highlightbackground="green", highlightcolor ="green")
        dg.Lager.config(bg="#d3d3d3")
        dg.Canvas.config(bg="#d3d3d3")
        dg.Lagerknapp.config(bg="#d3d3d3")

        for widget in dg.Lager.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for widget in dg.Lagerknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for ruta in [dg.ruta1, dg.ruta3]:
            ruta.config(bg="SystemButtonFace")
            for widget in ruta.winfo_children():
                try:
                    widget.config(state="normal")
                except:
                    pass

        dg.buttonStartdata.pack(fill="both", expand=True, padx=1, pady=1)
        dg.buttonStartdata.lift()          
        dg.buttonStart.pack_forget()

    elif (manuell_active_color == "green"):
        dg.buttonAuto.config(bg="grey")
        dg.buttonManuell.config(bg="green")
    return

def start_pressed():
    
    start_active_color = dg.buttonStart.cget("bg")
    try:
        bt.sendbyte(0x99) #Växla läge
    except:
        print("kunde inte växla läge")
    if start_active_color == "green":
        send_lager_info()
        dg.timestart = time.time()
        dg.timeractive = True
        dg.timer(dg.window)
        global gather_data
        gather_data = False  #ska vara true
        dg.buttonStart.config(bg="red")
        dg.buttonStart.config(text="Avbryt")

        dg.Lager.config(highlightbackground="red", highlightcolor ="red")
        dg.Lagerknapp.config(highlightbackground="red", highlightcolor ="red")

        for widget in dg.Lager.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for widget in dg.Lagerknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for widget in dg.Autoknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass
        for widget in dg.Manuellknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass


    elif start_active_color == "red":
        gather_data = False
        dg.timeractive = False
        dg.timer(dg.window)
        dg.buttonStart.config(bg="green")
        dg.buttonStart.config(text="Start")
        dg.Lager.config(highlightbackground="green", highlightcolor ="green")
        dg.Lagerknapp.config(highlightbackground="green", highlightcolor ="green")

        for widget in dg.Lager.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

        for widget in dg.Lagerknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

        for widget in dg.Autoknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass
        for widget in dg.Manuellknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

def startdata_pressed():
    global gather_data
    data_active_color = dg.buttonStartdata.cget("bg")

    if data_active_color == "green":
        gather_data = True
        dg.buttonStartdata.config(bg="red")
        dg.buttonStartdata.config(text="Avbryt data")
        

    elif data_active_color == "red":
        gather_data = False
        dg.buttonStartdata.config(bg="green")
        dg.buttonStartdata.config(text="Start data")





def calibrate_sensor():
    bt.sendbyte(0x67)


def send_lager_info():
    bt.sendbyte(0x70) #nu kommer lagerinfo
    bt.sendbyte(dg.lagerbredd)
    bt.sendbyte(dg.lagerhöjd)
    num_nodes = len(dg.placed_goods)*2
    print(dg.placed_goods)
    bt.sendbyte(num_nodes)

    for node_list in dg.placed_goods:
        bt.sendbyte(node_list[0])
        bt.sendbyte(node_list[1])

    return

