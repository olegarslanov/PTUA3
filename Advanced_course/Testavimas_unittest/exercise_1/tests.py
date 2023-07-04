import unittest
from main import skaiciu_suma


# 1
class SkaiciuSumaTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(56, skaiciu_suma(45, 5, 6))

    def test_addition2(self):
        self.assertEqual(12, skaiciu_suma(12, -100, 100))

    def test_addition3(self):
        self.assertEqual(0, skaiciu_suma(100, -100, 0))


# 2
from main import saraso_suma


class SarasoSumaTest(unittest.TestCase):
    def test_addition1(self):
        self.assertEqual(95, saraso_suma([4, 5, 78, 8]))

    def test_addition2(self):
        self.assertEqual(12, saraso_suma([12, -100, 100, 0]))

    def test_addition3(self):
        self.assertEqual(0, saraso_suma([100, -100, 0]))


# 3
from main import didziausias_skaicius


class DidziausiasSkaiciusTest(unittest.TestCase):
    def test_max1(self):
        self.assertEqual(5, didziausias_skaicius(4, 5, 1, 3))
        self.assertEqual(didziausias_skaicius(-10, -5, -8, -2), -2)
        self.assertEqual(didziausias_skaicius("a", "b", "c"), "c")
        self.assertEqual(didziausias_skaicius(True, False, True), True)


# 4
from main import stringas_atbulai


class StringasAtbulaiTest(unittest.TestCase):
    def test_string_atbulai(self):
        self.assertEqual("enilno tseT", stringas_atbulai("Test online"))
        self.assertEqual("1tseT", stringas_atbulai("Test1"))
        self.assertEqual("akieroN satanoD", stringas_atbulai("Donatas Noreika"))


# 5
from main import info_apie_sakini


class InfoApieSakiniTest(unittest.TestCase):
    def test_info_apie_sakini(self):
        self.assertEqual(
            "Zodziu: 6, Didžiosios: 1, mažosios: 20, skaičiai: 3",
            info_apie_sakini("Laba diena laba diena lab 522"),
        )


# 6
from main import unikalus_sarasas


class UnikalusSarasasTest(unittest.TestCase):
    def test_unikalus_sarasas1(self):
        self.assertEqual(
            6, len(unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))
        )

    def test_unikalus_sarasas2(self):
        self.assertCountEqual(
            [4, 5, "Labas", 6, True, 10],
            unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]),
        )


# 7
from main import ar_pirminis


class ArPirminisTest(unittest.TestCase):
    def test_ar_pirminis1(self):
        self.assertTrue(ar_pirminis(5), True)

    def test_ar_pirminis2(self):
        self.assertFalse(ar_pirminis(4), False)

    def test_ar_pirminis3(self):
        self.assertTrue(ar_pirminis(7), True)


# 8
from main import isrikiuoti_nuo_galo


class IsrikiuotiNuoGaloTest(unittest.TestCase):
    def test_isrikiuoti_nuo_galo(self):
        self.assertCountEqual(
            "Vienas du trys keturi", isrikiuoti_nuo_galo("Vienas du trys keturi")
        )


# 9
from main import ar_keliamieji


class ArKeliamiejiTest(unittest.TestCase):
    def test_ar_keliamieji1(self):
        self.assertTrue(ar_keliamieji(2020), True)

    def test_ar_keliamieji2(self):
        self.assertFalse(ar_keliamieji(2100), False)

    def test_ar_keliamieji3(self):
        self.assertTrue(ar_keliamieji(2000), True)


# 10
from main import patikrinti_data


class PatikrintiDataTest(unittest.TestCase):
    def test_patikrinti_data(self):
        self.assertEqual(("Praėjo metų: ", 23), patikrinti_data("2000-01-01 12:12:12"))
