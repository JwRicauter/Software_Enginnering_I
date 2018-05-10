diasDeSemana = ['lunes','martes','miercoles','jueves','viernes']
diasDeFinDeSemana = ['sabado','domingo']
diasSemana =  ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
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
		if self.diaSemana.lower() in diasSemana :
			return diasSemana.index(self.diaSemana)
		return False


def calcularPrecio(tarifa,tiempoDeServicio):
	cuentaDia = tiempoDeServicio[0].numeroDia() -1
	total_dias = tiempoDeServicio[1].dia - tiempoDeServicio[0].dia
	pago_total = 0
	
	if tiempoDeServicio[0].dia==tiempoDeServicio[1].dia and tiempoDeServicio[0].hora<tiempoDeServicio[1].hora:
		if tiempoDeServicio[0].esDiaDeSemana():
			pago_total += (tiempoDeServicio[1].hora - tiempoDeServicio[0].hora )* tarifa.tarifaDiaDeSemana
		else:
			pago_total += (tiempoDeServicio[1].hora - tiempoDeServicio[0].hora )* tarifa.tarifaFinDeSemana 
	elif tiempoDeServicio[0].dia<tiempoDeServicio[1].dia:
		x = 0
		while x != total_dias:
			cuentaDia +=1
			
			if 0<=cuentaDia<=4 :
				if x==0:
					pago_total += (24 - tiempoDeServicio[0].hora) *tarifa.tarifaDiaDeSemana 
					
				else:
					
					pago_total += 24 *tarifa.tarifaDiaDeSemana

			else:
				if x==0:

					pago_total += (24 - tiempoDeServicio[0].hora) *tarifa.tarifaFinDeSemana 

				else:
					pago_total += 24 *tarifa.tarifaFinDeSemana

			x+=1

			if cuentaDia==6:

				cuentaDia = 0

				
		if tiempoDeServicio[1].esDiaDeSemana():
			
			pago_total += tiempoDeServicio[1].hora * tarifa.tarifaDiaDeSemana
		else:
		
			pago_total += tiempoDeServicio[1].hora * tarifa.tarifaFinDeSemana
	return pago_total

################ Inicio de Prueba ############

#inicio = Tiempo ("jueves",1,5,2018,7)
#fin = Tiempo ("jueves",1,5,2018,20)

#inicio = Tiempo ("domingo",1,5,2018,7)
#fin = Tiempo ("domingo",1,5,2018,20)

inicio = Tiempo ("jueves",1,5,2018,7)
fin = Tiempo ("domingo",4,5,2018,8)

tarifa = Tarifa(20,25)
monto_total = calcularPrecio(tarifa,[inicio,fin])
print(monto_total)