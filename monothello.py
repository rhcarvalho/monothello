import sys
from Tkinter import *
import tkMessageBox


class Application:
    def __init__(self):

        window = Tk()
        window.title("MonOthello")

        menu = Menu(window)
        game_menu = Menu(menu, tearoff=0)
        help_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Game", menu=game_menu)
        menu.add_cascade(label="Help", menu=help_menu)
        game_menu.add_command(label="Quit", command=self.bye)
        help_menu.add_command(label="About", command=self.show_credits)

        window.config(menu=menu)
        window.mainloop()
  
    def show_credits(self):
        message = "MonOthello\nv.: 1.0" 
        tkMessageBox.showinfo(title="About", message=message)

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()


if __name__ == "__main__":
    app = Application()
