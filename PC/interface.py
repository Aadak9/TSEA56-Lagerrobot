import tkinter as tk
import Bluetooth as bt

global lagerbredd
lagerbredd = 3

global lagerhöjd
lagerhöjd = 3



def buttonpressed(button):
    global current_joint
    
    if(button=="W"):
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
            servo.config(text="Servo " + str(current_joint))
            servo.update()
            bt.sendbyte(0x20)
            bt.sendbyte(current_joint)
    elif(button=="H"):
        if(current_joint > 1):
            current_joint -= 1
            servo.config(text="Servo " + str(current_joint))
            servo.update()
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
    key = event.keysym.lower()
    if key in ["w", "a", "s", "d", "q", "e", "y", "h", "z", "c"] and (key not in pressed_keys):
        pressed_keys.add(key)
        buttonpressed(key.upper()) 

def on_key_release(event):
    key = event.keysym.lower()
    if key in pressed_keys:
        pressed_keys.remove(key)
    
    if not pressed_keys:
        all_keys_released()

def all_keys_released():
    bt.sendbyte(0)



def increase_lager_width():
    global lagerbredd
    lagerbredd += 1
    draw_lager()
    textW.config(text=lagerbredd)

def decrease_lager_width():
    global lagerbredd
    if(lagerbredd > 1):
        lagerbredd -= 1
    draw_lager()
    textW.config(text=lagerbredd)

def increase_lager_height():
    global lagerhöjd
    lagerhöjd += 1
    draw_lager()
    textH.config(text=lagerhöjd)

def decrease_lager_height():
    global lagerhöjd
    if(lagerhöjd > 1):
        lagerhöjd -= 1
    draw_lager()
    textH.config(text=lagerhöjd)

    
def reset_lager():
    global lagerhöjd
    global lagerbredd
    lagerhöjd = 3
    lagerbredd = 3
    draw_lager()
    textH.config(text=lagerhöjd)
    textW.config(text=lagerbredd)



def get_sensordata(): #hämta sensordata från IR och uppdatera i GUI

    global ir_data
    #ir_data += 1
    ir_data = bt.sendbyte()  #IR
    text4.config(text=f"Avstånd till hinder: {ir_data}")
   # bt.sendbyte(0x01)  #Reflex
    # bt.sendbyte(0x02)  #Gyro

   # window.after(100, get_sensordata)

ir_data = 0

def auto_pressed():

    auto_active_color = buttonAuto.cget("bg")
    if auto_active_color == "grey":
        buttonAuto.config(bg="green")
        buttonManuell.config(bg="grey")
        Lager.config(highlightbackground="green", highlightcolor ="green")
        Lagerknapp.config(highlightbackground="green", highlightcolor ="green")
        Kontrollruta.config(highlightbackground="grey", highlightcolor ="grey")
        Lager.config(bg="SystemButtonFace")
        Canvas.config(bg="SystemButtonFace")
        Lagerknapp.config(bg="SystemButtonFace")

        for widget in Lager.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

        for widget in Lagerknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass
       
        for ruta in [ruta1, ruta2, ruta3]:
            ruta.config(bg="#d3d3d3")
            for widget in ruta.winfo_children():
                try:
                    widget.config(state="disabled")
                except:
                    pass

        buttonStart.pack(fill="both", expand=True, padx=1, pady=1)            
        buttonStart.lift()
        buttonStart.config(bg="green")


    elif (auto_active_color == "green"):
        buttonAuto.config(bg="green")
        buttonManuell.config(bg="grey")
    
    return

def manuell_pressed():

    manuell_active_color = buttonManuell.cget("bg")
    if manuell_active_color == "grey":
        buttonAuto.config(bg="grey")
        buttonManuell.config(bg="green")
        Lager.config(highlightbackground="grey", highlightcolor ="grey")
        Lagerknapp.config(highlightbackground="grey", highlightcolor ="grey")
        Kontrollruta.config(highlightbackground="green", highlightcolor ="green")
        Lager.config(bg="#d3d3d3")
        Canvas.config(bg="#d3d3d3")
        Lagerknapp.config(bg="#d3d3d3")

        for widget in Lager.winfo_children():
            try:
                widget.config(state="disbaled")
            except:
                pass

        for widget in Lagerknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for ruta in [ruta1, ruta2, ruta3]:
            ruta.config(bg="SystemButtonFace")
            for widget in ruta.winfo_children():
                try:
                    widget.config(state="normal")
                except:
                    pass


        buttonStart.pack_forget()

    elif (manuell_active_color == "green"):
        buttonAuto.config(bg="grey")
        buttonManuell.config(bg="green")
    return

