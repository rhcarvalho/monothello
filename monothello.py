from Tkinter import *
import tkMessageBox
from engine import Engine


class Application:
    """Handles the GUI stuffs. It communicates with the Engine of the game."""

    def __init__(self):       
        self.window = Tk()
        self.window.title("MonOthello")
        self.window.wm_maxsize(width="400", height="400")
        self.window.wm_minsize(width="400", height="400")

        self.create_elements()
        self.game = False

        self.window.mainloop()

    def create_elements(self):
        self.create_menu()
        self.create_board()
        self.create_options()

    def create_menu(self):
        menu = Menu(self.window)

        game = Menu(menu, tearoff=0)
        game.add_command(label="New", command=self.create_game, underline=0)
        game.add_command(label="Quit", command=self.bye, underline=0)
        menu.add_cascade(label="Game", menu=game, underline=0)

        settings = Menu(menu, tearoff=0)
        self.playable_positions = False
        settings.add_checkbutton(label="Show playable positions", 
                                 variable=self.playable_positions, 
                                 command=self.toggle_playable_positions,
                                 underline=0)
        menu.add_cascade(label="Settings", menu=settings, underline=0)


        help = Menu(menu, tearoff=0)
        help.add_command(label="About", command=self.show_credits, underline=0)
        menu.add_cascade(label="Help", menu=help, underline=0)
        
        self.window.config(menu=menu)

    def create_board(self):
        self.score = Label(self.window)
        self.score.pack()
        self.board = dict()
        back = Frame(self.window)
        back.pack(fill=BOTH, expand=1)

        for row in range(8):
            frame = Frame(back)
            frame.pack(fill=BOTH, expand=1)
            for column in range(8):
                button = Button(frame,
                                state=DISABLED,
                                command=lambda position=(row, column): self.play(position))
                button["bg"] = "gray"
                button.pack(side=LEFT, fill=BOTH, expand=1)
                self.board.update( {(row, column): button} )

    def create_options(self):
        pass_turn = Button(self.window, text="Pass", command=self.pass_turn)
        pass_turn.pack()
        self.status = Label(self.window)
        self.status["text"] = "Welcome to MonOthello!"
        self.status.pack(side=LEFT)

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

    def toggle_playable_positions(self):
        self.playable_positions = not self.playable_positions            
        if self.game:
            self.update_board()

    def pass_turn(self):
        if not self.game:
            return
        self.game.change_turn()
        self.update_board()
        self.status["text"] = "%s's turn." % self.game.turn

    def play(self, position):
        if not self.game:
            return
        if not self.game.move(position, True):
            self.status["text"] = "Wrong move. %s's turn" % self.game.turn
        else:
            self.update_board()
            if self.game.check_end():
                message = "End of game. "
                if self.game.someone_winning():
                    message += self.game.who_is_winning() + " win!" 
                else:
                    message += "Tie."
                tkMessageBox.showinfo(title="End of game", message=message)
                self.game = False
            else:
                self.status["text"] = "%s's turn" % self.game.turn      

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

        if self.playable_positions:
            valid = self.game.find_valid_positions()
            for position in valid:
                button = self.board[position]
                button["bg"] = "green"

        self.score["text"] = "Black: %s | White: %s" % (self.game.black_score, self.game.white_score)

    def show_credits(self):
        message = "MonOthello\nv.: 1.0"
        tkMessageBox.showinfo(title="About", message=message)

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()


if __name__ == "__main__":
    app = Application()
