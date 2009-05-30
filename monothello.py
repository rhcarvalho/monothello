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

        self.board = dict()
        for row in range(8):
            frame = Frame(back)
            frame.pack(fill=BOTH, expand=1)
            for column in range(8):
                button = Button(frame,
                                state=DISABLED,
                                command=lambda row=row, column=column: self.message((row, column)))
                button["bg"] = "gray"
                button.pack(side=LEFT, fill=BOTH, expand=1)
                self.board.update( {(row, column): button} )
        give_up = Button(window, text="Pass", command=self.give_up)
        give_up.pack()
        self.status = Label(window)
        self.status["text"] = "Welcome to MonOthello!"
        self.status.pack(side=LEFT)

        window.mainloop()

    def give_up(self):
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


class Engine:
    def __init__(self, turn="B"):
        self.board = dict()
        for row in range(8):
            for column in range(8):
                self.board[(row, column)] = "E"
        self.board[(3, 3)] = self.board[(4, 4)] = "B"
        self.board[(3, 4)] = self.board[(4, 3)] = "W"
    
        self.turn = turn

    def play(self, position):
        row = position[0]
        column = position[1]
        change = list()

        valid = 0

        i = row
        count = 0
        #up vertical
        while i >= 1:
            i -= 1
            if self.board[(i, column)] == self.turn and count == 0:
                break
            elif self.board[(i, column)] == "E":
                break
            elif self.turn == self.board[(i, column)] and count != 0:
                for i in range(i+1, row+1):
                    change.append((i, column))
                valid += 1
                break
            elif self.turn != self.board[(i, column)]:
                count += 1

        i = row
        count = 0

        #down vertical
        while i <= 6:
            i += 1
            if self.board[(i, column)] == self.turn and count == 0:
                break
            elif self.board[(i, column)] == "E":
                break
            elif self.turn == self.board[(i, column)] and count != 0:
                for i in range(row, i+1):
                    change.append((i, column))
                valid += 1
                break
            elif self.turn != self.board[(i, column)]:
                count += 1

        j = column
        count = 0
        
        #left horizontal
        while j >= 1:
            j -= 1
            if self.board[(row, j)] == self.turn and count == 0:
                break
            elif self.board[(row, j)] == "E":
                break
            elif self.turn == self.board[(row, j)] and count != 0:
                for j in range(j, column+1):
                    change.append((row, j))
                valid += 1
                break
            elif self.turn != self.board[(row, j)]:
                count += 1

        j = column
        count = 0
        
        #right horizontal
        while j <= 6:
            j += 1
            if self.board[(row, j)] == self.turn and count == 0:
                break
            elif self.board[(row, j)] == "E":
                break
            elif self.turn == self.board[(row, j)] and count != 0:
                for j in range(column, j+1):
                    change.append((row, j))
                valid += 1
                break
            elif self.turn != self.board[(row, j)]:
                count += 1

        i = row
        j = column
        count = 0

        #northeast
        while j <= 6 and i >= 1:
            i -= 1
            j += 1
            if self.board[(i, j)] == self.turn and count == 0:
                break
            elif self.board[(i, j)] == "E":
                break
            elif self.turn == self.board[(i, j)] and count != 0:
                x = row
                y = column
                for times in range(count+1):
                    change.append((x, y))
                    x -= 1
                    y += 1
                valid += 1
                break
            elif self.turn != self.board[(i, j)]:
                count += 1
            
        i = row
        j = column
        count = 0

        #southwest
        while j >= 1 and i <= 6:
            i += 1
            j -= 1
            if self.board[(i, j)] == self.turn and count == 0:
                break
            elif self.board[(i, j)] == "E":
                break
            elif self.turn == self.board[(i, j)] and count != 0:
                x = row
                y = column
                for times in range(count+1):
                    change.append((x, y))
                    x += 1
                    y -= 1
                valid += 1
                break
            elif self.turn != self.board[(i, j)]:
                count += 1

        i = row
        j = column
        count = 0

        #northwest
        while j >= 1 and i >= 1:
            i -= 1
            j -= 1
            if self.board[(i, j)] == self.turn and count == 0:
                break
            elif self.board[(i, j)] == "E":
                break
            elif self.turn == self.board[(i, j)] and count != 0:
                x = row
                y = column
                for times in range(count+1):
                    change.append((x, y))
                    x -= 1
                    y -= 1
                valid += 1
                break
            elif self.turn != self.board[(i, j)]:
                count += 1

        i = row
        j = column
        count = 0

        #southeast
        while j <= 6 and i <= 6:
            i += 1
            j += 1
            if self.board[(i, j)] == self.turn and count == 0:
                break
            elif self.board[(i, j)] == "E":
                break
            elif self.turn == self.board[(i, j)] and count != 0:
                x = row
                y = column
                for times in range(count+1):
                    change.append((x, y))
                    x += 1
                    y += 1
                valid += 1
                break
            elif self.turn != self.board[(i, j)]:
                count += 1    

        if valid:
            for item in change:
                self.board[item] = self.turn

            if self.turn == "B":
                self.turn = "W"
            else:
                self.turn = "B"
            return True


if __name__ == "__main__":
    app = Application()
