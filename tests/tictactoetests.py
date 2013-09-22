import unittest
from tictactoe import Game

class TestsForLogic(unittest.TestCase):
	
	def test_addFirstPlayerMove_AddLegalMove_MoveHasBeenAddedToBoard(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		self.assertTrue(game.checkSquareIsPlayer(game.FirstPlayer,"A1"))

	def test_addSecondPlayerMove_AddLegalMove_MoveHasBeenAddedToBoard(self):
		game = Game()
		game.addSecondPlayerMove("A1")
		self.assertTrue(game.checkSquareIsPlayer(2,"A1"))

	def test_addFirstPlayerMove_IllegalMove_MoveHasBeenAddedToBoard(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		result = game.addFirstPlayerMove("A1")
		self.assertEqual(result,'Square already occupied', 'Should have said the square was occupied')

	def test_checkFinish_FirstRowIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		game.addFirstPlayerMove("A2")
		game.addFirstPlayerMove("A3")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_SecondRowIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("B1")
		game.addFirstPlayerMove("B2")
		game.addFirstPlayerMove("B3")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_ThirdRowIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("C1")
		game.addFirstPlayerMove("C2")
		game.addFirstPlayerMove("C3")
 		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_FirstRowIsAllSecondPlayer_ReturnsSecondPlayerWon(self):
		game = Game()
		game.addSecondPlayerMove("A1")
		game.addSecondPlayerMove("A2")
		game.addSecondPlayerMove("A3")
		result = game.checkFinish()
		self.assertEqual(result, game.SecondPlayerWin, 'The second player should have won')

	def test_checkFinish_FirstColumnIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		game.addFirstPlayerMove("B1")
		game.addFirstPlayerMove("C1")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_SecondColumnIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("A2")
		game.addFirstPlayerMove("B2")
		game.addFirstPlayerMove("C2")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_ThirdColumnIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("A3")
		game.addFirstPlayerMove("B3")
		game.addFirstPlayerMove("C3")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_LeftToRightDiagonalIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		game.addFirstPlayerMove("B2")
		game.addFirstPlayerMove("C3")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')

	def test_checkFinish_LeftToRightDiagonalIsAllFirstPlayer_ReturnsFirstPlayerWon(self):
		game = Game()
		game.addFirstPlayerMove("A3")
		game.addFirstPlayerMove("B2")
		game.addFirstPlayerMove("C1")
		result = game.checkFinish()
		self.assertEqual(result, game.FirstPlayerWin, 'The first player should have won')
	
	def test_validateInput_InputIsValid_returnsTrue(self):
		game = Game()
		result = game.validateInput("A1")
		self.assertTrue(result)
		
	def test_validateInput_ColumnInvalidTooLow_ReturnsFalse(self):
		game = Game()
		result = game.validateInput("A0")
		self.assertFalse(result)

	def test_validateInput_ColumnInvalidTooHigh_ReturnsFalse(self):
		game = Game()
		result = game.validateInput("A4")
		self.assertFalse(result)
		
	def test_validateInput_RowInvalidNotABC_ReturnsFalse(self):
		game = Game()
		result = game.validateInput("D1")
		self.assertFalse(result)

	def test_validateInput_InputLessThanTwoCharacters_ReturnsFalse(self):
		game = Game()
		result = game.validateInput("D")
		self.assertFalse(result)

	def test_validateInput_InputMoreThanTwoCharacters_ReturnsFalse(self):
		game = Game()
		result = game.validateInput("D43")
		self.assertFalse(result)
		
	def test_noMovesLeft_EmptyField_ReturnsFalse(self):
		game = Game()
		result = game.noMovesLeft()
		self.assertFalse(result)

	def test_noMovesLeft_OneMove_ReturnsFalse(self):
		game = Game()
		result = game.noMovesLeft()
		self.assertFalse(result)

	def test_noMovesLeft_AllButOneMove_ReturnsFalse(self):
		game = Game()
		result = game.noMovesLeft()
		self.assertFalse(result)
		
	def test_noMovesLeft_FullField_ReturnsTrue(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		game.addFirstPlayerMove("A2")
		game.addFirstPlayerMove("A3")
		game.addFirstPlayerMove("B1")
		game.addFirstPlayerMove("B2")
		game.addFirstPlayerMove("B3")
		game.addFirstPlayerMove("C1")
		game.addFirstPlayerMove("C2")
		game.addFirstPlayerMove("C3")
		result = game.noMovesLeft()
		self.assertTrue(result)
		
	def test_checkSquareIsOccupied_IsNot_ReturnsFalse(self):
		game = Game()
		result = game.checkSquareIsOccupied("A1")
		self.assertFalse(result)

	def test_checkSquareIsOccupied_ItIs_ReturnsTrue(self):
		game = Game()
		game.addFirstPlayerMove("A1")
		result = game.checkSquareIsOccupied("A1")
		self.assertTrue(result)

	def test_askPlayerMove_FirstPlayerPassed_ReturnsFirstPlayer(self):
		game = Game()
		result = game.askPlayerMove(game.FirstPlayer)
		self.assertEqual(result, 'First player, make your move')

	def test_askPlayerMove_SecondPlayerPassed_ReturnsSecondPlayer(self):
		game = Game()
		result = game.askPlayerMove(game.SecondPlayer)
		self.assertEqual(result, 'Second player, make your move')
		
	def test_askPlayerMove_ANotValidPlayerIsPassed_ReturnsError(self):
		self.assertTrue(False)
		
	def test_nextPlayer_CurrentOneIsFirst_ReturnsSecond(self):
		game = Game()
		game.setInitialPlayer(game.FirstPlayer)
		game.nextPlayer()
		self.assertEqual(game.currentPlayer, game.SecondPlayer)

	def test_nextPlayer_CurrentOneIsSecond_ReturnsFirst(self):
		game = Game()
		game.setInitialPlayer(game.SecondPlayer)
		game.nextPlayer()
		self.assertEqual(game.currentPlayer, game.FirstPlayer)
		
	def test_checkProblemsInput_ValidateTrueOccupiedFalse_returnsFalse(self):
		game = Game()
		result = game.checkProblemsInput(True, False)
		self.assertFalse(result)

	def test_checkProblemsInput_ValidateTrueOccupiedTrue_returnsTrue(self):
		game = Game()
		result = game.checkProblemsInput(True, True)
		self.assertTrue(result)

	def test_checkProblemsInput_ValidateFalseOccupiedFalse_returnsTrue(self):
		game = Game()
		result = game.checkProblemsInput(False, False)
		self.assertTrue(result)

	def test_checkProblemsInput_ValidateFalseOccupiedTrue_returnsTrue(self):
		game = Game()
		result = game.checkProblemsInput(False, False)
		self.assertTrue(result)

	def test_checkNotEndGame_NoMovesLeftWin_returnsFalse(self):
		game = Game()
		result = game.checkNotEndGame(True, game.FirstPlayerWin)
		self.assertFalse(result)

	def test_checkNotEndGame_NoMovesLeftNoWin_returnsFalse(self):
		game = Game()
		result = game.checkNotEndGame(True, game.NoWin)
		self.assertFalse(result)

	def test_checkNotEndGame_MovesLeftWin_returnsFalse(self):
		game = Game()
		result = game.checkNotEndGame(False, game.FirstPlayerWin)
		self.assertFalse(result)

	def test_checkNotEndGame_MovesLeftNoWin_returnsTrue(self):
		game = Game()
		result = game.checkNotEndGame(False, game.NoWin)
		self.assertTrue(result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestsForLogic)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
    
