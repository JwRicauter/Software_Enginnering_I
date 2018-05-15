import re

###############################################################################################
#																							  #
#																							  #	
#	Tarea Numero Tres																		  #	
#	Ingenieria del Software I 																  #	
# 	Integrantes: 																			  #
# 		David Cabeza, 13 																	  #
#		Jawil Ricauter, 13-11199 															  #
#																							  #
# 																							  #
###############################################################################################

def validacionClave(clave):
	

	# Verificamos la longitud de las claves.
	if(len(clave) < 8 or len(clave) > 16):
		raise NameError("Clave invalida, las claves deben tener entre 8 y 16 caracteres")			

	# Verificamos que no existan caracteres especiales en las claves.
	if not (clave.isalnum()):
		raise NameError("Clave invalida, las claves deben ser alfanumericas")			

	# Verificamos que la clave tenga mas de dos letras, con al menos una mayuscula
	# y una minuscula.
	cantLetras = 0
	cantMay = 0
	for letra in clave:
		if (letra.isalpha()):
			cantLetras += 1
		if(letra.isupper()):
			cantMay += 1
	
	if not (cantLetras > 2 and cantMay > 0 and cantLetras - cantMay > 0):
		raise NameError("Clave invalida, la clave debe tener al menos tres letras, con al menos una mayuscula y una minuscula")


	# Verificamos que la clave contenga al menos un digito
	hayNum = False
	for letra in clave:
		if letra.isdigit():
			hayNum = True

	if not (hayNum):
		raise NameError("Clave invalida, la clave debe contener al menos un digito")

	return True


class Seguridad:


	def __init__(self):
		self.diccionario = {}


	def registrarUsuario(self, eMail, claveUno, claveDos):

		# Verificamos si el email cumple el formato RFC 822.
		if (re.match(r"[^@]+@[^@]+\.[^@]+", eMail) == None):
			raise NameError("Correo electronico invalido, no cumple con el formato RFC 822")		
		
		# Verificamos si las claves coinciden.
		if(claveUno != claveDos):
			raise NameError("Clave invalida, las claves deben coincidir")

		validacionClave(claveUno)
		claveCodificada = claveUno[::-1]	
		self.diccionario[eMail] = claveCodificada

	def ingresarUsuario(self, eMail, clave):
		
		# Verificamos si el user existe
		userValido = False
		for mail in self.diccionario:
			if(mail == eMail):
				userValido = True

		claveValida = False
		if(userValido and self.diccionario[eMail] == clave[::-1]):
			claveValida = True	

		if not (userValido):
			print("Usuario invalido")
		elif not (claveValida):
			print("Clave invalida")
		if (userValido and claveValida):
			print("Usuario aceptado")


