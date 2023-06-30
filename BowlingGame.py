class BowlingGame:
    def __init__(self):
        """Initialize list"""
        self.rolls=[]

    def roll(self,pins):
        """Appends results to list"""
        self.rolls.append(pins)

    def score(self):
        """
        Score calculation based on the number of pins bowled.

        Args:
            rollIndex (int): number of the frame being bowled.

        Returns:
            Result of total calculation of pins bowled depending on strike, spare or random.      
        """
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        """
        Statement if results is a strike, ten pins within one frame, one bowl.

        Args:
            rollIndex (int): number of the frame being bowled.

        Returns:
            Result of strike which is 10 points      
        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """
        Statement if results is a spare, ten pins within one frame, two bowls.

        Args:
            rollIndex (int): number of the frame being bowled.

        Returns:
            Result of spare which is 10 points      
        """
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def strikeScore(self,rollIndex):
        """
        Provides formula if results is a strike.

        Args:
            rollIndex (int): number of the frame being bowled.

        Returns:
            Result of strike 10 points added with the points from the next two frames.      
        """
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """
        Provides formula if results is a spare.

        Args:
            rollIndex (int): number of the frame being bowled.

        Returns:
            Result of spare 10 points added with the points from the next frame.      
        """
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """
        Provides formula if results is a random ie not strike or spare.

        Args:
            rollIndex (int): number of the frame being bowled.

        Returns:
            Result of points on current frame and next frame.      
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]