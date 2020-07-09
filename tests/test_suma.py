import unittest
import sys
sys.path.append('../')
from calculadora import Suma

class TestBasicos(unittest.TestCase):
	
	def test_suma_valor_cero(self):
		calc = Suma()
		self.assertEqual(0,calc.valor())

	def test_suma_de_dos_valores_es_1000(self):
		calc = Suma()
		calc.suma(200,800)
		self.assertEqual(1000,calc.valor())

	def test_suma_de_dos_valores_es_9(self):
		calc = Suma()
		calc.suma(6,3)
		self.assertEqual(9,calc.valor())