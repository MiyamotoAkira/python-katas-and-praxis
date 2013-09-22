class KataTennis(object):
    def __init__(self, player1Name, player2Name):
        self.firstPlayer = Player(player1Name)
        self.secondPlayer = Player(player2Name)
    
    
    def isGameFinished(self):
        return self.pointsOnWinningRange() and abs(self.firstPlayer.getPoints() - self.secondPlayer.getPoints()) > 1
    

    def getFirstPlayer(self):
        return self.firstPlayer
    

    def getSecondPlayer(self):
        return self.secondPlayer


    def currentResult(self):
        if self.isGameFinished():
            return self.getPlayerWinningResult("Game")
        elif self.firstPlayer.getPoints() == 0 and self.secondPlayer.getPoints() == 0:
            return "All Love"
        elif self.checkIfScoresAreEqual(self.firstPlayer.getPoints(), self.secondPlayer.getPoints()):
            return self.equalScoresResults()
        elif self.playerHasAdvantage():
            return self.getPlayerWinningResult("Advantage")
        else:
            return self.getPlayersScores()


    def getPlayersScores(self):
        player1Points = self.getFirstPlayerScore()
        player2Points = self.getSecondPlayerScore()
        return player1Points + " - " + player2Points
            
    def pointsOnWinningRange(self):
        maxPoints = max(self.firstPlayer.getPoints(), self.secondPlayer.getPoints())
        return maxPoints > 3
    	
    
    def playerHasAdvantage(self):
        return self.pointsOnWinningRange() and abs(self.firstPlayer.getPoints() - self.secondPlayer.getPoints()) == 1
    
    
    def getPlayerWinningResult(self, advantage):
        if self.firstPlayer.getPoints() > self.secondPlayer.getPoints():
            return advantage + " Player 1"  
        else:
            return advantage + " Player 2"


    def equalScoresResults(self):
        if (self.firstPlayer.getPoints() > 2):
            return "Deuce"
        else:
            playerPoints = self.getFirstPlayerScore()
            return playerPoints + " equals"

                
    def checkIfScoresAreEqual(self, firstPlayerPoints, secondPlayerPoints):
        if firstPlayerPoints == secondPlayerPoints:
            return True
        else:
            return False

    
    def getFirstPlayerScore(self):
        return self.getPlayerScore(self.firstPlayer.getPoints())


    def getSecondPlayerScore(self):
        return self.getPlayerScore(self.secondPlayer.getPoints())



    def getPlayerScore(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "15"
        elif points == 2:
            return "30"
        else:
            return "40"


    def playerScored(self, player):
        if self.firstPlayer == player:
            self.firstPlayer.scorePoint()
        else:
            self.secondPlayer.scorePoint()


class Player(object):
    def __init__(self,playerName):
        self.playerName = playerName
        self.playerPoints = 0


    def getPlayerName(self):
        return self.playerName
    
    
    def getPoints(self):
        return self.playerPoints
    
    
    def scorePoint(self):
    	   self.playerPoints += 1
