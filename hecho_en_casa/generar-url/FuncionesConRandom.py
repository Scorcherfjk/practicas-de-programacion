import random

variable = ''

def mezclar(listaFuente,listaDestino):
	"""recibe 2 listas, la primera de donde sacara los datos y la segunda donde los va a introducir mezclados,
hecha para ser usada varias veces si es necesario con la misma lista de destino"""
	for i in listaFuente:
		listaDestino.append(i)
		random.shuffle(listaDestino)

def codigo(lista,longitud):
	"""recibe una lista, preferiblemente en combinacion con la lista generada con la funcion mezclar
la cantidad de caracateres de la variable

este mezclara la lista recibida y generara un alfanumerico aleatorio de la longitud de caracteres deseada"""
	global variable
	for i in range(longitud):
		random.shuffle(lista)
		variable = variable + str(random.choice(lista))
	return variable