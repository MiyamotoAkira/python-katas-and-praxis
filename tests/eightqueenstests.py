import unittest
from collections import deque
from eightqueens import Square
from eightqueens import QueenSolver

class TestsFor8Queens(unittest.TestCase):
	def test_equalitySquares_SquaresHaveTheSameContent_TheyAreEqual(self):
		square = Square(ord('A'),1)
		square2 = Square(ord('A'),1)
		self.assertTrue(square == square2)
		self.assertTrue(hash(square)==hash(square2))

	def test_equalitySquares_SquaresAreTheSameObject_TheyAreEqual(self):
		square = Square(ord('A'),1)
		self.assertTrue(square == square)
		self.assertTrue(hash(square)==hash(square))

	def test_equalitySquares_SquaresHaveDifferentContent_TheyAreDifferent(self):
		square = Square(ord('A'),1)
		square2 = Square(ord('A'),2)
		self.assertFalse(square == square2)
		self.assertFalse(hash(square)==hash(square2))
	
	def test_squareInSet_SameSquareObjectIsInSet_ReturnsTrue(self):
		setToCheck = set()
		square = Square(ord('A'),1)
		setToCheck.add(square)
		self.assertTrue(square in setToCheck)

	def test_squareInSet_SquareWithSameContentIsInSet_ReturnsTrue(self):
		setToCheck = set()
		square = Square(ord('A'),1)
		square2 = Square(ord('A'),1)
		setToCheck.add(square)
		self.assertTrue(square2 in setToCheck)

	def test_squareInSet_DifferentSquares_ReturnsFalse(self):
		setToCheck = set()
		square = Square(ord('A'),1)
		square2 = Square(ord('A'),2)
		setToCheck.add(square)
		self.assertFalse(square2 in setToCheck)
		
	def test_checkUnavailableSquare_NoUnavailableSquares_returnsFalse(self):
		queenSolver = QueenSolver()
		square = Square(ord('A'),1)
		isUnavailable = queenSolver.checkUnavailableSquare(square)
		self.assertFalse(isUnavailable)

	def test_checkUnavailableSquare_SameUnavailableSquaresAsPassed_returnsTrue(self):
		queenSolver = QueenSolver()
		square = Square(ord('A'),1)
		queenSolver.addUnavailableSquare(square)
		isUnavailable = queenSolver.checkUnavailableSquare(square)
		self.assertTrue(isUnavailable)

	def test_checkUnavailableSquare_UnavailableSquaresEqualToPassed_returnsTrue(self):
		queenSolver = QueenSolver()
		square = Square(ord('A'),1)
		queenSolver.addUnavailableSquare(square)
		square2 = Square(ord('A'),1)
		isUnavailable = queenSolver.checkUnavailableSquare(square2)
		self.assertTrue(isUnavailable)

	def test_checkUnavailableSquare_SeverUnavailableSquaresOneEqualToPassed_returnsTrue(self):
		queenSolver = QueenSolver()
		square = Square(ord('A'),1)
		queenSolver.addUnavailableSquare(square)
		square = Square(ord('B'),2)
		queenSolver.addUnavailableSquare(square)
		square = Square(ord('C'),3)
		queenSolver.addUnavailableSquare(square)
		square = Square(ord('C'),4)
		queenSolver.addUnavailableSquare(square)
		square = Square(ord('D'),5)
		queenSolver.addUnavailableSquare(square)
		square2 = Square(ord('C'),4)
		isUnavailable = queenSolver.checkUnavailableSquare(square2)
		self.assertTrue(isUnavailable)

	def test_findNextRank_NoRanksPreviouslyChosen_Returns1(self):
		queenSolver = QueenSolver()
		availableRanks = deque ([1,2,3,4,5,6,7,8])
		newRank = queenSolver.findNextRank(availableRanks)
		self.assertEqual(1, newRank)
		self.assertEqual(len(availableRanks), 7)

	def test_findNextRank_NoRanksAvailable_Returns1(self):
		queenSolver = QueenSolver()
		availableRanks = deque()
		newRank = queenSolver.findNextRank(availableRanks)
		self.assertEqual(None, newRank)

	def test_addSquareToResults_resultsWasEmpty_resultsHasOneComponent(self):
		queenSolver = QueenSolver()
		squareToAdd = Square(ord('A'),1)
		queenSolver.addSquareToResults(squareToAdd)
		self.assertEqual(len(queenSolver.results),1)
		self.assertEqual(queenSolver.results[0], squareToAdd)
	
	def test_removeLatestSquare_resultsWasEmpty_noErrorThrow(self):
		queenSolver = QueenSolver()
		queenSolver.removeLatestSquare()

	def test_removeLatestSquare_resultsHadOneEntry_resultsHasNoEntries(self):
		queenSolver = QueenSolver()
		queenSolver.addSquareToResults(Square(ord('A'), 1))
		self.assertEqual(len(queenSolver.results), 1)
		queenSolver.removeLatestSquare()
		self.assertEqual(len(queenSolver.results), 0)
		
	def test_putBackRank_availableRanksIsEmpty_singleElementOnAvailableRanks(self):
		queenSolver = QueenSolver()
		availableRanks = deque()
		queenSolver.putBackRank(availableRanks, 1)
		self.assertEqual(len(availableRanks),1)
		self.assertEqual(availableRanks[0],1)
		
	def test_addDiagonalsToUnavailable_A1_7Unavailable(self):
		queenSolver = QueenSolver()
		queenSolver.addDiagonalsToUnavailable(Square(ord('A'),1))
		self.assertEqual(len(queenSolver.unavailableSquare),7)
		
	def test_addDiagonalsToUnavailable_A8_7Unavailable(self):
		queenSolver = QueenSolver()
		queenSolver.addDiagonalsToUnavailable(Square(ord('A'),8))
		self.assertEqual(len(queenSolver.unavailableSquare),7)
		
	def test_addDiagonalsToUnavailable_H1_7Unavailable(self):
		queenSolver = QueenSolver()
		queenSolver.addDiagonalsToUnavailable(Square(ord('H'),1))
		self.assertEqual(len(queenSolver.unavailableSquare),7)
		
	def test_addDiagonalsToUnavailable_H8_7Unavailable(self):
		queenSolver = QueenSolver()
		queenSolver.addDiagonalsToUnavailable(Square(ord('H'),8))
		self.assertEqual(len(queenSolver.unavailableSquare),7)
		
	def test_addDiagonalsToUnavailable_C4_11Unavailable(self):
		queenSolver = QueenSolver()
		queenSolver.addDiagonalsToUnavailable(Square(ord('C'),4))
		self.assertEqual(len(queenSolver.unavailableSquare),11)
		
	def test_recalculateUnavailableSquares_noSquaresInResult_size0(self):
		queenSolver = QueenSolver()
		queenSolver.recalculateUnavailableSquares()
		self.assertEqual(len(queenSolver.unavailableSquare), 0)

	def test_recalculateUnavailableSquares_A1SquaresInResult_size7(self):
		queenSolver = QueenSolver()
		square = Square(ord('A'),1)
		queenSolver.addSquareToResults(square)
		queenSolver.recalculateUnavailableSquares()
		self.assertEqual(len(queenSolver.unavailableSquare), 7)

	def test_recalculateUnavailableSquares_A1C1noSquaresInResult_size13(self):
		queenSolver = QueenSolver()
		square = Square(ord('A'),1)
		queenSolver.addSquareToResults(square)
		square = Square(ord('C'),1)
		queenSolver.addSquareToResults(square)
		queenSolver.recalculateUnavailableSquares()
		self.assertEqual(len(queenSolver.unavailableSquare), 13)
			
	def test_getNextAvailableSquare_AllAvailableRanksNoUnavailableSquare_returnsTheFirstRank(self):
		queenSolver = QueenSolver()
		availableRanks = deque ([1,2,3,4,5,6,7,8])
		discardedRanks = list()
		possibleRank, square = queenSolver.getNextAvailableSquare(ord('A'), availableRanks , discardedRanks)
		self.assertEqual (possibleRank, 1)
		self.assertEqual (square, Square(ord('A'),1))

	def test_getNextAvailableSquare_AllAvailableRanksFirstIsUnavailableSquare_returnsTheSecondRank(self):
		queenSolver = QueenSolver()
		availableRanks = deque ([1,2,3,4,5,6,7,8])
		discardedRanks = list()
		queenSolver.addUnavailableSquare(Square(ord('A'),1))
		possibleRank, square = queenSolver.getNextAvailableSquare(ord('A'), availableRanks , discardedRanks)
		self.assertEqual(len(availableRanks), 6)
		self.assertEqual(len(discardedRanks), 1)
		self.assertEqual(discardedRanks[0], 1)
		self.assertEqual (possibleRank, 2)
		self.assertEqual (square, Square(ord('A'),2))

def main():
	suite = unittest.TestLoader().loadTestsFromTestCase(TestsFor8Queens)
	unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
	main()
