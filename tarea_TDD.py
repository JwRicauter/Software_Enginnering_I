from datetime import *
from decimal import *

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


class Tarifa:
	def __init__(self, tarifaNoFin, tarifaFin):
		self.tarifaFin = tarifaFin
		self.tarifaNoFin = tarifaNoFin

class Tiempo:

	def __init__(self, inicioDeServicio, finDeServicio):
		self.inicioDeServicio = inicioDeServicio
		self.finDeServicio = finDeServicio

	def tiempoDeTrabajo(self):

		tiempoTotal = self.finDeServicio - self.inicioDeServicio
		hora = tiempoTotal.seconds // 3600
		
		# Pruebo que el tiempo minimo sea de 15 minutos y que el tiempo maximo sea de 7 dias

		minuto = (tiempoTotal.seconds // 60) % 60


		if tiempoTotal.days == 0:
			assert(minuto >= 15)
		elif tiempoTotal.days != 0 and tiempoTotal.seconds > 0:
			assert(tiempoTotal.days <= 6)
		elif tiempoTotal.days != 0 and tiempoTotal.seconds == 0:	
			assert(tiempoTotal.days <= 7)


		# Se redondea hacia arriba la hora	
		if minuto > 0:
		 	hora += 1

		fechaTotalRedondeada = timedelta(tiempoTotal.days, hora * 3600)	
		return fechaTotalRedondeada


	def horasDeFinDeSemanaTotales(self):
		fecha = self.inicioDeServicio.weekday()
		finesDeSemanasTotales = 0	
		for i in range(0, self.tiempoDeTrabajo().days):
			fecha += 1
			if (fecha == 7):
				fecha = 0
			if(fecha == 5 or fecha == 6):
				finesDeSemanasTotales += 1
		horasDeFin = finesDeSemanasTotales * 24		
		if ((fecha == 4 or fecha == 5) and ((self.tiempoDeTrabajo().seconds // 3600) > 0)):
			horasDeFin += (self.tiempoDeTrabajo().seconds // 3600)

		return horasDeFin				


def calcularPrecio(tarifa, tiempoDeServicio):		

	dias = tiempoDeServicio.tiempoDeTrabajo().days

	# Horas totales de tiempo de servicio
	horas = tiempoDeServicio.tiempoDeTrabajo().seconds // 3600 + (dias * 24)

	# Horas totales de tiempo de servicio un fin de semana
	totalFinesSemana = tiempoDeServicio.horasDeFinDeSemanaTotales()


	# Probamos los datos introducimos por las tarifas.

	tarifaEntreSemana = tarifa.tarifaNoFin
	tarifaFinSemana = tarifa.tarifaFin

	assert(type(tarifaEntreSemana) == float)
	assert(type(tarifaFinSemana) == float)



	totalGananciaEntreSemana = (horas - totalFinesSemana) * tarifaEntreSemana
	totalGananciaFinSemana = totalFinesSemana * tarifaFinSemana

	totalPrecio = totalGananciaEntreSemana + totalGananciaFinSemana

	return totalPrecio





# uno = datetime(2018, 5, 16, 22, 0)
# dos = datetime(2018, 5, 10, 20, 0)
# tiempo = Tiempo(dos, uno)
# tarifa = Tarifa(10.0, 20.0)
# calcularPrecio(tarifa, tiempo)
# print(tiempo.diasDeFinDeSemanaTotales())
# print(tiempoDeTrabajo(dos, uno))
# print(uno - dos)





		