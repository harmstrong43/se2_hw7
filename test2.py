import unittest
import part2

class TestProgram(unittest.TestCase):
    def test_leapyear(self):
        self.assertEqual(part2.leap(4),True)
        self.assertEqual(part2.leap(100),True)
        self.assertEqual(part2.leap(400),False)