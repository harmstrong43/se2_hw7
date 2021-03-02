import unittest
import part1

class TestProgram(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(part1.fizz(3),("Fizz"))
        self.assertEqual(part1.buzz(5),("Buzz"))
        self.assertEqual(part1.fizzbuzz(15),("FizzBuzz"))