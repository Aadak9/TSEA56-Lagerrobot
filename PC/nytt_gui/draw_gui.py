import tkinter as tk
import buttoncontrol as bc
import bluetooth as bt
from buttoncontrol import current_joint
import time
global buttonManuell, Manuellknapp, Autoknapp, buttonAuto, Kontrollruta, Lager, Canvas, ruta1, ruta3, buttonStartdata, buttonStart, Lagerknapp, textH, textW
Canvas = None
global lagerbredd, lagerhöjd
lagerbredd, lagerhöjd = 3, 3
global timestart
timestart = time.time()
global timeractive
timeractive = False
global window
window = tk.Tk()


def draw_gui(window):

    global buttonManuell, Manuellknapp, Autoknapp, buttonAuto, Kontrollruta, Lager, ruta1, ruta3, buttonStartdata, buttonStart, Lagerknapp, textH, textW

    window.title("Robot") 
    window.configure(background="grey")
    window.geometry("1400x950")
    print(window.winfo_width())
    window.resizable(False, False)
    window.update()

    winwidth = window.winfo_width()
    winheight = window.winfo_height()



    ###############################################################
    ###############################################################

    # Lagerknapp-rutan
    lagerknapp_width = winwidth * 0.45
    lagerknapp_height = winheight*0.15
    lagerknapp_x = winwidth*0.04
    lagerknapp_y = (winheight - winheight*0.75)/2

    global Lagerknapp
    Lagerknapp = tk.Frame(master=window, width=lagerknapp_width, height=lagerknapp_height, bd=1, relief="solid", padx=4, pady=4, highlightthickness=6)
    Lagerknapp.place(x=lagerknapp_x, y=lagerknapp_y)
    Lagerknapp.grid_propagate(False)

    Lagerknapp.grid_rowconfigure(0, weight=1)
    Lagerknapp.grid_rowconfigure(1, weight=1)
    Lagerknapp.grid_rowconfigure(2, weight=1)
    Lagerknapp.grid_columnconfigure(0, weight=30)
    Lagerknapp.grid_columnconfigure(1, weight=1)
    Lagerknapp.grid_columnconfigure(2, weight=30)


    Lagerknapp.config(bg="#d3d3d3")



    ###############################################################
    ###############################################################

    # Lager-rutan
    lager_width = winwidth * 0.44
    lager_height = winheight * 0.56
    lager_x = winwidth * 0.04
    lager_y = (winheight + lagerknapp_height - lager_height) / 2

    global Lager
    Lager = tk.Frame(master=window, width=lager_width, height=lager_height, bd=1, relief="solid", padx=4, pady=4, highlightthickness=6)
    Lager.place(x=lager_x, y= lager_y)

    Lager.config(bg="#d3d3d3")


    ###############################################################
    ###############################################################

    #autonoma start-knappen

    autoknapp_width = lagerknapp_width/2
    autoknapp_height = winheight*0.075
    autoknapp_x = winwidth*0.04
    autoknapp_y = winheight*0.04

    Autoknapp = tk.Frame(master=window, width=autoknapp_width, height=autoknapp_height, bd=0, relief="solid", padx=4, pady=4)
    Autoknapp.place(x=autoknapp_x, y=autoknapp_y)
    Autoknapp.pack_propagate(False)

    buttonAuto = tk.Button(Autoknapp, text="Autonomt", bg="grey", fg="white", font=("Arial", 16), command=bc.auto_pressed)
    buttonAuto.pack(fill="both", expand=True, padx=1, pady=1)

    ###############################################################
    ###############################################################

    #start-knappen

    startknapp_width = autoknapp_width/2
    startknapp_height = autoknapp_height
    startknapp_x = winwidth*0.835
    startknapp_y = winheight*0.04

    Startknapp = tk.Frame(master=window, width=startknapp_width, height=startknapp_height, bd=0, relief="solid",bg=window.cget("bg"), padx=4, pady=4)
    Startknapp.place(x=startknapp_x, y=startknapp_y)
    Startknapp.pack_propagate(False)

    buttonStart = tk.Button(Startknapp, text="Start", bg="grey", fg="white", font=("Arial", 16), command=bc.start_pressed)
    buttonStart.pack(fill="both", expand=True, padx=1, pady=1)

    buttonStart.pack_forget()

    ###############################################################
    ###############################################################

    #manuell-knappen

    manuellknapp_width = lagerknapp_width/2
    manuellknapp_height = winheight*0.075
    manuellknapp_x = lagerknapp_width/2 + autoknapp_x
    manuellknapp_y = winheight*0.04


    Manuellknapp = tk.Frame(master=window, width=manuellknapp_width, height=manuellknapp_height, bd=0, relief="solid", padx=4, pady=4)
    Manuellknapp.place(x=manuellknapp_x, y=manuellknapp_y)
    Manuellknapp.pack_propagate(False)

    
    buttonManuell = tk.Button(Manuellknapp, text="Manuellt", bg="green", fg="white", font=("Arial", 16), command=bc.manuell_pressed)
    buttonManuell.pack(fill="both", expand=True, padx=1, pady=1)

    ###############################################################
    ###############################################################

    #startdata-knappen

    startdataknapp_width = autoknapp_width/2
    startdataknapp_height = autoknapp_height
    startdataknapp_x = winwidth*0.51
    startdataknapp_y = winheight*0.04

    Startdataknapp = tk.Frame(master=window, width=startdataknapp_width, height=startdataknapp_height, bd=0, relief="solid",bg=window.cget("bg"), padx=4, pady=4)
    Startdataknapp.place(x=startdataknapp_x, y=startdataknapp_y)
    Startdataknapp.pack_propagate(False)

    buttonStartdata = tk.Button(Startdataknapp, text="Starta data", bg="green", fg="white", font=("Arial", 16), command=bc.startdata_pressed)
    buttonStartdata.pack(fill="both", expand=True, padx=1, pady=1)


    ###############################################################
    ###############################################################

    #kalibrerings-knappen

    kalibreringknapp_width = autoknapp_width
    kalibreringknapp_height = autoknapp_height
    kalibreringknapp_x = winwidth*0.62
    kalibreringknapp_y = winheight*0.04

    Kalibreringknapp = tk.Frame(master=window, width=kalibreringknapp_width, height=kalibreringknapp_height, bd=0, relief="solid",bg=window.cget("bg"), padx=4, pady=4)
    Kalibreringknapp.place(x=kalibreringknapp_x, y=kalibreringknapp_y)
    Kalibreringknapp.pack_propagate(False)

    buttonKalibrering = tk.Button(Kalibreringknapp, text="Kalibrera linjesensor", bg="green", fg="white", font=("Arial", 16), command=bc.calibrate_sensor)
    buttonKalibrering.pack(fill="both", expand=True, padx=1, pady=1)

    ###############################################################
    ###############################################################

    # Data-rutan
    data_width = winwidth*0.44
    data_height = winheight*0.2
    data_x = winwidth*0.51
    data_y = (winheight - winheight*0.75)/2

    Data = tk.Frame(master=window, width=data_width, height=data_height, bd=1, relief="solid", padx=4, pady=4)
    Data.grid_propagate(False)
    Data.place(x=data_x, y=data_y)

    Data.grid_rowconfigure(0, weight=1)
    Data.grid_rowconfigure(1, weight=1)
    Data.grid_rowconfigure(2, weight=1)
    Data.grid_columnconfigure(0, weight=1)
    Data.grid_columnconfigure(1, weight=1)


    global text_lateral, text_gas, text_varor, text_IR, text_rotation, text_tid


    text_lateral = tk.Label(Data, text="Lateral position: ", font=("Arial", 15))
    text_lateral.grid(column= 0, row = 0, sticky="nsw")

    text_gas = tk.Label(Data, text="Gaspådrag: ", font=("Arial", 15))
    text_gas.grid(column= 0, row = 1, sticky="nsw")

    text_varor = tk.Label(Data, text="Upplockade varor: ", font=("Arial", 15))
    text_varor.grid(column= 0, row = 2, sticky="nsw")

    text_IR = tk.Label(Data, text=f"Avstånd till hinder: ", font=("Arial", 15))
    text_IR.grid(column= 1, row = 0, sticky="nsw")

    text_rotation = tk.Label(Data, text="Rotation platta: ", font=("Arial", 15))
    text_rotation.grid(column= 1, row = 1, sticky="nsw")

    text_tid = tk.Label(Data, text="Total körningstid: --- ", font=("Arial", 15))
    text_tid.grid(column= 1, row = 2, sticky="nsw")


    ###############################################################
    ###############################################################


    # Kontrollruta-rutan
    kontroll_width = winwidth * 0.44
    kontroll_height = winheight * 0.53
    kontroll_x = winwidth * 0.51
    kontroll_y = ((winheight - winheight*0.75) / 2 + winheight*0.75 - kontroll_height)

    Kontrollruta = tk.Frame(master=window, width=kontroll_width, height=kontroll_height, bd=1, relief="solid", highlightthickness=6, padx=4, pady=4)
    Kontrollruta.grid_propagate(False)
    Kontrollruta.config(highlightbackground="green", highlightcolor="green")

    Kontrollruta.place(x=kontroll_x, y=kontroll_y)

    Kontrollruta.grid_rowconfigure(0, weight=1)
    Kontrollruta.grid_rowconfigure(1, weight=1)
    Kontrollruta.grid_columnconfigure(0, weight=1)



    ruta1 = tk.Frame(Kontrollruta, relief="solid", bd = 2)
    ruta1.grid(row=0, column=0, sticky="nsew")
    #Gör ruta1:s grid balanserat så knapparna centreras bättre
    for i in range(3):  # 3 kolumner: A S D
        ruta1.grid_columnconfigure(i, weight=1)
    for i in range(3):  # 3 rader: Text + Q/W/E + A/S/D
        ruta1.grid_rowconfigure(i, weight=1)

    ruta1.grid_columnconfigure(0, uniform=True)
    ruta1.grid_columnconfigure(1, uniform=True)
    ruta1.grid_columnconfigure(2, uniform=True)
    ruta1.grid_rowconfigure(1, uniform=True)


    ruta3 = tk.Frame(Kontrollruta, relief="solid", bd = 2)
    ruta3.grid(row=1, column=0, sticky="nsew")
    # Gör ruta3:s grid balanserat så knapparna centreras bättre
    for i in range(3):  # 3 kolumner
        ruta3.grid_columnconfigure(i, weight=1)
    for i in range(2):  # 2 rader
        ruta3.grid_rowconfigure(i, weight=1)


    #INNEHÅLL LAGERKNAPPRUTA

    textC = tk.Label(Lagerknapp, text="Columner: ", font=("Arial", 15))
    textC.grid(column= 0, row = 0, sticky="nsw")

    textR = tk.Label(Lagerknapp, text="Rader: ", font=("Arial", 15))
    textR.grid(column= 0, row = 1, sticky="nsw")

    buttonaddW = tk.Button(Lagerknapp, text="+", font=("Arial", 15), width =6, height=2, command=lambda: bc.increase_lager_width())
    buttonaddW.grid(row = 0, column=2, padx=5, pady= 5)

    textW = tk.Label(Lagerknapp, text=lagerbredd, font=("Arial", 15))
    textW.grid(row = 0, column=1)

    buttonsubW = tk.Button(Lagerknapp, text="-", font=("Arial", 15), width =6, height=2, command=lambda: bc.decrease_lager_width())
    buttonsubW.grid(row = 0, column=0, padx=5, pady= 5)


    buttonaddH = tk.Button(Lagerknapp, text="+",  font=("Arial", 15), width =6, height=2, command=lambda: bc.increase_lager_height())
    buttonaddH.grid(row = 1, column=2, padx=5, pady= 5)

    textH = tk.Label(Lagerknapp, text=lagerhöjd, font=("Arial", 15))
    textH.grid(row = 1, column=1)

    buttonsubH = tk.Button(Lagerknapp, text="-", font=("Arial", 15), width =6, height=2, command=lambda: bc.decrease_lager_height())
    buttonsubH.grid(row = 1, column=0, padx=5, pady= 5)

    resetbutton = tk.Button(Lagerknapp, text="Reset", width =8, height=4, command=lambda: bc.reset_lager())
    resetbutton.grid(row = 2, column=1, padx=5, pady= 5)

    for widget in Lagerknapp.winfo_children():
        try:
            widget.config(state="disabled")
        except:
            pass

    # INNEHÅLL RUTA1


    buttonw = tk.Button(ruta1, text= "W", width =8, height=4)
    buttonw.grid(row = 1, column=1, padx=5, pady= 5)
    buttonw.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("w", "press"))
    buttonw.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("w", "release"))

    buttona = tk.Button(ruta1, text= "A", width =8, height=4)
    buttona.grid(row = 2, column=0, padx=5, pady= 5)
    buttona.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("a", "press"))
    buttona.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("a", "release"))


    buttons = tk.Button(ruta1, text= "S", width =8, height=4)
    buttons.grid(row = 2, column=1, padx=5, pady= 5)
    buttons.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("s", "press"))
    buttons.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("s", "release"))

    buttond = tk.Button(ruta1, text= "D", width =8, height=4)
    buttond.grid(row = 2, column=2, padx=5, pady= 5)
    buttond.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("d", "press"))
    buttond.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("d", "release"))

    platta = tk.Label(ruta1, text="Platta", font=("Arial", 15))
    platta.grid(column= 1, row = 0)

    
    






    # INNEHÅLL RUTA3

    button_minus = tk.Button(ruta3, text="- (H)", font=("Arial", 15), width =7, height=1)
    button_minus.grid(row = 1, column=0, padx=5, pady= 5)
    button_minus.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("-", "press"))
    button_minus.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("-", "release"))
    
    global servo, current_joint
    servo = tk.Label(ruta3, text="Led " + str(current_joint), font=("Arial", 15))
    servo.grid(row=1, column=1)

    button_plus = tk.Button(ruta3, text="+ (Y)", font=("Arial", 15), width =7, height=1)
    button_plus.grid(row = 1, column=2, padx=5, pady= 5)
    button_plus.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("+", "press"))
    button_plus.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("+", "release"))

    button_counterclockwise = tk.Button(ruta3, text="CCW (Z)", font=("Arial", 9), width =15, height=3)
    button_counterclockwise.grid(row = 2, column=0, padx=5, pady= 5)
    button_counterclockwise.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("z", "press"))
    button_counterclockwise.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("z", "release"))


    button_clockwise = tk.Button(ruta3, text="CW (C)", font=("Arial", 9), width =15, height=3)
    button_clockwise.grid(row = 2, column=2, padx=5, pady= 5)
    button_clockwise.bind("<ButtonPress-1>", lambda e: bc.simulate_key_event("c", "press"))
    button_clockwise.bind("<ButtonRelease-1>", lambda e: bc.simulate_key_event("c", "release"))


    arm = tk.Label(ruta3, text="Arm", font=("Arial", 15))
    arm.grid(row=0, column=1)



    ###############################################################
    ###############################################################


    window.bind("<KeyPress>", bc.on_key_press)
    window.bind("<KeyRelease>", bc.on_key_release)




   








    ## LAGERRUTA
    Lager.update()
    global Canvas
    Canvas = tk.Canvas(Lager, height=str(Lager.winfo_height()), width=str(Lager.winfo_width()) ,bg="white")
    Canvas.pack()

    Canvas.config(bg="#d3d3d3")
    
    Canvas.tag_bind("line", "<Button-1>", on_line_click)

    for widget in Lager.winfo_children():
        try:
            widget.config(state="disabled")
        except:
            pass
    
    
    window.update()
    window.update_idletasks()



