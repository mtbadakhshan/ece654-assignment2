import unittest
from src.fib import fibonacci

class TestAuth(unittest.TestCase):

	def test_check_output(self):
		result = fibonacci(6)
		self.assertEqual(result, 8)
		result = fibonacci(10)
		self.assertEqual(result, 55)
		result = fibonacci(20)
		self.assertEqual(result, 6765)


if __name__ == '__main__':
    unittest.main()