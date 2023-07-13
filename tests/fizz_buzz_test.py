import unittest

from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
	def test_fizz(self):
		self.assertEqual("Fizz", fizz_buzz(3))
	def test_buzz(self):
		self.assertEqual("Buzz", fizz_buzz(5))
	def test_fizz_buzz(self):
		self.assertEqual("FizzBuzz", fizz_buzz(15))
	def test_other(self):
		self.assertEqual("7", fizz_buzz(7))