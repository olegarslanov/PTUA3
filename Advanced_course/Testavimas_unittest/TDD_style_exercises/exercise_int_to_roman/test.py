import unittest
from main import convert_int_to_roman


class TestConvertIntToRoman(unittest.TestCase):
    def test_convert_five_correctly(self):
        self.assertEqual(convert_int_to_roman(5), "V")

    def test_convert_nine_correctly(self):
        self.assertEqual(convert_int_to_roman(9), "IX")

    def test_convert_fourty_correctly(self):
        self.assertEqual(convert_int_to_roman(40), "XL")

    def test_convert_to_one_ninty_zero_four_correctly(self):
        self.assertEqual(convert_int_to_roman(1904), "MCMIV")
