import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        #Initialize Bowling Game        
        self.game = BowlingGame.BowlingGame()

    def rollMany(self, pins,rolls):
        """
        Method to specify number of pins bowled and number of rolls by bowler.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.   
        """
        for i in range(rolls):
            self.game.roll(pins)

    def testGutterGame(self):
        """
        Method to test if score calculated matches expected score, for when no pins bowled at all.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.

        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.rollMany(0, 20)
        self.assertEqual (0,self.game.score())

    def testAllOnes(self):
        """
        Method to test if score calculated matches expected score, for when one pin bowled in the specified number of rolls.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.rollMany(1, 20)
        self.assertEqual(20, self.game.score())

    def testOneSpare(self):
        """
        Method to test if score calculated matches expected score, for when there is only one spare.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        self.assertEqual(16,self.game.score())

    def testOneStrike(self):
        """
        Method to test if score calculated matches expected score, for when there is only one strike.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(24, self.game.score())

    def testPerfectGame(self):
        """
        Method to test if score calculated matches expected score, for when strike is scored for all 10+2 bonus frames.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.rollMany(10,12)
        self.assertEqual(300, self.game.score())

    def testCombinationGame(self):
        """
        Method to test if score calculated matches expected score, for when there is a strike, spare, and random numbers of pin scores.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.game.roll(10)
        self.game.roll(8)
        self.game.roll(2)
        self.game.roll(3)
        self.game.roll(2)
        self.game.roll(5)
        self.game.roll(1)
        self.rollMany(0,12)
        self.assertEqual(44 , self.game.score())

    def testTwoStrikeScores(self):
        """
        Method to test if score calculated matches expected score, for when there are two strikes.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(2)
        self.rollMany(0,16)
        self.assertEqual(46, self.game.score())
    
    def testTwoSpareScores(self):
        """
        Method to test if score calculated matches expected score, for when there are two spares.

        Args:
            pins (int): number of pins bowled.
            rolls (int): number of rolls by bowler.
            
        Returns:
            Score calculated using method in Bowling Game file.      
        """
        self.game.roll(3)
        self.game.roll(5)
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(8)
        self.game.roll(2)
        self.rollMany(0,14)
        self.assertEqual(36, self.game.score())
    

   