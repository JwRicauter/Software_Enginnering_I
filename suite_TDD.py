import unittest
from tarea_TDD import *

###############################################################################################
#																							  #
#																							  #	
#	Tarea Numero Dos																		  #	
#	Ingenieria del Software I 																  #	
# 	Integrantes: 																			  #
# 		Nairelys Hernandez, 12-10199 														  #
#		Jawil Ricauter, 13-11199 															  #
#																							  #
# 																							  #
###############################################################################################


class TestTarifa(unittest.TestCase):

	def testTarifa(self):
		unaTarifa = Tarifa(10.0, 20.0)
		self.assertTrue(type(unaTarifa.tarifaNoFin) == float, "El tiempo de la tarifa deberia ser decimal")
		self.assertTrue(type(unaTarifa.tarifaFin) == float, "El tiempo de la tarifa deberia ser decimal")


class TestTiempo(unittest.TestCase):



	def testTiempoDeTrabajo(self):


		# Pruebas por esquina

		datetime1 = datetime(2018, 5, 10, 0, 0)
		datetime2 = datetime(2018, 5, 17, 0, 0)
		tiempo1 = Tiempo(datetime1, datetime2)
		
		datetime3 = datetime(2018, 5, 17, 0, 0)
		datetime4 = datetime(2018, 5, 17, 0, 15)
		tiempo2 = Tiempo(datetime3, datetime4)

		# Pruebas por frontera

		datetime5 = datetime(2018, 5, 10, 21, 0)
		datetime6 = datetime(2018, 5, 13, 0, 0)
		tiempo3 = Tiempo(datetime5, datetime6)

		# Pruebas por malicia

		datetime7 = datetime(2018, 5, 10, 21, 43)
		datetime8 = datetime(2018, 5, 15, 12, 21)
		tiempo4 = Tiempo(datetime7, datetime8)


		test1 = tiempo1.tiempoDeTrabajo()
		minuto1 = (test1.seconds // 60) % 60

		if test1.days == 0:
			self.assertTrue(minuto1 >= 15, "La cantidad minima de minutos es 15 con 0 dias")
		elif test1.days != 0 and test1.seconds > 0:
			self.assertTrue(testo1.days <= 6, "No puedes tener mas de 0 horas con 7 dias")
		elif test1.days != 0 and test1.seconds == 0:	
			self.assertTrue(test1.days <= 7, "La cantidad maxima de dias es 7 con 0 minutos")

		test2 = tiempo2.tiempoDeTrabajo()
		minuto2 = (test2.seconds // 60) 

		if test2.days == 0:
			self.assertTrue(minuto2 >= 15, "La cantidad minima de minutos es 15 con 0 dias")
		elif test2.days != 0 and test2.seconds > 0:
			self.assertTrue(testo2.days <= 6, "No puedes tener mas de 0 horas con 7 dias")
		elif test2.days != 0 and test2.seconds == 0:	
			self.assertTrue(test2.days <= 7, "La cantidad maxima de dias es 7 con 0 minutos")


		test3 = tiempo3.tiempoDeTrabajo()
		minuto3 = (test3.seconds // 60) % 60

		if test3.days == 0:
			self.assertTrue(minuto3 >= 15, "La cantidad minima de minutos es 15 con 0 dias")
		elif test3.days != 0 and test3.seconds > 0:
			self.assertTrue(test3.days <= 6, "No puedes tener mas de 0 horas con 7 dias")
		elif test3.days != 0 and test3.seconds == 0:	
			self.assertTrue(test3.days <= 7, "La cantidad maxima de dias es 7 con 0 minutos")

		test4 = tiempo4.tiempoDeTrabajo()		
		minuto4 = (test4.seconds // 60) % 60

		if test4.days == 0:
			self.assertTrue(minuto4 >= 15, "La cantidad minima de minutos es 15 con 0 dias")
		elif test4.days != 0 and test4.seconds > 0:
			self.assertTrue(test4.days <= 6, "No puedes tener mas de 0 horas con 7 dias")
		elif test4.days != 0 and test4.seconds == 0:	
			self.assertTrue(test4.days <= 7, "La cantidad maxima de dias es 7 con 0 minutos")
		

	def testHorasDeFinDeSemanaTotales(self):


		# Pruebas por esquina

		datetime1 = datetime(2018, 5, 10, 0, 0)
		datetime2 = datetime(2018, 5, 17, 0, 0)
		tiempo1 = Tiempo(datetime1, datetime2)
		
		datetime3 = datetime(2018, 5, 17, 0, 0)
		datetime4 = datetime(2018, 5, 17, 0, 15)
		tiempo2 = Tiempo(datetime3, datetime4)

		# Pruebas por frontera

		datetime5 = datetime(2018, 5, 10, 21, 0)
		datetime6 = datetime(2018, 5, 13, 0, 0)
		tiempo3 = Tiempo(datetime5, datetime6)

		# Pruebas por malicia

		datetime7 = datetime(2018, 5, 10, 21, 43)
		datetime8 = datetime(2018, 5, 15, 12, 21)
		tiempo4 = Tiempo(datetime7, datetime8)


		test1 = tiempo1.horasDeFinDeSemanaTotales()
		self.assertTrue(test1 == 48, "Si se introduce una semana completa, la cantidad de horas de Fin de Semana deberia ser 48")

		test2 = tiempo2.horasDeFinDeSemanaTotales()
		self.assertTrue(test2 == 0, "Si se introduce 15 min un jueves, la cantidad de horas de fin de semana deberia ser 0")

		test3 = tiempo3.horasDeFinDeSemanaTotales()
		self.assertTrue(test2 > 24, "Para una semana que incluye un sabado, la cantidad de horas de fin de semana deberia ser mayor a 24")

		test4 = tiempo4.horasDeFinDeSemanaTotales()
		self.assertTrue(test1 == 48, "Si se introduce una semana que incluya un fin, la cantidad de horas de Fin de Semana deberia ser 48")				


if __name__ == "__main__":
	unittest.main() # run all tests




















