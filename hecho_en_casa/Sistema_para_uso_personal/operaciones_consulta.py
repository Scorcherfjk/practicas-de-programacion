from subprocess import run
from sqlite3 import connect


def res_long(datos):
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {} de {} de {}/S cada uno, un total de {}/S".format(i[0],i[1],i[2],i[0]*i[2]))

def res_short(datos):
	if datos == []:
			print("no hay productos disponibles")
	else:
		for i in datos:
			print("{} a {}/S cada uno".format(i[0],i[1],))

def prod_disp(cursor):
	run("clear")
	datos = cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad > 0").fetchall()
	res_long(datos)

def prod_poca_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad BETWEEN 1 AND 3").fetchall()
	res_long(datos)

def prod_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT nombre, precios FROM productos WHERE cantidad = 0").fetchall()
	res_short(datos)


def prod_total(cursor):
	run("clear")
	datos = cursor.execute("SELECT nombre, precios FROM productos").fetchall()
	res_short(datos)

