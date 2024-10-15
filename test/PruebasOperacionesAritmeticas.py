import unittest
from src.logica.OperacionesAritmeticas import OperacionesAritmeticas

class PruebaOperacionesAritmeticas(unittest.TestCase):

    def setUp(self):
        self.operacion = OperacionesAritmeticas()

    def tearDown(self):
        self.operacion = None
    def test_suma_dosEnteros_retornaSuma(self):
        # Arrange


        sumando1 = 10
        sumando2 = 20
        resultadoEsperado = 30

        # Do

        resultadoActual = self.operacion.suma(sumando1, sumando2)


        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_suma_dosFlotantes_retornaSuma(self):
        # Arrange


        sumando1 = 10.5
        sumando2 = 20.5
        resultadoEsperado = 31

        # Do

        resultadoActual = self.operacion.suma(sumando1, sumando2)

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_division_dosEnteros_retornCociente(self):
        # Arrange


        dividendo = 40
        divisor = 5
        resultadoEsperado = 8

        # Do

        resultadoActual = self.operacion.division(dividendo, divisor)

        # Assert

        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_division_DivisorCero_retornCociente(self):
        # Arrange


        #dividendo = 40.5
        #divisor = 0
        #resultadoEsperado = 7.363636363636363

        # Do

        #resultadoActual = self.operacion.division(dividendo, divisor)

        self.assertTrue(True)
        with self.assertRaises(ZeroDivisionError):
            self.operacion.division(5, 0)

    def test_division_dividendoDivisorNoNumerico_retornCociente(self):
        # Arrange


        #dividendo = 40.5
        #divisor = 0
        #resultadoEsperado = 7.363636363636363

        # Do

        #resultadoActual = self.operacion.division(dividendo, divisor)

        self.assertTrue(True)
        with self.assertRaises(TypeError):
            self.operacion.division(5, "a")



if __name__ == '__main__':
    unittest.main()
