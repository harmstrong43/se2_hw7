import unittest
import part1

class TestProgram(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(part1.fizz(3),("Fizz"))