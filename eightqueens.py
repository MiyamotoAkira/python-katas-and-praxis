from collections import deque

import dequeextensions


class QueenSolver(object):

    def __init__(self):
        self.availableRanks = deque([1, 2, 3, 4, 5, 6, 7, 8])
        self.results = list()
        self.unavailableSquare = set()

    def checkUnavailableSquare(self, square):
        if square in self.unavailableSquare:
            return True
        else:
            for s in self.unavailableSquare:
                if s == square:
                    return True
        return False

    def addUnavailableSquare(self, square):
        if square not in self.unavailableSquare:
            self.unavailableSquare.add(square)

    def findNextRank(self, availableRanks):
        if len(availableRanks) > 0:
            return availableRanks.popleft()
        else:
            return None

    def useRank(self, availableRanks, rankToUse):
        availableRanks.remove(rankToUse)

    def solve(self, file, availableRanks):
        discardedRanks = list()

        while True:
            if file > ord('H'):
                return True

            possibleRank, square = self.getNextAvailableSquare(file, availableRanks, discardedRanks)

            if square is None:
                return False

            self.addSquareToResults(square)
            self.recalculateUnavailableSquares()

            newAvailableRanks = dequeextensions.combineDeques(availableRanks, deque(discardedRanks))

            if self.solve(file + 1, newAvailableRanks):
                return True
            else:
                discardedRanks.append(possibleRank)
                self.removeLatestSquare()
                self.recalculateUnavailableSquares()
                if len(availableRanks) == 0:
                    return False

    def getNextAvailableSquare(self, file, availableRanks, discardedRanks):
        possibleRank, square = self.getSquare(file, availableRanks)
        while self.checkUnavailableSquare(square):
            if len(availableRanks) == 0:
                return -1, None
            discardedRanks.append(possibleRank)
            possibleRank, square = self.getSquare(file, availableRanks)

        return (possibleRank, square)

    def getSquare(self, file, availableRanks):
        possibleRank = self.findNextRank(availableRanks)
        square = Square(file, possibleRank)
        return (possibleRank, square)

    def outputResults(self):
        print "The solution found is:"
        for square in self.results:
            print square

    def recalculateUnavailableSquares(self):
        self.unavailableSquare.clear()
        for square in self.results:
            self.addDiagonalsToUnavailable(square)

    def addDiagonalsToUnavailable(self, square):
        originalRank = square.rank
        originalFile = square.file
        self.addDiagonalToUnavailable(originalFile, originalRank, 1, 1)
        self.addDiagonalToUnavailable(originalFile, originalRank, -1, 1)
        self.addDiagonalToUnavailable(originalFile, originalRank, 1, -1)
        self.addDiagonalToUnavailable(originalFile, originalRank, -1, -1)

    def addDiagonalToUnavailable(self, file, rank, incrementFile, incrementRank):
        while self.rankAndFileInsideTable(file, rank):
            rank = rank + incrementRank
            file = file + incrementFile
            if self.rankAndFileInsideTable(file, rank):
                self.addUnavailableSquare(Square(file, rank))

    def rankAndFileInsideTable(self, file, rank):
        return rank > 0 and rank < 9 and file >= ord('A') and file <= ord('H')

    def putBackRank(self, availableRanks, rankToPutBack):
        availableRanks.appendleft(rankToPutBack)

    def showSolution(self):
        availableRanks = deque([1, 2, 3, 4, 5, 6, 7, 8])
        self.solve(ord('A'), availableRanks)
        self.outputResults()

    def addSquareToResults(self, square):
        if square is not None:
            if square.file is not None and square.rank is not None:
                self.results.append(square)

    def removeLatestSquare(self):
        if len(self.results) > 0:
            self.results.pop()


class Square(object):
    def __init__(self, file, rank):
        self.rank = rank
        self.file = file

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return hash((self.file, self.rank))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '{0}{1}'.format(chr(self.file), self.rank)


def main():
    queenSolver = QueenSolver()
    queenSolver.showSolution()

if __name__ == '__main__':
    main()
