from subprocess import run
from sqlite3 import connect

def prod_disp(cursor):
	run("clear")
	cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad > 0")
	datos = cursor.fetchall()
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {} de {} de {}/S cada uno, un total de {}/S".format(i[0],i[1],i[2],i[0]*i[2]))


def prod_poca_exis(cursor):
	run("clear")
	cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad BETWEEN 1 AND 3")
	datos = cursor.fetchall()
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {} de {} de {}/S cada uno, un total de {}/S".format(i[0],i[1],i[2],i[0]*i[2]))


def prod_exis(cursor):
	run("clear")
	cursor.execute("SELECT nombre, precios FROM productos WHERE cantidad = 0")
	datos = cursor.fetchall()
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("{} a {}/S cada uno".format(i[0],i[1]))


def prod_total(cursor):
		run("clear")
		cursor.execute("SELECT nombre, precios FROM productos")
		datos = cursor.fetchall()
		if datos == []:
			print("no hay productos disponibles")
		else:
			for i in datos:
				print("{} a {}/S cada uno".format(i[0],i[1],))