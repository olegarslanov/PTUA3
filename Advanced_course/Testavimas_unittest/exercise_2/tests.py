import unittest
from main import Sakinys


# klase TestSakinys paveldi klase unittest.TestCase
class TestSakinys(unittest.TestCase):
    # setUp tai metodas unittest modulyje, kuris paleidziamas pries kiekviena testa (inicializuoti testo objektus ir duomenys)
    def setUp(self):
        self.object = Sakinys("Mano tekstas yra toks")

    def test_atbulai1(self):
        rezultatas = self.object.atbulai()
        lukestis = "skot ary satsket onaM"
        self.assertEqual(lukestis, rezultatas)

    def test_atbulai2(self):
        rezultatas = Sakinys().atbulai()
        lukestis = "nohtyP fo neZ"
        self.assertEqual(lukestis, rezultatas)

    def test_didziosiomis1(self):
        self.assertEqual(self.object.didziosiomis(), "MANO TEKSTAS YRA TOKS")

    def test_mazosiomis(self):
        self.assertEqual(self.object.mazosiomis(), "mano tekstas yra toks")

    def test_ieskoti(self):
        self.assertEqual(self.object.ieskoti("a"), 3)
        self.assertEqual(self.object.ieskoti("m"), 0)

    def test_pakeisti(self):
        self.assertEqual("Savo tekstas yra toks", self.object.pakeisti("Mano", "Savo"))

    def test_atspausdinti_zodi(self):
        self.assertEqual(self.object.atspausdinti_zodi(1), "tekstas")
        self.assertEqual(self.object.atspausdinti_zodi(2), "yra")

    def test_info(self):
        self.assertEqual(
            self.object.info(),
            "Žodžių kiekis: 4, Skaičiai: 0, Didžiosios: 1, Mažosios: 17",
        )
