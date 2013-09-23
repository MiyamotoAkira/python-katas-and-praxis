
class FizzBuzzCalculator(object):
    def checkNumber(self, numberToCalculate):
    
    	if numberToCalculate == 0:
    		result = numberToCalculate
        elif self.numberIsDivisibleBy3And5(numberToCalculate):
        	result = 'FizzBuzz'
        elif self.numberIsDivisibleBy3(numberToCalculate):
            result = 'Fizz'
        elif self.numberIsDivisibleBy5(numberToCalculate):
            result = 'Buzz'
        else:
             result = numberToCalculate
        return result

	
    def numberIsDivisibleByDivisor(self, numberToCalculate, divisor):
        division = numberToCalculate % divisor
        return division == 0

	
    def numberIsDivisibleBy5(self, numberToCalculate):
        return self.numberIsDivisibleByDivisor (numberToCalculate, 5)

	
    def numberIsDivisibleBy3(self, numberToCalculate):
        return self.numberIsDivisibleByDivisor (numberToCalculate, 3)
    
    
    def numberIsDivisibleBy3And5(self, numberToCalculate):
    	divisibleBy3 = self.numberIsDivisibleBy3(numberToCalculate)
    	divisibleBy5 = self.numberIsDivisibleBy5(numberToCalculate)
    	return divisibleBy3 and divisibleBy5


def main():
    fizzBuzzCalculator = FizzBuzzCalculator()
    for x in range(1, 101):
        print fizzBuzzCalculator.checkNumber(x)


if __name__ == '__main__':
    main()
