import unittest
from main import list_user_free_pica


class ListUserFreePicaTest(unittest.TestCase):
    def test_list_user_free_pica(self):
        self.assertEqual(
            ["client1", "client3", "client4"],
            list_user_free_pica(),
        )
