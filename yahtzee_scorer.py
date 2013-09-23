
import enum_ForPython2

Categories = enum_ForPython2.enum('Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Pair', 'TwoPair', 'House', 'ThreeOfAKind', 'FourOfAKind', 'SmallStraight', 'LargeStraight', 'FullHouse', 'Yahtzee', 'Chance')

class YahtzeeScorer(object):
    def getScore(self, diceRoll, category):
        if len(diceRoll) < 5:
            raise NotEnoughDiceException("There should be 6 dice given")
        elif len(diceRoll) > 5:
            raise TooManyDiceException("There should be 6 dice given")
        else:
        	diceToSum = self.chooseBasedOnCategory(diceRoll, category)
        	result = self.sumDice(diceToSum)
        return result
    
    def sumDice(self, diceToSum):
    	return sum(diceToSum)
    
    def chooseBasedOnCategory(self, diceRoll, category):
    	diceSelector = categorySelectorFactory(category)
    	return diceSelector.selectDice(diceRoll)

class BaseYahtzeeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
		return self.message


class TooManyDiceException(BaseYahtzeeException):
    pass

class NotEnoughDiceException(BaseYahtzeeException):
    pass
    
def categorySelectorFactory(category):
    if category == Categories.Ones:
        return OnesCategorySelector()
    elif category == Categories.Twos:
        return TwosCategorySelector()
    elif category == Categories.Threes:
        return ThreesCategorySelector()
    elif category == Categories.Fours:
        return FoursCategorySelector()
    elif category == Categories.Fives:
        return FivesCategorySelector()
    elif category == Categories.Sixes:
        return SixesCategorySelector()
    elif category == Categories.Pair:
        return PairCategorySelector()
    elif category == Categories.TwoPair:
        return TwoPairCategorySelector()
    elif category == Categories.House:
        return HouseCategorySelector()
    elif category == Categories.ThreeOfAKind:
        return ThreeOfAKindCategorySelector()
    elif category == Categories.FourOfAKind:
        return FourOfAKindCategorySelector()
    elif category == Categories.Yahtzee:
        return YahtzeeCategorySelector()
    elif category == Categories.Chance:
        return ChanceCategorySelector()


class NumberCategorySelector(object):
    def __init__(self, numberCategory):
        self.numberCategory = numberCategory

    def selectDice(self, dices):
        dicesSelected = [x for x in dices if x == self.numberCategory]
        return dicesSelected
		
class OnesCategorySelector(object):
    def selectDice(self, dices):
        selector = NumberCategorySelector(1)
        return selector.selectDice(dices)
		
		
class TwosCategorySelector(object):
    def selectDice(self, dices):
        selector = NumberCategorySelector(2)
        return selector.selectDice(dices)


class ThreesCategorySelector(object):
    def selectDice(self, dices):
        selector = NumberCategorySelector(3)
        return selector.selectDice(dices)


class FoursCategorySelector(object):
    def selectDice(self, dices):
        selector = NumberCategorySelector(4)
        return selector.selectDice(dices)


class FivesCategorySelector(object):
    def selectDice(self, dices):
        selector = NumberCategorySelector(5)
        return selector.selectDice(dices)


class SixesCategorySelector(object):
    def selectDice(self, dices):
        selector = NumberCategorySelector(6)
        return selector.selectDice(dices)

def sortCollectionDices(dices):
    arrangedDices = {}
    for dice in dices:
        if dice in arrangedDices:
            arrangedDices[dice] += 1
        else:
            arrangedDices[dice] = 1
        
    arrangedDices = sorted(arrangedDices.items(), key = lambda (k,v): (v,k), reverse = True)
        
    return arrangedDices

def getKind(numberOf, dices):
    sortedDices = sortCollectionDices(dices)
    kind = [(key,value) for key,value in sortedDices if value == numberOf]
    if len(kind) == 0:
        return ()
    return [kind[0][0]] * kind[0][1]


class PairCategorySelector(object):
    def selectDice(self, dices):
    	return getKind(2, dices)


class TwoPairsCategorySelector(object):
    def selectDice(self, dices):
        mergedResult = TwoKinds(dices, 2, 2)
        return mergedResult


class ThreeOfAKindCategorySelector(object):
    def selectDice(self, dices):
    	return getKind(3, dices)


class FourOfAKindCategorySelector(object):
    def selectDice(self, dices):
        return getKind(4, dices)


class YahtzeeCategorySelector(object):
    def selectDice(self, dices):
        return getKind(5, dices)


class ChanceCategorySelector(object):
    def selectDice(self, dices):
        return dices


class HouseCategorySelector(object):
    def selectDice(self, dices):
    	mergedResult = TwoKinds(dices, 3,2)
        return mergedResult

def TwoKinds(dices, firstKind, secondKind):
    firstSelection = getKind(firstKind,dices)
    if len(firstSelection) == 0:
        return ()
    		
    newList = [dice for dice in dices if dice != firstSelection[0]]
    secondSelection = getKind(secondKind, newList)
    if len(secondSelection) == 0:
        return ()
    	
    mergedResult = firstSelection + secondSelection
    return mergedResult


