"""
version 4
generar-url.py

genera un codigo aleatorio que al combinarse con la url estandar de youtube podria abrir el navegador en un video aleatorio

proximo a generar version 5 con funciones lambda
"""
import webbrowser
import random

constante = 'https://www.youtube.com/watch?v='
ABC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abc = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0,1,2,3,4,5,6,7,8,9]
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
	else:
		print("adios")
		break