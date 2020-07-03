import unittest

from calculadora import Calculadora


class PruebasBasicas(unittest.TestCase):

    def test_sumar(self):
        calc = Calculadora()
        self.assertEqual(calc.sumar(7, 6), 13)

    def test_restar(self):
        calc = Calculadora()
        self.assertEqual(calc.restar(5, 2), 3)


if __name__ == '__main__':
    unittest.main()
