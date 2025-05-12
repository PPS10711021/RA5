import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_multiplicacion_positiva(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_multiplicacion_cero(self):
        self.assertEqual(self.calc.multiplicar(0, 100), 0)

    def test_multiplicacion_negativa(self):
        self.assertEqual(self.calc.multiplicar(-2, 5), -10)

if __name__ == "__main__":
    unittest.main()