import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        self.rollMany(0, 20)
        self.assertEqual (0,self.game.score())
    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(20, self.game.score())
    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        self.assertEqual(16,self.game.score())
    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        self.assertEqual(28, self.game.score())

    def testPerfectGame(self):
        self.rollMany(10,12)
        self.assertEqual(300, self.game.score())
    def testOneSpare(self):
        self.rollMany(5,21)
        self.assertEqual(150, self.game.score())
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)