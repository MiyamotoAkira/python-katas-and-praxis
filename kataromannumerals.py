import enum_ForPython2


OrderNumeral = enum_ForPython2.enum('undetermined', 'ones', 'tens', 'hundreds', 'thousands')

class KataRomanNumerals(object):
    def convert(self, number):
        digits = self.get_digits(number)
        list_of_characters = [self.get_roman_character(digits,position) for position in range(len(digits))]
        finalNumber = ''.join(list_of_characters)
        return finalNumber
    
    def get_digits(self, number):
        digits = str(number)
        return digits
    
    
    def get_roman_character(self, digits, position):
        order = self.find_order(len(digits), position)
        digit = digits[position:position + 1]
        character = self.get_roman_for_digit_on_order(order, digit)
        return character
    
    
    def get_roman_for_digit_on_order(self, order, digit):
        orderCharacterFinder = self.factoryOrders(order)
        return orderCharacterFinder.getCharacter(digit)


    def find_order(self, length_of_number, position):
        difference = length_of_number - position
        if difference == 1:
            return OrderNumeral.ones
        elif difference == 2:
            return OrderNumeral.tens
        elif difference == 3:
            return OrderNumeral.hundreds
        elif difference == 4:
            return OrderNumeral.thousands
        else:
            return OrderNumeral.undetermined

    def factoryOrders(self, order):
        if order == OrderNumeral.ones:
            return OrderOnes()
        elif order == OrderNumeral.tens:
            return OrderTens()
        elif order == OrderNumeral.hundreds:
            return OrderHundreds()
        elif order == OrderNumeral.thousands:
            return OrderThousands()

class OrderOnes(object):
    def getCharacter(self, numeral):
        if numeral == '1':
            return 'I'
        elif numeral == '2':
            return 'II'
        elif numeral == '3':
            return 'III'
        elif numeral == '4':
            return 'IV'
        elif numeral == '5':
            return 'V'
        elif numeral == '6':
            return 'VI'
        elif numeral == '7':
            return 'VII'
        elif numeral == '8':
            return 'VIII'
        elif numeral == '9':
            return 'IX'

class OrderTens(object):
    def getCharacter(self, numeral):
        if numeral == '1':
            return 'X'
        elif numeral == '2':
            return 'XX'
        elif numeral == '3':
            return 'XXX'
        elif numeral == '4':
            return 'XL'
        elif numeral == '5':
            return 'L'
        elif numeral == '6':
            return 'LX'
        elif numeral == '7':
            return 'LXX'
        elif numeral == '8':
            return 'LXXX'
        elif numeral == '9':
            return 'XC'

class OrderHundreds(object):
    def getCharacter(self, numeral):
        if numeral == '1':
            return 'C'
        elif numeral == '2':
            return 'CC'
        elif numeral == '3':
            return 'CCC'
        elif numeral == '4':
            return 'CD'
        elif numeral == '5':
            return 'D'
        elif numeral == '6':
            return 'DC'
        elif numeral == '7':
            return 'DCC'
        elif numeral == '8':
            return 'DCCC'
        elif numeral == '9':
            return 'CM'

class OrderThousands(object):
    def getCharacter(self, numeral):
        if numeral == '1':
            return 'M'
        elif numeral == '2':
            return 'MM'
        elif numeral == '3':
            return 'MMM'

#I need classes for each OrderNumeral, so I can get the right roman character
