import unittest
import os
import sys
import inspect


from kataromannumerals import KataRomanNumerals, OrderNumeral, OrderOnes


class TestForKataRomanNumerals(unittest.TestCase):
    def setUp(self):
        '''We are assuming that there is no side effects to the different methods executed'''
        self.romanNumerals=KataRomanNumerals()

    def test_convert_1_I(self):
        result = self.romanNumerals.convert(1)
        self.assertEqual(result,'I')


    def test_convert_2_II(self):
        result = self.romanNumerals.convert(2)
        self.assertEqual(result,'II')

    def test_convert_1623_MDCXXIII(self):
        result = self.romanNumerals.convert(1623)
        self.assertEqual(result, 'MDCXXIII')


    def test_find_order_len_equals_position_None(self):
        result = self.romanNumerals.find_order(0,0)
        self.assertEqual(result, OrderNumeral.undetermined)
        result = self.romanNumerals.find_order(1,1)
        self.assertEqual(result, OrderNumeral.undetermined)
        result = self.romanNumerals.find_order(2,2)
        self.assertEqual(result, OrderNumeral.undetermined)
        result = self.romanNumerals.find_order(3,3)
        self.assertEqual(result, OrderNumeral.undetermined)


    def test_find_order_len_smaller_position_None(self):
        result = self.romanNumerals.find_order(0,1)
        self.assertEqual(result, OrderNumeral.undetermined)
        result = self.romanNumerals.find_order(1,2)
        self.assertEqual(result, OrderNumeral.undetermined)
        result = self.romanNumerals.find_order(2,3)
        self.assertEqual(result, OrderNumeral.undetermined)
        result = self.romanNumerals.find_order(3,4)
        self.assertEqual(result, OrderNumeral.undetermined)


    def test_find_order_ones(self):
        result = self.romanNumerals.find_order(1,0)
        self.assertEqual(result, OrderNumeral.ones)
        result = self.romanNumerals.find_order(2,1)
        self.assertEqual(result, OrderNumeral.ones)
        result = self.romanNumerals.find_order(3,2)
        self.assertEqual(result, OrderNumeral.ones)
        result = self.romanNumerals.find_order(4,3)
        self.assertEqual(result, OrderNumeral.ones)

 
    def test_find_order_tens(self):
        result = self.romanNumerals.find_order(2,0)
        self.assertEqual(result, OrderNumeral.tens)
        result = self.romanNumerals.find_order(3,1)
        self.assertEqual(result, OrderNumeral.tens)
        result = self.romanNumerals.find_order(4,2)
        self.assertEqual(result, OrderNumeral.tens)


    def test_find_order_hundreds(self):
        result = self.romanNumerals.find_order(3,0)
        self.assertEqual(result, OrderNumeral.hundreds)
        result = self.romanNumerals.find_order(4,1)
        self.assertEqual(result, OrderNumeral.hundreds)


    def test_find_order_thousands(self):
        result = self.romanNumerals.find_order(4,0)
        self.assertEqual(result, OrderNumeral.thousands)

    def test_get_roman_for_digit_on_order_Order1(self):
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '1')
        self.assertEqual(result, 'I')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '2')
        self.assertEqual(result, 'II')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '3')
        self.assertEqual(result, 'III')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '4')
        self.assertEqual(result, 'IV')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '5')
        self.assertEqual(result, 'V')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '6')
        self.assertEqual(result, 'VI')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '7')
        self.assertEqual(result, 'VII')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '8')
        self.assertEqual(result, 'VIII')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.ones, '9')
        self.assertEqual(result, 'IX')


    def test_get_roman_for_digit_on_order_Order2(self):
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '1')
        self.assertEqual(result, 'X')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '2')
        self.assertEqual(result, 'XX')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '3')
        self.assertEqual(result, 'XXX')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '4')
        self.assertEqual(result, 'XL')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '5')
        self.assertEqual(result, 'L')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '6')
        self.assertEqual(result, 'LX')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '7')
        self.assertEqual(result, 'LXX')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '8')
        self.assertEqual(result, 'LXXX')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.tens, '9')
        self.assertEqual(result, 'XC')


    def test_get_roman_for_digit_on_order_Order3(self):
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '1')
        self.assertEqual(result, 'C')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '2')
        self.assertEqual(result, 'CC')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '3')
        self.assertEqual(result, 'CCC')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '4')
        self.assertEqual(result, 'CD')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '5')
        self.assertEqual(result, 'D')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '6')
        self.assertEqual(result, 'DC')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '7')
        self.assertEqual(result, 'DCC')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '8')
        self.assertEqual(result, 'DCCC')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.hundreds, '9')
        self.assertEqual(result, 'CM')

    def test_get_roman_for_digit_on_order_Order4(self):
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.thousands, '1')
        self.assertEqual(result, 'M')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.thousands, '2')
        self.assertEqual(result, 'MM')
        result = self.romanNumerals.get_roman_for_digit_on_order(OrderNumeral.thousands, '3')
        self.assertEqual(result, 'MMM')


    def test_factoryOrders_Ones(self):
        order = self.romanNumerals.factoryOrders(OrderNumeral.ones)
        self.assertTrue(type(order) is OrderOnes)

    def test_getCharacter_OrderOnes(self):
        orderOnes = OrderOnes()
        self.assertEqual(orderOnes.getCharacter('1'),'I')

def main():
	suite = unittest.TestLoader().loadTestsFromTestCase(TestForKataRomanNumerals)
	unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