def draw_circle(canvas, x, y, r, color="blue"):
    return canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="black")


def draw_lager():
    global Canvas, Lager, lagerbredd, lagerhöjd
    Canvas.delete("all")
    nr_xnodes = lagerbredd + 1
    nr_ynodes = lagerhöjd + 1

    xposlist =[]
    nr = 1
    while nr <= nr_xnodes:
        xposlist.append(Lager.winfo_width()/(nr_xnodes + 1) * nr)
        nr += 1

    yposlist = []
    nr = 1
    while nr <= nr_ynodes:
        yposlist.append(Lager.winfo_height()/(nr_ynodes + 1) * nr)
        print(yposlist)
        nr += 1


    lines = []

    # Draw horizontal lines
    for y in yposlist:
        for i in range(len(xposlist) - 1):
            x1, x2 = xposlist[i], xposlist[i + 1]
            line = Canvas.create_line(x1, y, x2, y, fill="black", width=5, tags="line")
            lines.append((line, (x1, y, x2, y)))

    # Draw vertical lines
    for x in xposlist:
        for i in range(len(yposlist) - 1):
            y1, y2 = yposlist[i], yposlist[i + 1]
            line = Canvas.create_line(x, y1, x, y2, fill="black", width=5, tags="line")
            lines.append((line, (x, y1, x, y2)))
    
    #Draw nodes
    node_count = 1
    for xpos in xposlist:
        for ypos in yposlist:
            draw_circle(Canvas, xpos, ypos, 16, color="lightgray")
            Canvas.create_text(xpos, ypos, text=str(node_count), fill="black", font=("Arial", 14))
            node_count += 1



