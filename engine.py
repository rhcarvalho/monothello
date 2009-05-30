class Engine:
    def __init__(self, turn="B"):
        """Put the pieces on the board and set the turn."""

        self.board = dict()
        for row in range(8):
            for column in range(8):
                self.board[(row, column)] = "E"
        self.board[(3, 3)] = self.board[(4, 4)] = "B"
        self.board[(3, 4)] = self.board[(4, 3)] = "W"
    
        self.turn = turn

    def move(self, position):
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
            for item in change:
                self.board[item] = self.turn

            if self.turn == "B":
                self.turn = "W"
            else:
                self.turn = "B"
            return True
