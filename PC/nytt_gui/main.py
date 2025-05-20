import tkinter as tk
import draw_gui as dg
import bluetooth as bt

def main():

    bt.bluetoothinit()
    dg.draw_gui(dg.window)
    print("drawguid")
    dg.draw_lager()
    print("lagerdrawed")
    dg.data_loop(dg.window)   
    dg.window.mainloop()



main()  