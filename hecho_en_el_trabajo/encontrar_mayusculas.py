def mayusculas(cadena):
	letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	coincidencias = ''
	for x in cadena:
		for y in letras: 
			if x == y:
				coincidencias = coincidencias + x
	return coincidencias

cadena = input("Introduce una cadena de texto")
print("Se han encontrado {} mayusculas y estas fueron las letras {}.".format(len(mayusculas(cadena)),mayusculas(cadena)))
