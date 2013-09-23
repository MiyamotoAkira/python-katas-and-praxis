import unittest

from fizzbuzz_calculator import FizzBuzzCalculator

class TestsForFizzBuzz(unittest.TestCase):
	def test_checkNumber_NumberIs1_NumberReturnedIs1(self):
		fizzBuzzCalculator = FizzBuzzCalculator()
		result = fizzBuzzCalculator.checkNumber(1)
		self.assertEqual(result, 1)
	
	def test_checkNumber_NumberIs3_FizzIsReturned(self):
		fizzBuzzCalculator = FizzBuzzCalculator()
		result = fizzBuzzCalculator.checkNumber(3)
		self.assertEqual(result, 'Fizz')
	
	def test_checkNumber_NumberIs5_BuzzIsReturned(self):
		fizzBuzzCalculator = FizzBuzzCalculator()
		result = fizzBuzzCalculator.checkNumber(5)
		self.assertEqual(result, 'Buzz')
	
	def test_checkNumber_NumberIs15_FizzBuzzIsReturned(self):
		fizzBuzzCalculator = FizzBuzzCalculator()
		result = fizzBuzzCalculator.checkNumber(15)
		self.assertEqual(result, 'FizzBuzz')

	def test_checkNumber_NumberIs0_NumberReturnedIs0(self):
		fizzBuzzCalculator = FizzBuzzCalculator()
		result = fizzBuzzCalculator.checkNumber(0)
		self.assertEqual(result, 0)

def main():
	suite = unittest.TestLoader().loadTestsFromTestCase(TestsForFizzBuzz)
	unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
	main()
