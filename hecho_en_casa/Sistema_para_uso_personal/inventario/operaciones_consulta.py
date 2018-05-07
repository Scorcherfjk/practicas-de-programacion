from subprocess import run
from sqlite3 import connect

def res_long(datos):
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {cantidad} \t de {nombre} \t de S/ {precio} cada {tipo_medida}, \t un total de S/ {total:04.2f}".format( cantidad=i[0], nombre=i[1], precio=i[2], total=i[0]*i[2], tipo_medida=i[3]))

def res_short(datos):
	if datos == []:
			print("no hay productos disponibles")
	else:
		for n,i in enumerate(datos):
			print("{contador}.- {nombre} \t a S/ {precio} cada {tipo_medida}".format(contador=n, nombre=i[0], precio=i[1], tipo_medida=i[2] ))

def prod_disp(cursor):
	run("clear")
	datos = cursor.execute("SELECT cantidad, nombre, precio, tipo_medida FROM productos WHERE cantidad > 0").fetchall()
	res_long(datos)

def prod_poca_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT cantidad, nombre, precio, tipo_medida FROM productos WHERE tipo_medida = 'un' AND cantidad BETWEEN 0.01 AND 3").fetchall()
	res_long(datos)

def prod_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT nombre, precio, tipo_medida FROM productos WHERE cantidad = 0").fetchall()
	res_short(datos)


def prod_total(cursor):
	run("clear")
	datos = cursor.execute("SELECT nombre, precio, tipo_medida FROM productos").fetchall()
	res_short(datos)