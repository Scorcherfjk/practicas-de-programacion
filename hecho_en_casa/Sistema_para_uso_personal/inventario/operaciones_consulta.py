from subprocess import run
from sqlite3 import connect

def res_long(datos):
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {cantidad} \t de {nombre} \t de S/ {precio} cada {medida}, \t un total de S/ {total:04.2f}".format( cantidad=i[0], nombre=i[1], precio=i[2], total=i[0]*i[2], medida=i[3]))

def res_short(datos):
	if datos == []:
			print("no hay productos disponibles")
	else:
		print("id | nombre    |   precio  | medida      |")
		print("=========================================#")
		for i in datos:
			print("{codigo}.- {nombre} \t a S/ {precio} cada {medida} \t |".format(codigo=i[3], nombre=i[0], precio=i[1], medida=i[2] ))
		print("=========================================#")

def prod_disp(cursor):
	run("clear")
	datos = cursor.execute("SELECT productos.cantidad, productos.nombre, productos.precio, medidas.medida FROM productos INNER JOIN medidas ON(medidas.id = productos.tipo_medida) WHERE productos.cantidad > 0").fetchall()
	res_long(datos)

def prod_poca_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT productos.cantidad, productos.nombre, productos.precio, medidas.medida FROM productos INNER JOIN medidas ON(medidas.id = productos.tipo_medida) WHERE (medidas.medida = 'un' AND cantidad BETWEEN 1 AND 4) OR ((medidas.medida = 'kg' OR medidas.medida = 'lt') AND cantidad BETWEEN 0.01 AND 0.5)").fetchall()
	res_long(datos)

def prod_exis(cursor):
	run("clear")
	datos = cursor.execute("SELECT productos.nombre, productos.precio, medidas.medida, productos.id FROM productos INNER JOIN medidas ON(medidas.id = productos.tipo_medida) WHERE productos.cantidad = 0").fetchall()
	res_short(datos)


def prod_total(cursor):
	run("clear")
	datos = cursor.execute("SELECT productos.nombre, productos.precio, medidas.medida, productos.id FROM productos INNER JOIN medidas ON(medidas.id = productos.tipo_medida)").fetchall()
	res_short(datos)