import unittest
from unittest.mock import patch
import xmlrunner

from io import StringIO


# Suponiendo que el código principal con la función nominaDocente se encuentra en un archivo llamado "nomina.py"
from nomina import nominaDocente, leer_tipo_contrato, leer_entero_no_negativo

class TestNominaDocente(unittest.TestCase):

    # Caso 1: Ingresar un valor negativo en las horas extras diurnas.
    @patch('builtins.input', side_effect=['-5', '2'])
    def test_horas_negativas(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_entero_no_negativo("Ingrese horas extra diurnas: ")
            self.assertEqual(resultado, 2)
            output = mock_stdout.getvalue()
            self.assertIn("No se permiten números negativos.", output)

    # Caso 2: Ingresar un valor no numérico en las horas extras nocturnas.
    @patch('builtins.input', side_effect=['abc', '2'])
    def test_horas_no_numericas(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_entero_no_negativo("Ingrese horas extra nocturnas: ")
            self.assertEqual(resultado, 2)
            output = mock_stdout.getvalue()
            self.assertIn("Error: Ingrese un número entero válido (>= 0).", output)

    # Caso 3: Ingresar 0 horas en recargo nocturno.
    @patch('builtins.input', side_effect=['0'])
    def test_horas_zero_recargo_nocturno(self, mock_input):
        resultado = leer_entero_no_negativo("Ingrese recargo nocturno: ")
        self.assertEqual(resultado, 0)

    # Caso 4: Ingresar un número extremadamente grande en las horas extras diurnas dominicales/festivas.
    @patch('builtins.input', side_effect=['999999'])
    def test_horas_extras_grande(self, mock_input):
        resultado = leer_entero_no_negativo("Ingrese horas extra dominical/festiva diurna: ")
        self.assertEqual(resultado, 999999)

    # Caso 5: Omitir la entrada para las horas extras.
    @patch('builtins.input', side_effect=['', '2'])
    def test_entrada_vacia(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_entero_no_negativo("Ingrese horas extra diurnas: ")
            self.assertEqual(resultado, 2)
            output = mock_stdout.getvalue()
            self.assertIn("Error: Ingrese un número entero válido (>= 0).", output)

    # Caso 6: Seleccionar un tipo de contrato inválido.
    @patch('builtins.input', side_effect=['3', '1'])
    def test_tipo_contrato_invalido(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_tipo_contrato()
            self.assertEqual(resultado, 1)
            output = mock_stdout.getvalue()
            self.assertIn("Debe ingresar '1' para tiempo completo o '2' para medio tiempo.", output)
            
    # Prueba para el ValueError en leer_tipo_contrato y verificar el mensaje de error
    @patch('builtins.input', side_effect=['3', '1'])  # Simulamos que el usuario ingresa '3' y luego '1'
    def test_tipo_contrato_no_valido(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_tipo_contrato()  # Llamamos a la función leer_tipo_contrato
            self.assertEqual(resultado, 1)  # Después de rechazar '3', debería tomar '1'
            output = mock_stdout.getvalue()  # Capturamos la salida estándar
            # Verificamos si el mensaje de error esperado está en la salida
            self.assertIn("Error: Debe ingresar '1' para tiempo completo o '2' para medio tiempo.", output)
            
    # Prueba para validar el manejo del ValueError en leer_tipo_contrato
    @patch('builtins.input', side_effect=['abc', '1'])
    def test_tipo_contrato_no_numerico(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_tipo_contrato()
            self.assertEqual(resultado, 1)  # Después de rechazar 'abc', debería tomar '1'
            output = mock_stdout.getvalue()
            self.assertIn("Error: Debe ingresar un número entero (1 o 2).", output)
            
    
            
    # Prueba para validar el ValueError en nominaDocente
    def test_tipo_contrato_invalido(self):
        with self.assertRaises(ValueError) as context:
            nominaDocente(3, 5, 3, 2, 1, 2, 3, 4)  # '3' es un tipo de contrato inválido
        self.assertEqual(str(context.exception), "Tipo de contrato inválido. Use 1 para tiempo completo o 2 para medio tiempo.")
        

    # Caso 7: Seleccionar tipo de contrato 1 (tiempo completo) y no ingresar datos para las horas extras.
    @patch('builtins.input', side_effect=['1', '0', '0', '0', '0', '0', '0', '0'])
    def test_tipo_contrato_1_no_horas(self, mock_input):
        resultado = nominaDocente(1, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(resultado["base_salario"], 1423500)
        self.assertEqual(resultado["pago_extras"], 0)

    # Caso 8: Seleccionar tipo de contrato 2 (medio tiempo) y registrar valores válidos en los 7 tipos de horas extra.
    @patch('builtins.input', side_effect=['2', '1', '2', '3', '4', '5', '6', '7'])
    def test_tipo_contrato_2_valores_validos(self, mock_input):
        resultado = nominaDocente(2, 1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(resultado["base_salario"], 711750)
        self.assertGreater(resultado["pago_extras"], 0)

    # Caso 9: Ingresar un valor no entero en la hora extra diurna.
    @patch('builtins.input', side_effect=['3.5', '2'])
    def test_horas_no_enteras(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            resultado = leer_entero_no_negativo("Ingrese horas extra diurnas: ")
            self.assertEqual(resultado, 2)
            output = mock_stdout.getvalue()
            self.assertIn("Error: Ingrese un número entero válido (>= 0).", output)

    # Caso 10: Verificar el recálculo automático si se corrige un dato.
    @patch('builtins.input', side_effect=['-5', '10'])  # Mock de input para simular los valores negativos y positivos
    @patch('sys.stdout', new_callable=StringIO)  # Mock de la salida estándar para capturar los prints
    def test_recálculo_hora_extra(self, mock_stdout, mock_input):
        # Ejecutar la función que solicita la entrada
        resultado = leer_entero_no_negativo("Ingrese horas extra diurnas: ")

        # Verificamos que el resultado final sea 10
        self.assertEqual(resultado, 10)

        # Verificamos que se haya impreso el mensaje de error por el valor negativo
        output = mock_stdout.getvalue()
        self.assertIn("Error: No se permiten números negativos.", output)

    # Caso 11: Confirmar que se apliquen los recargos correctos en recargo dominical/festivo diurno.
    @patch('builtins.input', side_effect=['1'])
    def test_recargo_dominical_diurno(self, mock_input):
        resultado = leer_entero_no_negativo("Ingrese recargo dominical/festivo diurno (75%): ")
        self.assertEqual(resultado, 1)

    # Caso 12: Confirmar que se apliquen los recargos correctos en hora extra dominical/festiva diurna.
    @patch('builtins.input', side_effect=['2'])
    def test_recargo_extra_dominical_diurno(self, mock_input):
        resultado = leer_entero_no_negativo("Ingrese hora extra dominical/festiva diurna (100%): ")
        self.assertEqual(resultado, 2)

    # Caso 13: Validar el cálculo de descuentos de salud y pensión.
    @patch('builtins.input', side_effect=['2', '5', '3', '1', '2', '1', '2'])
    def test_calculo_descuentos(self, mock_input):
        resultado = nominaDocente(2, 5, 3, 1, 2, 1, 2, 1)
        self.assertGreater(resultado["descuento_salud"], 0)
        self.assertGreater(resultado["descuento_pension"], 0)

    # Caso 14: Ingresar valores mixtos en las horas extras.
    @patch('builtins.input', side_effect=['5', '0', '3', '4', '0', '2', '1'])
    def test_valores_mixtos(self, mock_input):
        resultado = nominaDocente(1, 5, 0, 3, 4, 0, 2, 1)
        self.assertEqual(resultado["base_salario"], 1423500)
        self.assertGreater(resultado["pago_extras"], 0)

    # Caso 15: Confirmar la suma del salario mínimo completo con los recargos.
    @patch('builtins.input', side_effect=['1', '5', '0', '1', '2', '3', '4'])
    def test_salario_completo_con_recargos(self, mock_input):
        resultado = nominaDocente(1, 5, 0, 1, 2, 3, 4, 5)
        self.assertGreater(resultado["pago_total_bruto"], 1423500)

    # Caso 16: Confirmar la suma de medio salario mínimo con los recargos.
    @patch('builtins.input', side_effect=['2', '5', '1', '3', '2', '4', '5'])
    def test_salario_medio_con_recargos(self, mock_input):
        resultado = nominaDocente(2, 5, 1, 3, 2, 4, 5, 6)
        self.assertGreater(resultado["pago_total_bruto"], 711750)

    # Caso 17: Ingresar valores altos en todos los campos de horas.
    @patch('builtins.input', side_effect=['100', '100', '100', '100', '100', '100', '100'])
    def test_valores_altos(self, mock_input):
        resultado = nominaDocente(1, 100, 100, 100, 100, 100, 100, 100)
        self.assertGreater(resultado["pago_extras"], 0)

    # Caso 18: Ingresar todos los campos de horas en 0.
    @patch('builtins.input', side_effect=['0', '0', '0', '0', '0', '0', '0'])
    def test_todas_las_horas_en_cero(self, mock_input):
        resultado = nominaDocente(1, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(resultado["base_salario"], 1423500)
        self.assertEqual(resultado["pago_extras"], 0)

    # Caso 19: Confirmar el redondeo a dos decimales.
    @patch('builtins.input', side_effect=['2', '2', '2', '2', '2', '2', '2'])
    def test_redondeo_dos_decimales(self, mock_input):
        resultado = nominaDocente(1, 2, 2, 2, 2, 2, 2, 2)
        self.assertEqual(round(resultado["pago_total_bruto"], 2), resultado["pago_total_bruto"])

    # Caso 20: Verificar el mensaje final con el resumen de cálculos.
    # Prueba 20: Verificar el mensaje final con el resumen de cálculos (usando return)
    @patch('builtins.input', side_effect=['1', '5', '3', '2', '1', '2', '3'])
    def test_resumen_final(self, mock_input):
        # Valores de ejemplo
        tipo_contrato = 1  # Tiempo completo
        horas_extra_diurna = 5
        horas_extra_nocturna = 3
        recargo_nocturno = 2
        horas_extra_dominical_diurna = 4
        recargo_dominical_diurno = 3
        horas_extra_nocturna_dominical = 2
        recargo_dominical_nocturno = 1

        # Llamada a la función
        resultado = nominaDocente(tipo_contrato, horas_extra_diurna, horas_extra_nocturna, recargo_nocturno, 
                                horas_extra_dominical_diurna, recargo_dominical_diurno, horas_extra_nocturna_dominical, 
                                recargo_dominical_nocturno)

        # Cálculos manuales esperados (según los valores de las horas y los recargos)
        hora_base = 5197
        pago_extras_esperado = (
            5 * hora_base * 1.25 + 3 * hora_base * 1.75 + 2 * hora_base * 1.35 +
            4 * hora_base * 2.00 + 3 * hora_base * 1.75 + 2 * hora_base * 2.10 +
            1 * hora_base * 2.10
        )

        salario_base_esperado = 1423500
        pago_total_bruto_esperado = salario_base_esperado + pago_extras_esperado
        descuento_salud_esperado = pago_total_bruto_esperado * 0.04
        descuento_pension_esperado = pago_total_bruto_esperado * 0.04
        pago_neto_esperado = pago_total_bruto_esperado - (descuento_salud_esperado + descuento_pension_esperado)

        # Verificar los valores calculados
        self.assertEqual(resultado["base_salario"], salario_base_esperado)
        self.assertEqual(resultado["pago_total_bruto"], round(pago_total_bruto_esperado, 2))
        self.assertEqual(resultado["pago_neto"], round(pago_neto_esperado, 2))




if __name__ == '__main__':
    unittest.main()