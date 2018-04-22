"""Generador de URL's aleatorias de Youtube ;)
version 6
generar-url.py

genera un codigo aleatorio que al combinarse con la url estandar de youtube podria abrir el navegador en un video aleatorio

combinando:
	modulos:
		pickle
		random
		webbrowser
		funciones propias importadas
	funciones:
		mezclar
		codigo
	compresion de listas
	manejo de archivos
	archivos que almacenan listas
	entradas de texto
	condiciones
	bucles

"""
import webbrowser, pickle
from io import open
from FuncionesConRandom import *

mayusculas = open('abecedarioMayusculas.pckl','rb')
minusculas = open('abecedarioMinusculas.pckl','rb')

constante = 'https://www.youtube.com/watch?v='
ABC = pickle.load(mayusculas)
abc = pickle.load(minusculas)
num = [i for i in range(10)]
variable = ''
mix = []

mezclar(ABC,mix)
mezclar(abc,mix)
mezclar(num,mix)
variable = codigo(mix,variable,11)

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


mayusculas.close()
minusculas.close()