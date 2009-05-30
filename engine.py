class Engine:
    def __init__(self, turn="B"):
        """Put the pieces on the board and set the turn."""

        self.board = dict()
        for row in range(8):
            for column in range(8):
                self.board[(row, column)] = "E"
        self.board[(3, 3)] = self.board[(4, 4)] = "B"
        self.board[(3, 4)] = self.board[(4, 3)] = "W"
    
        self.black_score = self.white_score = 2
        self.turn = turn

    def change_turn(self):
        if self.turn == "B":
            self.turn = "W"
        else:
            self.turn = "B"

    def move(self, position, play):
        """If play is True, move to that position. 
        If play is False, just check if the position is valid.
        """

        row = position[0]
        column = position[1]
        change = list()

        valid = 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), 
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for direction in directions:            
            i = row
            j = column
            count = 0
                
            while True:
                if direction[0] == 1 and i > 6:
                    break
                if direction[0] == -1 and i < 1:
                    break
                if direction[1] == 1 and j > 6:
                    break
                if direction[1] == -1 and j < 1:
                    break
                
                i += direction[0]
                j += direction[1]

                if self.board[(i, j)] == self.turn and count == 0:
                    break
                elif self.board[(i, j)] == "E":
                    break
                elif self.turn == self.board[(i, j)] and count != 0:
                    if not play:
                        return True
                    x = row
                    y = column
                    for times in range(count+1):
                        change.append((x, y))
                        x += direction[0]
                        y += direction[1]
                    valid += 1
                    break
                elif self.turn != self.board[(i, j)]:
                    count += 1    

        if valid:
            if play:
                for item in change:
                    self.board[item] = self.turn

                self.change_turn()
            return True
        else:
            return False

    def find_valid_positions(self):
        """Return a list of valid positions."""

        valid_positions = list()
        for i in range(8):
            for j in range(8):
                if self.board[(i, j)] == "E" and self.move((i, j), False):
                    valid_positions.append((i, j))
        return valid_positions

    def calculate_score(self):
        self.black_score = self.white_score = 0
        for i in range(8):
            for j in range(8):
                if self.board[(i, j)] == "W":
                    self.white_score += 1
                if self.board[(i, j)] == "B":
                    self.black_score += 1

    def check_end(self):
        this_turn = self.find_valid_positions()
        self.change_turn()
        next_turn = self.find_valid_positions()
        if len(this_turn) == len(next_turn) == 0:
            self.change_turn()
            return True
        else:
            self.change_turn()
            return False
