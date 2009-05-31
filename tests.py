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


class BaseMonOthelloTest(unittest.TestCase):
    def setUp(self):
        self.game = Engine()
        cleanup_board()
        
    def cleanup_board(self):
        self.game.board[(3, 3)] = self.game.board[(4, 4)] = "E"
        self.game.board[(3, 4)] = self.game.board[(4, 3)] = "E"


class TestMove(BaseMonOthelloTest):
    def test_move_west(self):
        self.game.turn = "B"
        self.game.board[(0, 0)] = "B"
        self.game.board[(0, 1)] = "W"
        valid = self.game.move((0, 2), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(0, 1)], "B")
    
    def test_move_east(self):
        self.game.turn = "B"
        self.game.board[(0, 2)] = "B"
        self.game.board[(0, 1)] = "W"
        valid = self.game.move((0, 0), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(0, 1)], "B")        

    def test_move_north(self):
        self.game.turn = "B"
        self.game.board[(3, 2)] = "B"
        self.game.board[(4, 2)] = "W"
        valid = self.game.move((5, 2), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(4, 2)], "B")

    def test_move_south(self):
        self.game.turn = "B"
        self.game.board[(5, 2)] = "B"
        self.game.board[(4, 2)] = "W"
        valid = self.game.move((3, 2), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(3, 2)], "B")

    def test_move_northeast(self):
        self.game.turn = "B"
        self.game.board[(3, 7)] = "B"
        self.game.board[(4, 6)] = "W"
        valid = self.game.move((5, 5), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(4, 6)], "B")        

    def test_move_southwest(self):
        self.game.turn = "B"
        self.game.board[(5, 5)] = "B"
        self.game.board[(4, 6)] = "W"
        valid = self.game.move((3, 7), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(4, 6)], "B")       

    def test_move_northwest(self):
        self.game.turn = "B"
        self.game.board[(3, 5)] = "B"
        self.game.board[(4, 6)] = "W"
        valid = self.game.move((5, 7), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(4, 6)], "B")        

    def test_move_southeast(self):
        self.game.turn = "B"
        self.game.board[(5, 7)] = "B"
        self.game.board[(4, 6)] = "W"
        valid = self.game.move((3, 5), True)
        self.assertEqual(valid, True)
        self.assertEqual(self.game.board[(4, 6)], "B")        


class TestScoreCalculus(BaseMonOthelloTest):
    def test_black5_white2(self):
        self.game.board[(0, 0)] = "B"
        self.game.board[(0, 1)] = "B"
        self.game.board[(0, 5)] = "B"
        self.game.board[(0, 3)] = "B"
        self.game.board[(0, 2)] = "B"
        self.game.board[(4, 2)] = "W"
        self.game.board[(2, 1)] = "W"
        self.game.calculate_score()
        self.assertEqual(self.game.black_score, 5)
        self.assertEqual(self.game.white_score, 2)


class TestWhoIsWinning(BaseMonOthelloTest):
    def test_black_wins(self):
        self.game.board[(5, 5)] = "B"
        self.game.board[(5, 4)] = "B"
        self.game.board[(1, 3)] = "W"
        self.game.calculate_score()
        self.assertEqual(self.game.who_is_winning(), "Black")

    def test_white_wins(self):
        self.game.board[(5, 5)] = "W"
        self.game.board[(5, 4)] = "W"
        self.game.board[(1, 3)] = "W"
        self.game.calculate_score()
        self.assertEqual(self.game.who_is_winning(), "White")

    def test_none_win(self):
        self.game.board[(5, 5)] = "W"
        self.game.board[(5, 4)] = "B"
        self.game.calculate_score()
        self.assertEqual(self.game.who_is_winning(), None)


class TestEndGame(BaseMonOthelloTest):
    def test_no_move(self):
        self.game.board[(0, 1)] = "W"
        self.game.board[(3, 5)] = "B"
        self.assertEqual(self.game.check_end(), True)
  

if __name__ == "__main__":
    unittest.main()
