"""
version 5
generar-url.py

genera un codigo aleatorio que al combinarse con la url estandar de youtube podria abrir el navegador en un video aleatorio

combinando:
	modulos:
		random
		webbrowser
	funciones:
		mezclar
		codigo
	compresion de listas
	entradas de texto
	condiciones
	bucles

"""
import webbrowser
import random

constante = 'https://www.youtube.com/watch?v='
ABC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abc = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [i for i in range(10)]
variable = ''
mix = []

def mezclar(listaFuente,listaDestino):
	for i in listaFuente:
		listaDestino.append(i)
		random.shuffle(listaDestino)

def codigo(lista,variable):
	for i in range(11):
		random.shuffle(lista)
		variable = variable + str(random.choice(lista))
	return variable

mezclar(ABC,mix)
mezclar(abc,mix)
mezclar(num,mix)
variable = codigo(mix,variable)

print(variable)

url = constante + variable

while True:
	opcion = input("desea abrir la url generada en el Browser? (y,n)")
	if opcion == "y":
		webbrowser.open_new_tab(url)
	elif opcion == "n":
		print("adios")
		break
	else:
		print("intentalo de nuevo")