def start_pressed():
    start_active_color = buttonStart.cget("bg")

    if start_active_color == "green":
       # activate_auto = bt.sendbyte(0x40)
        buttonStart.config(bg="red")
        buttonStart.config(text="Avbryt")

        Lager.config(highlightbackground="red", highlightcolor ="red")
        Lagerknapp.config(highlightbackground="red", highlightcolor ="red")

        for widget in Lager.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for widget in Lagerknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass

        for widget in Autoknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass
        for widget in Manuellknapp.winfo_children():
            try:
                widget.config(state="disabled")
            except:
                pass


    elif start_active_color == "red":
        #cancel_auto = bt.sendbyte(0x41)
        buttonStart.config(bg="green")
        buttonStart.config(text="Start")
        Lager.config(highlightbackground="green", highlightcolor ="green")
        Lagerknapp.config(highlightbackground="green", highlightcolor ="green")

        for widget in Lager.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

        for widget in Lagerknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass

        for widget in Autoknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass
        for widget in Manuellknapp.winfo_children():
            try:
                widget.config(state="normal")
            except:
                pass


bt.bluetoothinit()

window = tk.Tk()

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

buttonAuto = tk.Button(Autoknapp, text="Autonomt", bg="grey", fg="white", font=("Arial", 16), command=auto_pressed)
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

buttonStart = tk.Button(Startknapp, text="Start", bg="grey", fg="white", font=("Arial", 16), command=start_pressed)
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

buttonManuell = tk.Button(Manuellknapp, text="Manuellt", bg="green", fg="white", font=("Arial", 16), command=manuell_pressed)
buttonManuell.pack(fill="both", expand=True, padx=1, pady=1)

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

text1 = tk.Label(Data, text="Lateral position: ", font=("Arial", 15))
text1.grid(column= 0, row = 0, sticky="nsw")

text2 = tk.Label(Data, text="Gaspådrag: ", font=("Arial", 15))
text2.grid(column= 0, row = 1, sticky="nsw")

text3 = tk.Label(Data, text="Upplockade varor: ", font=("Arial", 15))
text3.grid(column= 0, row = 2, sticky="nsw")

text4 = tk.Label(Data, text=f"Avstånd till hinder: {ir_data}", font=("Arial", 15))
text4.grid(column= 1, row = 0, sticky="nsw")

text5 = tk.Label(Data, text="Rotation platta: ", font=("Arial", 15))
text5.grid(column= 1, row = 1, sticky="nsw")

text6 = tk.Label(Data, text="Total körningstid: ", font=("Arial", 15))
text6.grid(column= 1, row = 2, sticky="nsw")


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
Kontrollruta.grid_columnconfigure(1, weight=1)



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


ruta2 = tk.Frame(Kontrollruta, relief="solid", bd = 2)
ruta2.grid(row=0, column=1, rowspan=2, sticky="nsew")


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

buttonaddW = tk.Button(Lagerknapp, text="+", width =8, height=4, command=lambda: increase_lager_width())
buttonaddW.grid(row = 0, column=2, padx=5, pady= 5)

textW = tk.Label(Lagerknapp, text=lagerbredd, font=("Arial", 15))
textW.grid(row = 0, column=1)

buttonsubW = tk.Button(Lagerknapp, text="-", width =8, height=4, command=lambda: decrease_lager_width())
buttonsubW.grid(row = 0, column=0, padx=5, pady= 5)


buttonaddH = tk.Button(Lagerknapp, text="+", width =8, height=4, command=lambda: increase_lager_height())
buttonaddH.grid(row = 1, column=2, padx=5, pady= 5)

textH = tk.Label(Lagerknapp, text=lagerhöjd, font=("Arial", 15))
textH.grid(row = 1, column=1)

buttonsubH = tk.Button(Lagerknapp, text="-", width =8, height=4, command=lambda: decrease_lager_height())
buttonsubH.grid(row = 1, column=0, padx=5, pady= 5)

resetbutton = tk.Button(Lagerknapp, text="Reset", width =8, height=4, command=lambda: reset_lager())
resetbutton.grid(row = 2, column=1, padx=5, pady= 5)

