# Tarifa: Obetoq que contiene infomacion sobre las tarifas por hora segun el dia de la semana 
class Tarifa:
	def __init__(self,tarifaDiaDeSemana,tarifaFinDeSemana):
		self.tarifaFinDeSemana = tarifaFinDeSemana
		self.tarifaDiaDeSemana = tarifaDiaDeSemana

# Tiempo : Objeto que indica el dia de la semana (nombre), fecha y hora de inicio y fin del servicio.
#			la hora es en formato 24h
class Tiempo:
	def __init__(self,diaSemana,dia,mes,anio, hora):
		self.diaSemana = diaSemana
		self.dia = dia
		self.mes = mes
		self.anio = anio
		self.hora = hora
	

	def esFinDeSemana(self):
		if self.diaSemana.lower() in diasDeFinDeSemana :
			return True
		else:
			return False;

	def esDiaDeSemana(self):
		if self.diaSemana.lower() in diasDeSemana :
			return True
		else:
			return False;
	
	def numeroDia(self):
		print(self.diaSemana.lower())
		if self.diaSemana.lower() in diasSemana :
			return diasSemana.index(self.diaSemana)
		return False


def calcularPrecio(tarifa,tiempoDeServicio):
	pass