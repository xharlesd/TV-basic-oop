# Bernido, Charles David P. | BSCPE 1-5 
# Assignment 6 in OOP

# import class tv and other modules to be used
from tv_class import TV
from tkinter import *

# def main
def main():
    # call out TV 1
    # methods for TV 1
    tv_1 = TV()
    tv_1.turn_on_TV()
    tv_1.set_channel(5)
    tv_1.set_volume_level(6)

    print("TV 1's channel is", tv_1.get_channel(), "and volume level is", tv_1.get_volume_level())

    # call out TV 2
    # methods for TV 2

window = Tk()  # Create an instance of tkinter frame or window
window.title("Test TV")  # Title of the Window
window.config(bg = "#D8F9FF")

window.mainloop()
