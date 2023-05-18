import unittest
from main import convert_int_to_fizz, convert_int_to_buzz, convert_int_to_fizzbuzz


class TestConvertIntToFizzBuzz(unittest.TestCase):
    def test_convert_fizz_corectly(self):
        self.assertEqual(convert_int_to_fizz(12), "fizz")

    def test_convert_buzz_correctly(self):
        self.assertEqual(convert_int_to_buzz(10), "buzz")

    def test_convert_fizzbuzz_correctly(self):
        self.assertEqual(convert_int_to_fizzbuzz(15), "fizzbuzz")
