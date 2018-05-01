from subprocess import run
from sqlite3 import connect
from operaciones_consulta import *

run("clear")
opcion = None

#abrir la conexion
conexion = connect('almacen.db')
cursor = conexion.cursor()

#menu
print("BINEVENIDO AL SISTEMA DE CONTROL DE INVENTARIO")
while True:
	try:
		opcion = int(input("""\nSeleccione la opcion requerida

1) productos disponibles
2) productos con poca existencia
3) productos sin existencia
4) todos los productos
5) salir
"""))
	except ValueError:
		run("clear")
		print("ingrese un valor valido")
	if opcion == 1:
		prod_disp(cursor)
	if opcion == 2:
		prod_poca_exis(cursor)
	if opcion == 3:
		prod_exis(cursor)
	if opcion == 4:
		prod_total(cursor)
	if opcion == 5:
		print("\nadios!")
		break
	else:
		print("\nIntentelo de nuevo")

#cerrar la conexion
del(cursor)
conexion.close()