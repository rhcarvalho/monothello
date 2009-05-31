class Engine:
    def __init__(self, turn="B"):
        """Put the pieces on the board, set the turn, scores and the directions 
        to check valid positions."""

        self.board = dict()
        for row in range(8):
            for column in range(8):
                self.board[(row, column)] = "E"
        self.board[(3, 3)] = self.board[(4, 4)] = "B"
        self.board[(3, 4)] = self.board[(4, 3)] = "W"

        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1), 
                           (1, 1), (-1, -1), (1, -1), (-1, 1)]
  
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

        to_change = list()
        any_valid_position = False
        for direction in self.directions:
            i, j = position
            between = 0
                
            while True:
                if (direction[0] == 1 and i == 7) or (direction[0] == -1 and i == 0) or \
                   (direction[1] == 1 and j == 7) or (direction[1] == -1 and j == 0):
                    break
                
                i += direction[0]
                j += direction[1]

                if self.board[(i, j)] == "E":
                    break
                elif self.turn != self.board[(i, j)]:
                    between += 1    
                elif self.board[(i, j)] == self.turn:
                    if between == 0:
                        break
                    else:
                        if not play:
                            return True
                        any_valid_position = True
                        x, y = position
                        for times in range(between+1):
                            to_change.append((x, y))
                            x += direction[0]
                            y += direction[1]
                        break

        if play and any_valid_position:
            for item in to_change:
                self.board[item] = self.turn
            self.calculate_score()
            self.change_turn()
            return True
        return False

    def find_valid_positions(self):
        """Returns a list of valid positions."""

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
        self.change_turn()
        return len(this_turn) == len(next_turn) == 0

    def someone_winning(self):
        return self.black_score != self.white_score

    def who_is_winning(self):
        """Returns a string with the winning side."""
        if self.someone_winning():
            if self.black_score > self.white_score:
                return "Black"
            else:
                return "White"           
        return None

