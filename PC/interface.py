import tkinter as tk
import Bluetooth as bt


def buttonpressed(button):
    if(button=="W"):
        bt.sendbyte(1)
    elif(button=="A"):
        bt.sendbyte(2)
    elif(button=="S"):
        bt.sendbyte(3)
    elif(button=="D"):
        bt.sendbyte(4)
    elif(button=="Q"):
        bt.sendbyte(0x14)
    elif(button=="E"):
        bt.sendbyte(0x15)
    elif(button=="Y"):
        if(int(servo.cget("text")[6]) < 5):
            new_number = int(servo.cget("text")[6]) + 1
            servo.config(text="Servo " + str(new_number))
            servo.update()
            bt.sendbyte(0x20)
    elif(button=="H"):
        if(int(servo.cget("text")[6]) > 1):
            new_number = int(servo.cget("text")[6]) - 1
            servo.config(text="Servo " + str(new_number))
            servo.update()
            bt.sendbyte(0x21)
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


# Lager-rutan
lager_width = winwidth * 0.44
lager_height = winheight * 0.75
lager_x = winwidth * 0.04
lager_y = (winheight - lager_height) / 2

Lager = tk.Frame(master=window, width=lager_width, height=lager_height, bd=1, relief="solid", padx=4, pady=4)
Lager.place(x=lager_x, y= lager_y)

###############################################################
###############################################################

# Data-rutan
data_width = winwidth*0.44
data_height = winheight*0.2
data_x = winwidth*0.51
data_y = (winheight - lager_height)/2

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

text4 = tk.Label(Data, text="Avstånd till hinder: ", font=("Arial", 15))
text4.grid(column= 1, row = 0, sticky="nsw")

text5 = tk.Label(Data, text="Rotation platta: ", font=("Arial", 15))
text5.grid(column= 1, row = 1, sticky="nsw")


###############################################################
###############################################################


# Kontrollruta-rutan
kontroll_width = winwidth * 0.44
kontroll_height = winheight * 0.53
kontroll_x = winwidth * 0.51
kontroll_y = (lager_height + lager_y - kontroll_height)

Kontrollruta = tk.Frame(master=window, width=kontroll_width, height=kontroll_height, bd=1, relief="solid", padx=4, pady=4)
Kontrollruta.grid_propagate(False)

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



# INNEHÅLL RUTA1

buttonq = tk.Button(ruta1, text="Q", width =8, height=4, command=lambda: buttonpressed("Q"))
buttonq.grid(row = 1, column=0, padx=5, pady= 5)

buttone = tk.Button(ruta1, text="E", width =8, height=4, command=lambda: buttonpressed("E"))
buttone.grid(row = 1, column=2, padx=5, pady= 5)

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

button_minus = tk.Button(ruta3, text="-", font=("Arial", 20), width =3, height=1, command=lambda: buttonpressed("-"))
button_minus.grid(row = 1, column=0, padx=5, pady= 5)

servo = tk.Label(ruta3, text="Servo 1", font=("Arial", 15))
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
    
    window.destroy()
    return


#knapp_frame = tk.Frame(master=Kontrollruta, bd=1, relief="solid", padx=4, pady=4)
#knapp_frame.pack(padx=20, pady=20)

#forwardbutton = tk.Button(window, text="W", width=50, height=50)
#forwardbutton.place(x=200, y= 200)

window.protocol("WM_DELETE_WINDOW", windowclosed)
window.mainloop()
