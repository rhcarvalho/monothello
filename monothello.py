import sys
from Tkinter import *


def quit():
    print "Thanks for playing MonOthello !"
    sys.exit()


window = Tk()
window.title("MonOthello")

menu = Menu(window)
game_menu = Menu(menu, tearoff=0)
game_menu.add_command(label="quit", command=quit)
menu.add_cascade(label="Game", menu=game_menu)

window.config(menu=menu)

window.mainloop()

