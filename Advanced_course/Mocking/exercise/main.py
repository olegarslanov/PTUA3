# Modulis, kurį norime ištestuoti
# calculator.py


def add_numbers(a, b):
    return a + b


# Testų failas
# test_calculator.py

import unittest
from unittest.mock import patch
from calculator import add_numbers


class CalculatorTest(unittest.TestCase):
    @patch("calculator.add_numbers")
    def test_add_numbers(self, mock_add):
        # Nustatome, kad fiktyvus add_numbers grąžintų reikšmę 10
        mock_add.return_value = 10

        result = add_numbers(5, 3)

        # Tikriname, ar funkcija add_numbers buvo iškviečiama su teisingais argumentais
        mock_add.assert_called_once_with(5, 3)
        # Tikriname, ar gautas rezultatas yra teisingas
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
