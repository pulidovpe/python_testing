import unittest
import sys
sys.path.append('../')

from calculadora import Calculadora


class PruebasBasicas(unittest.TestCase):

    def test_restar(self):
        calc = Calculadora()
        self.assertEqual(calc.restar(10, 3), 7)


if __name__ == '__main__':
    unittest.main()
