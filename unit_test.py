import unittest
from app import app

class IsPrimeFunction(unittest.TestCase):

    def test_true_when_x_is_17(self):
        result = app.is_prime(17)
        self.assertTrue(result,'true')

    def test_false_when_x_is_36(self):
        result = app.is_prime(36)
        self.assertTrue(result,'false')

    def test_true_when_x_is_13219(self):
        result = app.is_prime(13219)
        self.assertTrue(result,'true')

if __name__ == '__main__':
    unittest.main()
