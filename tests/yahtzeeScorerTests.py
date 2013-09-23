import unittest

from yahtzee_scorer import YahtzeeScorer, TooManyDiceException, NotEnoughDiceException, Categories

class TestsForYahtzeeScorer(unittest.TestCase):
    def test_getScore_4ItemsInArray_throwsNotEnoughDiceException(self):
    	yahtzeeScorer = YahtzeeScorer()
        self.assertRaises(NotEnoughDiceException, yahtzeeScorer.getScore, [1,1,1,1], Categories.Ones)
	
    def test_getScore_6ItemsInArray_throwsTooManyDiceException(self):
    	yahtzeeScorer = YahtzeeScorer()
        self.assertRaises(TooManyDiceException, yahtzeeScorer.getScore, [1,1,1,1,1,1], Categories.Ones)
			
    def test_getScore_11224OnFour_Givesback8(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,2,4,4], Categories.Fours)
        self.assertEqual(result,8)

    def test_getScore_11224OnPair_Givesback4(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,2,2,4], Categories.Pair)
        self.assertEqual(result,4)


    def test_getScore_11224OnChance_Givesback10(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,2,2,4], Categories.Chance)
        self.assertEqual(result,10)


    def test_getScore_11224OnYahtzee_Givesback0(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,2,2,4], Categories.Yahtzee)
        self.assertEqual(result,0)

    def test_getScore_11111OnYahtzee_Givesback5(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,1,1,1], Categories.Yahtzee)
        self.assertEqual(result,5)

    def test_getScore_11224OnHouse_Givesback0(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,2,2,4], Categories.House)
        self.assertEqual(result,0)

    def test_getScore_11221OnHouse_Givesback7(self):
        yahtzeeScorer = YahtzeeScorer()
        result = yahtzeeScorer.getScore([1,1,2,2,1], Categories.House)
        self.assertEqual(result,7)
    
    def test_diceSum_1Passed_1Returned(self):
    	yahtzeeScorer = YahtzeeScorer()
    	result = yahtzeeScorer.sumDice([1])
    	self.assertEqual(result, 1)

    def test_diceSum_123Passed_1Returned(self):
    	yahtzeeScorer = YahtzeeScorer()
    	result = yahtzeeScorer.sumDice([1,2,3])
    	self.assertEqual(result, 6)

    def test_diceSum_EmptyListPassed_0Returned(self):
    	yahtzeeScorer = YahtzeeScorer()
    	result = yahtzeeScorer.sumDice([])
    	self.assertEqual(result, 0)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestsForYahtzeeScorer)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()
	
