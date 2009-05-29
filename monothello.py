import sys
from Tkinter import *
import tkMessageBox


class Application:
    def __init__(self):
        
        self.game = False
        window = Tk()
        window.title("MonOthello")
        window.wm_maxsize(width="400", height="400")
        window.wm_minsize(width="400", height="400")

        menu = Menu(window)

        game_menu = Menu(menu, tearoff=0)
        settings_menu = Menu(menu, tearoff=0)
        help_menu = Menu(menu, tearoff=0)

        menu.add_cascade(label="Game", menu=game_menu)
        menu.add_cascade(label="Settings", menu=settings_menu)
        menu.add_cascade(label="Help", menu=help_menu)

        game_menu.add_command(label="New", command=self.create_game)
        game_menu.add_command(label="Quit", command=self.bye)
        help_menu.add_command(label="About", command=self.show_credits)

        window.config(menu=menu)

        back = Frame(window)
        back.pack(fill=BOTH, expand=1)

        for row in range(8):
            frame = Frame(back)
            frame.pack(fill=BOTH, expand=1)
            for column in range(8):
                button = Button(frame)
                button["bg"] = "brown"
                button.pack(side=LEFT, fill=BOTH, expand=1)
        self.status = Label(window)
        self.status["text"] = "Welcome to MonOthello!"
        self.status.pack(side=LEFT)
        
        window.mainloop()

    def create_game(self):
        if self.game:
            if not tkMessageBox.askyesno(title="New", message="Are you sure you want to restart?"):
                return 
        self.game = Game()
        self.status["text"] = "Game created."

    def show_credits(self):
        message = "MonOthello\nv.: 1.0" 
        tkMessageBox.showinfo(title="About", message=message)

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()


class Game:
    def __init__(self):
        pass


if __name__ == "__main__":
    app = Application()
