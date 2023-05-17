# Bernido, Charles David P. | BSCPE 1-5 
# Assignment 6 in OOP

# import class tv and other modules to be used
from tv_class import TV
from tkinter import *

def tv_1():
    tv_1 = TV()
    # TV 1 method
    tv_1.turn_on_TV()
    tv_1.set_channel(7)
    tv_1.set_volume_level(7)
    output = "TV 1's channel is " + str(tv_1.get_channel()) + " and volume level is " + str(tv_1.get_volume_level())
    label1.config(text = output)
    
def tv_2():
    tv_2 = TV()
    # TV 2 methods
    tv_2.turn_on_TV()
    tv_2.set_channel(7)
    tv_2.set_volume_level()
    output = "TV 2's channel is " + str(tv_2.get_channel()) + " and volume level is " + str(tv_2.get_volume_level())
    label2.config(text = output)

gui = Tk()  # Create an instance of tkinter frame or window
gui.title("Test TV")  # Title of the Window
gui.geometry("500x200")  # set window size
gui.config(bg = "#D8F9FF")  # background color

label1 = Label(gui, text = "", font=("Segoe",16,"bold"), bg = "#D8F9FF", fg = "#0B0B45", justify = CENTER)
label1.grid(padx= 35, pady= 40)

label2 = Label(gui, text = "", font=("Segoe",16,"bold"), bg = "#D8F9FF", fg = "#0B0B45", justify = CENTER)
label2.grid(padx= 35)

# call functions tv 1 and tv 2
tv_1()
tv_2()
gui.mainloop()

# FINAL