for widget in Lagerknapp.winfo_children():
    try:
        widget.config(state="disabled")
    except:
        pass

# INNEHÅLL RUTA1


buttonw = tk.Button(ruta1, text= "W", width =8, height=4, command=lambda: buttonpressed("W"))
buttonw.grid(row = 1, column=1, padx=5, pady= 5)

buttona = tk.Button(ruta1, text= "A", width =8, height=4, command=lambda: buttonpressed("A"))
buttona.grid(row = 2, column=0, padx=5, pady= 5)

buttons = tk.Button(ruta1, text= "S", width =8, height=4, command=lambda: buttonpressed("S"))
buttons.grid(row = 2, column=1, padx=5, pady= 5)

buttond = tk.Button(ruta1, text= "D", width =8, height=4, command=lambda: buttonpressed("D"))
buttond.grid(row = 2, column=2, padx=5, pady= 5)

platta = tk.Label(ruta1, text="Platta", font=("Arial", 15))
platta.grid(column= 1, row = 0)

pressed_keys = set()


# INNEHÅLL RUTA2

gripklotext = tk.Label(ruta2, text="Gripklo", font=("Arial", 15))
gripklotext.pack(pady=5)

button_open = tk.Button(ruta2, text="Öppna", width =20, height=3, command=lambda: buttonpressed("Öppna"))
button_open.pack(padx=30, pady=25)

button_close = tk.Button(ruta2, text="Stäng", width =20, height=3, command=lambda: buttonpressed("Stäng"))
button_close.pack(padx=30, pady=25)

button_turnright = tk.Button(ruta2, text="Vrid höger", width =20, height=3, command=lambda: buttonpressed("Vrid höger"))
button_turnright.pack(padx=30, pady=25)

button_turnleft = tk.Button(ruta2, text="Vrid vänster", width =20, height=3, command=lambda: buttonpressed("Vrid vänster"))
button_turnleft.pack(padx=30, pady=25)



# INNEHÅLL RUTA3

button_minus = tk.Button(ruta3, text="- \n (Y)", font=("Arial", 20), width =3, height=1, command=lambda: buttonpressed("-"))
button_minus.grid(row = 1, column=0, padx=5, pady= 5)

servo = tk.Label(ruta3, text="Servo " + str(current_joint), font=("Arial", 15))
servo.grid(row=1, column=1)

button_plus = tk.Button(ruta3, text="+", font=("Arial", 20), width =3, height=1, command=lambda: buttonpressed("+"))
button_plus.grid(row = 1, column=2, padx=5, pady= 5)

button_counterclockwise = tk.Button(ruta3, text="CCW", width =20, height=3, command=lambda: buttonpressed("CCW"))
button_counterclockwise.grid(row = 2, column=0, padx=5, pady= 5)

button_clockwise = tk.Button(ruta3, text="CW", width =20, height=3, command=lambda: buttonpressed("CW"))
button_clockwise.grid(row = 2, column=2, padx=5, pady= 5)


arm = tk.Label(ruta3, text="Arm", font=("Arial", 15))
arm.grid(row=0, column=1)



###############################################################
###############################################################


window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)


def windowclosed():
    try:
        bt.sendbyte(0x10)
    except:
        pass
    
    bt.s.close()
    window.destroy()
    return





#def draw_map():
#
#
#
 #   window.after(100, draw_map)




#knapp_frame = tk.Frame(master=Kontrollruta, bd=1, relief="solid", padx=4, pady=4)
#knapp_frame.pack(padx=20, pady=20)

#forwardbutton = tk.Button(window, text="W", width=50, height=50)
#forwardbutton.place(x=200, y= 200)


window.update()
window.update_idletasks()
#get_sensordata()








## LAGERRUTA

Lager.update()
Canvas = tk.Canvas(Lager, height=str(Lager.winfo_height()), width=str(Lager.winfo_width()) ,bg="white")
Canvas.pack()

Canvas.config(bg="#d3d3d3")

for widget in Lager.winfo_children():
    try:
        widget.config(state="disabled")
    except:
        pass


def draw_circle(canvas, x, y, r, color="blue"):
    return canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="black")


def draw_lager():
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


Canvas.tag_bind("line", "<Button-1>", on_line_click)


draw_lager()


window.protocol("WM_DELETE_WINDOW", windowclosed)
window.mainloop()