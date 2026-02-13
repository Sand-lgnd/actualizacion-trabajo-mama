import unittest
from unittest.mock import patch, MagicMock
import trabajo_mama

class TestNewLogic(unittest.TestCase):

    @patch('trabajo_mama.ejecutar_query')
    def test_obtener_movimientos_proximos_7_dias(self, mock_ejecutar):
        mock_ejecutar.return_value = [('Calamar', 10), ('Pota', 5)]

        tipo_mov = 'S'
        fecha_inicio = '2023-05-01'
        resultado = trabajo_mama.obtener_movimientos_proximos_7_dias(tipo_mov, fecha_inicio)

        # Verificar que ejecutar_query fue llamado con el SQL y parámetros correctos
        args, kwargs = mock_ejecutar.call_args
        query = args[0]
        params = args[1]

        self.assertIn("BETWEEN %s AND DATE_ADD(%s, INTERVAL 6 DAY)", query)
        self.assertEqual(params, (tipo_mov, fecha_inicio, fecha_inicio))
        self.assertEqual(resultado, [('Calamar', 10), ('Pota', 5)])

    @patch('trabajo_mama.ejecutar_query')
    def test_obtener_movimientos_mes_concreto(self, mock_ejecutar):
        mock_ejecutar.return_value = [('Calamar', 100)]

        tipo_mov = 'E'
        mes = 5
        resultado = trabajo_mama.obtener_movimientos_mes_concreto(tipo_mov, mes)

        args, kwargs = mock_ejecutar.call_args
        query = args[0]
        params = args[1]

        self.assertIn("MONTH(m.fecha_mov) = %s", query)
        self.assertEqual(params, (tipo_mov, mes))
        self.assertEqual(resultado, [('Calamar', 100)])

    @patch('trabajo_mama.ejecutar_query')
    def test_obtener_total_movimientos_por_nombre(self, mock_ejecutar):
        mock_ejecutar.return_value = [(150,)]

        tipo_mov = 'S'
        search_term = 'Calamar'
        resultado = trabajo_mama.obtener_total_movimientos_por_nombre(tipo_mov, search_term)

        args, kwargs = mock_ejecutar.call_args
        query = args[0]
        params = args[1]

        self.assertIn("p.producto LIKE %s", query)
        self.assertEqual(params, (tipo_mov, '%Calamar%'))
        self.assertEqual(resultado, 150)

if __name__ == '__main__':
    unittest.main()
