import unittest

from katatennis import KataTennis, Player


class KataTennisTests(unittest.TestCase):
    def test_fullGame_NoDeuce(self):
        kataTennis = KataTennis ("Player 1", "Player 2")
        player1 = kataTennis.getFirstPlayer()
        player2 = kataTennis.getSecondPlayer()
        result = kataTennis.currentResult()
        self.assertEqual (result, "All Love")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "15 - Love")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "30 - Love")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "40 - Love")
        kataTennis.playerScored(player2)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "40 - 15")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertTrue(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Game Player 1")


    def test_fullGame_WithDeuce(self):
        kataTennis = KataTennis ("Player 1", "Player 2")
        player1 = kataTennis.getFirstPlayer()
        player2 = kataTennis.getSecondPlayer()
        result = kataTennis.currentResult()
        self.assertEqual (result, "All Love")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "15 - Love")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "30 - Love")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "40 - Love")
        kataTennis.playerScored(player2)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "40 - 15")
        kataTennis.playerScored(player2)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "40 - 30")
        kataTennis.playerScored(player2)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Deuce")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Advantage Player 1")
        kataTennis.playerScored(player2)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Deuce")
        kataTennis.playerScored(player2)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Advantage Player 2")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Deuce")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertFalse(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Advantage Player 1")
        kataTennis.playerScored(player1)
        gameFinished = kataTennis.isGameFinished()
        self.assertTrue(gameFinished)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Game Player 1")


    def test_currentResult_GameJustStarted_AllLove(self):
        kataTennis = KataTennis("Player 1", "Player 2")
        result = kataTennis.currentResult()
        self.assertEqual (result, "All Love")


    def test_currentResult_FirstPlayerScored_15_0(self):
        kataTennis = KataTennis("Player 1", "Player 2")
        player1 =kataTennis.getFirstPlayer()
        kataTennis.playerScored(player1)
        result = kataTennis.currentResult()
        self.assertEqual (result, "15 - Love")


    def test_currentResult_SecondPlayerScored_0_15(self):
        kataTennis = KataTennis("Player 1", "Player 2")
        player2 =kataTennis.getSecondPlayer()
        kataTennis.playerScored(player2)
        result = kataTennis.currentResult()
        self.assertEqual (result, "Love - 15")


    def test_getPlayerName_Player1_Player1(self):
        nameToCheck = "Player1"
        player = Player(nameToCheck)
        playerName = player.getPlayerName()
        self.assertEqual(playerName, nameToCheck)


    def test_getFirstPlayer_Player1(self):
        nameToCheck = "Player1"
        kataTennis = KataTennis(nameToCheck, "Player2")
        player = kataTennis.getFirstPlayer()
        playerName = player.getPlayerName()
        self.assertEqual(playerName, nameToCheck)


    def test_getSecondPlayer_Player1(self):
        nameToCheck = "Player2"
        kataTennis = KataTennis("Player1", nameToCheck)
        player = kataTennis.getSecondPlayer()
        playerName = player.getPlayerName()
        self.assertEqual(playerName, nameToCheck)


    def test_getPlayerScore_0Points_Love(self):
        kataTennis = KataTennis("Player1", "Player2")
        value = kataTennis.getPlayerScore(0)
        self.assertEqual(value, "Love")


    def test_getPlayerScore_1Points_15(self):
        kataTennis = KataTennis("Player1", "Player2")
        value = kataTennis.getPlayerScore(1)
        self.assertEqual(value, "15")


    def test_getPlayerScore_2Points_30(self):
        kataTennis = KataTennis("Player1", "Player2")
        value = kataTennis.getPlayerScore(2)
        self.assertEqual(value, "30")


    def test_getPlayerScore_3Points_40(self):
        kataTennis = KataTennis("Player1", "Player2")
        value = kataTennis.getPlayerScore(3)
        self.assertEqual(value, "40")


    def test_getPlayerScore_4Points_40(self):
        kataTennis = KataTennis("Player1", "Player2")
        value = kataTennis.getPlayerScore(4)
        self.assertEqual(value, "40")


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(KataTennisTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()

        
