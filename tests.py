import unittest
from engine import Engine


class TestInitialization(unittest.TestCase):
    def setUp(self):
        self.game = Engine()

    def test_pieces(self):
        self.assertEqual(self.game.board[(3, 3)], "B")
        self.assertEqual(self.game.board[(4, 4)], "B")
        self.assertEqual(self.game.board[(3, 4)], "W")
        self.assertEqual(self.game.board[(4, 3)], "W")

    def test_score(self):
        self.assertEqual(self.game.black_score, 2)
        self.assertEqual(self.game.white_score, 2)


class TestChangeTurn(unittest.TestCase):
    def test_change_turn(self):
        game = Engine()
        turn = game.turn
        game.change_turn()
        new_turn = game.turn
        self.assertEqual(turn == "W", new_turn == "B")
        self.assertEqual(turn == "B", new_turn == "W")
        

class TestMove(unittest.TestCase):
    def setUp(self):
        self.game = Engine()
        #cleaning board
        self.game.board[(3, 3)] = self.game.board[(4, 4)] = "E"
        self.game.board[(3, 4)] = self.game.board[(4, 3)] = "E"
    
    def test_move_left_horizontal(self):
        self.game.turn = "B"
        self.game.board[(0, 0)] = "B"
        self.game.board[(0, 1)] = "W"
        self.game.move((0, 2), True)
        self.assertEqual(self.game.board[(0, 1)], "B")
    
    def test_move_right_horizontal(self):
        self.game.turn = "B"
        self.game.board[(0, 2)] = "B"
        self.game.board[(0, 1)] = "W"
        self.game.move((0, 0), True)
        self.assertEqual(self.game.board[(0, 1)], "B")        

    def test_move_up_vertical(self):
        self.game.turn = "B"
        self.game.board[(3, 2)] = "B"
        self.game.board[(4, 2)] = "W"
        self.game.move((5, 2), True)
        self.assertEqual(self.game.board[(4, 2)], "B")

    def test_move_down_vertical(self):
        self.game.turn = "B"
        self.game.board[(5, 2)] = "B"
        self.game.board[(4, 2)] = "W"
        self.game.move((3, 2), True)
        self.assertEqual(self.game.board[(3, 2)], "B")

    def test_move_northeast(self):
        self.game.turn = "B"
        self.game.board[(3, 7)] = "B"
        self.game.board[(4, 6)] = "W"
        self.game.move((5, 5), True)
        self.assertEqual(self.game.board[(4, 6)], "B")        

    def test_move_southwest(self):
        self.game.turn = "B"
        self.game.board[(5, 5)] = "B"
        self.game.board[(4, 6)] = "W"
        self.game.move((3, 7), True)
        self.assertEqual(self.game.board[(4, 6)], "B")       

    def test_move_northwest(self):
        self.game.turn = "B"
        self.game.board[(3, 5)] = "B"
        self.game.board[(4, 6)] = "W"
        self.game.move((5, 7), True)
        self.assertEqual(self.game.board[(4, 6)], "B")        

    def test_move_southeast(self):
        self.game.turn = "B"
        self.game.board[(5, 7)] = "B"
        self.game.board[(4, 6)] = "W"
        self.game.move((3, 5), True)
        self.assertEqual(self.game.board[(4, 6)], "B")        


if __name__ == "__main__":
    unittest.main()
