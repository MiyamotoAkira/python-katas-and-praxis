import sys

class MainMenu(object):
	def showOptions(self):
		print "Select run to do"
		print "1 - game"
		print "2 - exit"
		
		value = None
		while value is None:
			try:
				value = int(raw_input())
			except ValueError:
				print 'Please enter a number!'
			if value < 1 or value > 2:
				print 'Please enter a number between 1 and 2!'
				value = None
		return value
		
	def executeOption(self, value):
		if value == 1:
			game = Game()
			game.start()
		elif value == 2:
			sys.exit()

class Game(object):
	# game logic
	# each square/cell is represented by a pair:one letter and one number
	# letters are rows
	# numbers are columns
	
	validRows = ['A','B','C']
	validColumns = ['1','2','3']
	FirstPlayer = 1
	SecondPlayer = 2
	FirstPlayerWin = 'First Player Won'
	SecondPlayerWin = 'Second Player Won'
	NoWin = 'None won'
	
	def __init__(self):
		self.internalSquare = {}
		self.currentPlayer = self.FirstPlayer
	
	def addFirstPlayerMove(self, square):
		return self.addPlayerMove(self.FirstPlayer, square)

	def addSecondPlayerMove(self, square):
		return self.addPlayerMove(self.SecondPlayer, square)

	def addPlayerMove(self, player, square):
		if square in self.internalSquare:
			return 'Square already occupied'
		self.internalSquare[square] = player
		
	def checkSquareIsPlayer(self, player, square):
		if square in self.internalSquare:
			if self.internalSquare[square] == player:
			  return True
		return False

	def checkSquareIsOccupied(self, square):
		if square in self.internalSquare:
			return True
		return False 

	def checkRowIsPlayer(self, player, row):
		return self.checkSquareIsPlayer(player, row + "1") and self.checkSquareIsPlayer(player, row + "2") and self.checkSquareIsPlayer(player, row + "3")

	def checkColumnIsPlayer(self, player, column):
		return self.checkSquareIsPlayer(player, "A" + column) and self.checkSquareIsPlayer(player, "B" + column) and self.checkSquareIsPlayer(player, "C" + column)
		
	def checkLeftToRightDiagonalIsPlayer(self, player):
		return self.checkSquareIsPlayer(player, "A1") and self.checkSquareIsPlayer(player, "B2") and self.checkSquareIsPlayer(player, "C3")
		
	def checkRightToLeftDiagonalIsPlayer(self, player):
		return self.checkSquareIsPlayer(player, "A3") and self.checkSquareIsPlayer(player, "B2") and self.checkSquareIsPlayer(player, "C1")
	
	def playerHasWon(self, player):
		if self.checkRowIsPlayer(player, "A"):
			return True
		if self.checkRowIsPlayer(player, "B"):
			return True
		if self.checkRowIsPlayer(player, "C"):
			return True
		if self.checkColumnIsPlayer(player, "1"):
			return True
		if self.checkColumnIsPlayer(player, "2"):
			return True
		if self.checkColumnIsPlayer(player, "3"):
			return True
		if self.checkLeftToRightDiagonalIsPlayer(player):
			return True
		if self.checkRightToLeftDiagonalIsPlayer(player):
			return True

	def checkFinish(self):
		if self.playerHasWon(self.FirstPlayer):
			return self.FirstPlayerWin
		if self.playerHasWon(self.SecondPlayer):
			return self.SecondPlayerWin
		return self.NoWin
		
	def validateInput(self, input):
		if len(input) != 2:
			return False
		if not (input[0] in self.validRows):
			return False
		if not (input[1] in self.validColumns):
			return False			
		return True
	
	def noMovesLeft(self):
		for row in self.validRows:
			for column in self.validColumns:
				if not self.checkSquareIsOccupied(row+column):
					return False
		return True
		
	def askPlayerMove(self, currentPlayer):
		if currentPlayer == self.FirstPlayer:
			playerString = 'First player'
		else:
			playerString = 'Second player'
		return playerString + ', make your move'
		
	def setInitialPlayer(self, initialPlayer):
		self.currentPlayer = initialPlayer
		
	def nextPlayer(self):
		if self.currentPlayer == self.FirstPlayer:
			self.currentPlayer = self.SecondPlayer
		else:
			self.currentPlayer = self.FirstPlayer
	
	def checkInput(self, move):
		validate = self.validateInput(move)
		if validate:
			occupied = self.checkSquareIsOccupied(move)
		else:
			occupied = False
		return move, validate, occupied

	def indicateError(self, validate, occupied):
		if not validate:
			return "The move entered is not valid"
		elif occupied:
			return "The square is occupied"
		else:
			return ""
		
	def playMove(self):
		print self.askPlayerMove(self.currentPlayer)
		move, validate, occupied = self.checkInput(raw_input())		
		while self.checkProblemsInput(validate, occupied):
			print self.indicateError(validate, occupied)
			move, validate, occupied = self.checkInput(raw_input())
		self.addPlayerMove(self.currentPlayer, move)
		return self.checkFinish()
		
	def checkProblemsInput(self, validate, occupied):
		if (validate and not occupied):
			return False
		return True

	def displayFirstColumnOfRow(self, row):
		return self.displayColumnOfRow(row + "1")

	def displaySecondColumnOfRow(self, row):
		return self.displayColumnOfRow(row + "2")

	def displayThirdColumnOfRow(self, row):
		return self.displayColumnOfRow(row + "3")

	def displayColumnOfRow(self, square):
		if self.checkSquareIsPlayer(self.FirstPlayer, square):
			return "X"
		elif self.checkSquareIsPlayer(self.SecondPlayer, square):
			return "O"
		else:
			return " "

	def displayRow(self, row):
		toDisplay = "|"
		toDisplay += self.displayFirstColumnOfRow(row)
		toDisplay += "|"
		toDisplay += self.displaySecondColumnOfRow(row)
		toDisplay += "|"
		toDisplay += self.displayThirdColumnOfRow(row)
		toDisplay += "|"
		return toDisplay

	def displayUpperBoundary(self):
		self.displayBoundary()
		
	def displayFirstRow(self):
		print self.displayRow("A")
		
	def displayUpperMiddleBoundary(self):
		self.displayBoundary()	
		
	def displaySecondRow(self):
		print self.displayRow("B")
			
	def displayLowerMiddleBoundary(self):
		self.displayBoundary()
		
	def displayThirdRow(self):
		print self.displayRow("C")
		
	def displayLowerBoundary(self):
		self.displayBoundary()
		
	def displayBoundary(self):
		print "-------"
	
	def displayGame(self):
		self.displayUpperBoundary()
		self.displayFirstRow()
		self.displayUpperMiddleBoundary()
		self.displaySecondRow()
		self.displayLowerMiddleBoundary()
		self.displayThirdRow()
		self.displayLowerBoundary()
		
	def checkNotEndGame(self, noMovesLeft, result):
		if noMovesLeft or result != self.NoWin:
			return False
		return True
	
	def start(self):
		print 'The game starts' 
		result = self.playMove()
		self.displayGame()
		while self.checkNotEndGame(self.noMovesLeft(), result):
			self.nextPlayer()
			result = self.playMove()
			self.displayGame()
		print result

		
def main():
	mainMenu = MainMenu()
	value = mainMenu.showOptions()
	mainMenu.executeOption(value)

if __name__ == '__main__':
	main()
