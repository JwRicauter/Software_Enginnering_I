import unittest
from tarea2 import *


class TestTarifa(unittest.TestCase):
	unaTarifa = Tarifa(10, 20)
	print("unaTarifa = Tarifa(10, 20)")
	print("Probando los valores iniciales de las tarifas...")
	print("Esta es la tarifa de un dia entre Lunes y Viernes")
	print(unaTarifa.tarifaDiaDeSemana)
	print("Esta es la tarifa de un dia de fin de semana")
	print(unaTarifa.tarifaFinDeSemana)


class TestTiempo(unittest.TestCase):
	

	def testEsFinDeSemana(self):

		# Prueba por frontera
		tiempo1 = Tiempo("Sabado", "01", "01", "2000", 12)
		self.assertTrue(tiempo1.esFinDeSemana(), "El dia deberia ser sabado o domingo")

		tiempo2 = Tiempo("Domingo", "01", "01", "2000", 12)
		self.assertTrue(tiempo2.esFinDeSemana(), "El dia deberia ser sabado o domingo")

		# Prueba por esquina

		tiempo3 = Tiempo("Lunes", "01", "01", "2000", 12)
		self.assertTrue(tiempo2.esFinDeSemana(), "El dia deberia ser sabado o domingo")

		# Prueba por malicia

		tiempo4 = Tiempo("lunmar", "01", "01", "2000", 12)
		self.assertTrue(tiempo2.esFinDeSemana(), "El dia deberia ser sabado o domingo")


	def testEsDiaDeSemana(self):

		# Prueba por frontera
		tiempo1 = Tiempo("Viernes", "01", "01", "2000", 12)
		self.assertTrue(tiempo1.esDiaDeSemana(), "El dia deberia ser entre lunes y viernes")

		tiempo2 = Tiempo("Lunes", "01", "01", "2000", 12)
		self.assertTrue(tiempo2.esDiaDeSemana(), "El dia deberia ser entre lunes y viernes")

		# Prueba por esquina

		tiempo3 = Tiempo("Sabado", "01", "01", "2000", 12)
		self.assertTrue(tiempo2.esDiaDeSemana(), "El dia deberia ser entre lunes y viernes")

		# Prueba por malicia

		tiempo4 = Tiempo("lunmar", "01", "01", "2000", 12)
		self.assertTrue(tiempo2.esDiaDeSemana(), "El dia deberia ser entre lunes y viernes")


	def testNumeroDia(self):
 
		# Prueba por frontera

		tiempo1 = Tiempo("lunes", "01", "01", "2000", 12)
		self.assertEqual(0, tiempo1.numeroDia())

		# Prueba por esquina

		tiempo2 = Tiempo("domingo", "01", "01", "2000", 12)
		self.assertEqual(6, tiempo2.numeroDia())

		# Prueba por malicia

		tiempo3 = Tiempo("sunday", "01", "01", "2000", 12)
		self.assertEqual(False, tiempo3.numeroDia())







if __name__ == "__main__":
	unittest.main() # run all tests
