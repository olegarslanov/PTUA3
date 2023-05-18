import unittest
from ar_keliamieji import ar_keliamieji


class TestIsLeap(unittest.TestCase):
    def test_returns_true_when_leap_year(self):
        result = ar_keliamieji(2000)
        self.assertTrue(result)

    def test_returns_false_when_not_leap_year(self):
        result = ar_keliamieji(2100)
        self.assertFalse(result)

    def test_returns_false_when_not_leap_year2(self):
        result = ar_keliamieji(2020)
        self.assertTrue(result)

    def test_raises_error_when_str_is_passed(self):
        with self.assertRaises(TypeError):
            ar_keliamieji("1234")

    def test_our_random_test(self):
        self.assertIsNotNone(obj="")


# Kad paleisti tik si faila:
# python -m unittest test_ar_keliamieji.py

# Kad paleisti visus unitest failus:
# Kad paleisti i komandine eilute ivedu: "python -m unittest"

# Kad galima butu tikrinti daugelio funkciju viename faile reiketu sukurti faila __init__.py
