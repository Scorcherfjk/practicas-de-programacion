from subprocess import run
from sqlite3 import connect

def res_long(datos):
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {} \t de {} \t de S/ {} cada uno, \t un total de S/ {:04.2f}".format(i[0],i[1],i[2],i[0]*i[2]))

def res_short(datos):
	if datos == []:
			print("no hay productos disponibles")
	else:
		for n,i in enumerate(datos):
			print("{}.- {} \t a S/ {} cada uno".format(n,i[0],i[1],))

def prod_disp(cursor):
	run("clear")
	datos = cursor.execute("SELECT cantidad, nombre, precio FROM productos WHERE cantidad > 0").fetchall()
	res_long(datos)

def prod_poca_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT cantidad, nombre, precio FROM productos WHERE cantidad BETWEEN 0.01 AND 3").fetchall()
	res_long(datos)

def prod_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT nombre, precio FROM productos WHERE cantidad = 0").fetchall()
	res_short(datos)


def prod_total(cursor):
	run("clear")
	datos = cursor.execute("SELECT nombre, precio FROM productos").fetchall()
	res_short(datos)