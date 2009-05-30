from Tkinter import *
import tkMessageBox
from engine import Engine


class Application:
    """Handles the GUI stuffs of the game. It communicates with the Engine of 
    the game."""

    def __init__(self):
        
        self.game = False
        window = Tk()
        window.title("MonOthello")
        window.wm_maxsize(width="400", height="400")
        window.wm_minsize(width="400", height="400")

        self.create_elements(window)        

        window.mainloop()

    def create_elements(self, window):
        create_menu(window)
        self.board = dict()        
        self.create_board(window, self.board)
        pass_turn = Button(window, text="Pass", command=self.pass_turn)
        pass_turn.pack()
        self.status = Label(window)
        self.status["text"] = "Welcome to MonOthello!"
        self.status.pack(side=LEFT)

    def create_menu(self, window):
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

    def create_board(self, window, board):
        back = Frame(window)
        back.pack(fill=BOTH, expand=1)

        for row in range(8):
            frame = Frame(back)
            frame.pack(fill=BOTH, expand=1)
            for column in range(8):
                button = Button(frame,
                                state=DISABLED,
                                command=lambda row=row, column=column: self.message((row, column)))
                button["bg"] = "gray"
                button.pack(side=LEFT, fill=BOTH, expand=1)
                board.update( {(row, column): button} )

    def pass_turn(self):
        if self.game.turn == "B":
            self.game.turn = "W"
            self.status["text"] = "W's turn."
        else:
            self.game.turn = "B"
            self.status["text"] = "B's turn."

    def message(self, position):
        if not self.game.play(position):
            self.status["text"] = "Wrong move. %s's turn" % self.game.turn
        else:
            self.update_board()
            self.status["text"] = "%s's turn" % self.game.turn

    def create_game(self):
        if self.game:
            if not tkMessageBox.askyesno(title="New", message="Are you sure you want to restart?"):
                return
        try:
            self.game = Engine()
            self.update_board()
            self.status["text"] = "Let's play!"
        except:
            print "Error."
            quit()

    def update_board(self):
        for row in range(8):
            for column in range(8):
                position = self.board[(row, column)]
                position["state"] = NORMAL
                if self.game.board[(row, column)] == "W":
                    position["bg"] = "white"
                    position["state"] = DISABLED
                elif self.game.board[(row, column)] == "B":
                    position["bg"] = "black"
                    position["state"] = DISABLED
                else:
                    position["bg"] = "brown"

    def show_credits(self):
        message = "MonOthello\nv.: 1.0"
        tkMessageBox.showinfo(title="About", message=message)

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()


if __name__ == "__main__":
    app = Application()
