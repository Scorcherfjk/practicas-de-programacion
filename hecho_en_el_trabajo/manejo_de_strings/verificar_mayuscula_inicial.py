# Metodo de otros lenguajes 
def otros(cadena):
	letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in letras:
		if i == cadena[0]:
			valor = True
			break
		else:
			valor = False
	if valor:
		print("La cadena inicia con mayusculas")
	else:
		print("La cadena NO inicia con mayusculas")

# Metodo de Python
def propio(cadena):
	if cadena is not cadena.capitalize():
		print("La cadena inicia con mayusculas")
	else:
		print("La cadena NO inicia con mayusculas")


cadena = "Hola mundo"
otros(cadena)
propio(cadena)
