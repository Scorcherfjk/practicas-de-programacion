from subprocess import run
from sqlite3 import connect

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
		run("clear")
		#consulta
		cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad > 0")
		datos = cursor.fetchall()
		if datos == []:
			print("no hay productos disponibles")
			continue
		else:
			for i in datos:
				print("hay {} de {} de {}/S cada uno, un total de {}/S".format(i[0],i[1],i[2],i[0]*i[2]))
				continue
	if opcion == 2:
		run("clear")
		#consulta
		cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad BETWEEN 1 AND 3")
		datos = cursor.fetchall()
		if datos == []:
			print("no hay productos disponibles")
			continue
		else:
			for i in datos:
				print("hay {} de {} de {}/S cada uno, un total de {}/S".format(i[0],i[1],i[2],i[0]*i[2]))
				continue
	if opcion == 3:
		run("clear")
		#consulta
		cursor.execute("SELECT nombre, precios FROM productos WHERE cantidad = 0")
		datos = cursor.fetchall()
		if datos == []:
			print("no hay productos disponibles")
			continue
		else:
			for i in datos:
				print("{} a {}/S cada uno".format(i[0],i[1]))
				continue
	if opcion == 4:
		run("clear")
		#consulta
		cursor.execute("SELECT nombre, precios FROM productos")
		datos = cursor.fetchall()
		if datos == []:
			print("no hay productos disponibles")
			continue
		else:
			for i in datos:
				print("{} a {}/S cada uno".format(i[0],i[1],))
				continue
	if opcion == 5:
		print("\nadios!")
		break
	else:
		print("\nIntentelo de nuevo")

#cerrar la conexion
del(cursor)
conexion.close()