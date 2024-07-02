import unittest # biblioteca estándar para escribir y ejecutar pruebas
from Modsuma.suma import add # type: ignore # Importa la función add desde el módulo suma dentro del paquete suma

class TestAddFunction(unittest.TestCase): # definición de la clase de prueba
    def test_add(self): # método de prueba
        self.assertEqual(add(2, 3), 5) # Llama a la función add con los argumentos 2 y 3, y verifica que el resultado sea 5. Si el resultado no es 5, la prueba fallará.
        self.assertEqual(add(-1, 1), 6)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':  #  Esta línea verifica si el script se está ejecutando directamente (no importado como un módulo)
    unittest.main()