#Draw goalnode
def on_line_click(event):
    global Canvas
    clicked_items = Canvas.find_withtag("current")
    if not clicked_items:
        return

    item = clicked_items[0]
    coords = Canvas.coords(item)
    x1, y1, x2, y2 = coords

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    node = Canvas.create_oval(mx - 10, my - 10, mx + 10, my + 10, fill="green", outline="black")
    Canvas.tag_bind(node, "<Button-1>", remove_node)

def remove_node(event):
    Canvas.delete("current")



def update_joint(current_joint):
    servo.config(text="Led " + str(current_joint))
    servo.update()


def display_sensor_value(sensor, value):
    global text_lateral, text_gas, text_varor, text_IR, text_rotation, text_tid
    if sensor == "IR":
        text_IR.config(text="Avstånd till hinder: " + value)
    elif sensor == "Reflex":
        text_lateral.config(text="Lateral position: " + value)
    elif sensor == "Gas":
        text_gas.config(text="Gaspådrag: " + value)
    elif sensor == "Gyro":
        text_rotation.config(text="Rotation platta: " + value)
    elif sensor == "Time":
        text_tid.config(text="Total körningstid: " + value)






def data_loop(window):
    if not bc.gather_data:
        window.after(100, lambda: data_loop(window))
        return
    try:
        IR_data = bt.send_and_receive(0x60)
    except:
        print("IR misslyckat")
    display_sensor_value("IR", str(IR_data))

    try:
        Reflex_data = bt.send_and_receive(0x61)
        Reflex_data = 6 - Reflex_data/2
    except:
        print("Reflex misslyckat")
    display_sensor_value("Reflex", str(Reflex_data))

    try:
        leftgas = bt.send_and_receive(0x66)
    except:
        print("Vänster gas misslyckat")

    try:    
        rightgas = bt.send_and_receive(0x65)
    except:
        print("Höger gas misslyckat")
    gas_value = str(leftgas) + ", " + str(rightgas)
    display_sensor_value("Gas", gas_value)

    try:
        Gyro_data = bt.send_and_receive(0x62)
    except:
        print("Gyro misslyckat")
    display_sensor_value("Gyro", str(Gyro_data))
    
    print("letar data")
    
    window.after(100, lambda: data_loop(window))


def timer(window):
    if timeractive:
        timenow = time.time()
        elapsed_time = round(timenow - timestart, 0)
        display_sensor_value("Time", str(elapsed_time))

    window.after(1000, lambda: timer(window))




def windowclosed():
    try:
        bt.sendbyte(0x10)
    except:
        pass
    
    bt.s.close()
    window.destroy()
    return


