from collections import OrderedDict

from unittest import TestCase, main
from RomanNumeralGenerator import RomanNumeralGenerator

def write_roman(num):
    """ this is a thing to check the content of 
    the string taken from stack exchange
    """

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

class mainUnitTest(TestCase):

    def test_convert(self):
        testInt = 4999
        test = RomanNumeralGenerator().convertNumber(testInt)

        print(test)
        print(write_roman(testInt))
        self.assertEqual(
            type(test),
            str
        )

        self.assertEqual(
            write_roman(testInt),
            test
        )

if __name__ == '__main__':
    main()