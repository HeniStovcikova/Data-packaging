import unittest

def is_evennumber(n):
    return n % 2 == 0


class TestIsEvenNumber(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_evennumber(4))

    def test_odd_number(self):
        self.assertFalse(is_evennumber(7))

    def test_zero(self):
        self.assertTrue(is_evennumber(0))


if __name__ == '__main__':
    unittest.main()