import tkinter as tk
import draw_gui as dg
import bluetooth as bt

def main():

    bt.bluetoothinit()

    
    window = tk.Tk()
    dg.draw_gui(window)
    print("drawguid")
    dg.draw_lager()
    print("lagerdrawed")
    window.mainloop()


main()