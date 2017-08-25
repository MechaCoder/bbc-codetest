from random import randint

from unittest import TestCase, main
from RomanNumeralGenerator import romannumeralgenerator

def write_roman(num):
    """
    this is control function this a soultion
    i found on stackexchange this and has no bearing on the code
    i have actally wrritten, this is here becouse it is a peer
    reviewd soultions
    (https://stackoverflow.com/a/40274588/6779610)
    """

    num_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman


class MainUnitTest(TestCase):
    """ the main unittesting class that runs all unittests"""

    def test_convert(self):
        """
        testing weather the returned value
        is of the correct type and weather
        a fixed value is correct.
        """
        testint = 3999
        test = romannumeralgenerator(testint)

        self.assertEqual(
            type(test),
            str
        )

        self.assertEqual(
            write_roman(testint),
            test
        )

    def test_convert_onmass(self):
        """ tests the correctness of of returned value based on a random
        genrated integer based on the contraolled function
        """

        for x in range(0, 120):
            testInt = randint(1, 3999)

            self.assertEqual(
                write_roman(testInt),
                romannumeralgenerator(testInt)
            )

if __name__ == '__main__':
    main()