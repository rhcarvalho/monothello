from Tkinter import Tk, Menu, Label, Frame, Button
from Tkinter import BOTH, LEFT, RIGHT, NORMAL, DISABLED
import tkMessageBox
from engine import Engine, EmptyPiece, Player1Piece, Player2Piece

#TODO centralize 'messages' somewhere - there's duplication in code

class Application:

    """GUI of the game."""

    def __init__(self):
        """Initialize the window and the GUI elements."""

        self.game = False
        self.show_valid_positions = False

        self.window = Tk()
        self.window.title("MonOthello")
        self.window.wm_maxsize(width="400", height="400")
        self.window.wm_minsize(width="400", height="400")

        self.create_elements()

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
        settings.add_checkbutton(label="Show valid positions",
                                 variable=self.show_valid_positions,
                                 command=self.toggle_show_valid_positions,
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
                self.board.update({(row, column): button})

    def create_options(self):
        pass_turn = Button(self.window, text="Pass", command=self.pass_turn)
        pass_turn.pack(side=RIGHT)
        self.status = Label(self.window)
        self.update_status("Welcome to MonOthello!")
        self.status.pack(side=LEFT)

    def create_game(self):
        message="Are you sure you want to restart?"
        if self.game and \
           not tkMessageBox.askyesno(title="New", message=message):
                return

        self.game = Engine()
        self.update_board()
        message = "Let's play! Now it's the %s's turn." % (self.game.turn.name,)
        self.update_status(message)

    def toggle_show_valid_positions(self):
        self.show_valid_positions = not self.show_valid_positions
        if self.game:
            self.update_board()

    def pass_turn(self):
        if not self.game:
            return
        self.game.change_turn()
        self.update_board()
        message = "%s's turn." % (self.game.turn.name,)
        self.update_status(message)

    def show_credits(self):
        message = "MonOthello\nv.: 1.0"
        tkMessageBox.showinfo(title="About", message=message)

    def bye(self):
        if tkMessageBox.askyesno(title="Quit", message="Really quit?"):
            quit()

    def play(self, position):
        """Move a piece to the given position."""

        if not self.game:
            return
        if not self.game.move(position, True):
            message = "Wrong move. %s's turn." % (self.game.turn.name,)
            self.update_status(message)
        else:
            self.update_board()
            if self.game.check_end():
                message = "End of game. "
                if self.game.someone_winning():
                    message += self.game.who_is_winning() + " won!"
                else:
                    message += "Tie."
                tkMessageBox.showinfo(title="End of game", message=message)
                self.game = False
            else:
                message = "%s's turn." % (self.game.turn.name,)
                self.update_status(message)

    def update_board(self):
        for row in range(8):
            for column in range(8):
                position = self.board[(row, column)]
                current_cell = self.game.board[(row, column)]

                position["bg"] = current_cell.color
                position["state"] = DISABLED
                if isinstance(current_cell, EmptyPiece):
                    position["state"] = NORMAL

        if self.show_valid_positions:
            valid_positions = self.game.find_valid_positions()
            for position in valid_positions:
                self.board[position]["bg"] = "green"
        self.update_score()

    def update_score(self):
        self.score["text"] = "Black: %s | White: %s" % \
                             (self.game.black_score,
                              self.game.white_score)

    def update_status(self, message):
        self.status["text"] = message


if __name__ == "__main__":
    app = Application()
