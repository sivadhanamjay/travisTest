import unittest
from core.setup import calc_average
 
class TestUM(unittest.TestCase):
 
    def test_numbers_3_4(self):
        self.assertEqual( calc_average(), 12)
