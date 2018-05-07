from sqlite3 import connect

#abrir la conexion
conexion = connect('almacen.db')

#creando el cursor
cursor = conexion.cursor()

def res_long(datos):
	if datos == []:
		print("no hay productos disponibles")
	else:
		for i in datos:
			print("hay {cantidad} \t de {nombre} \t de S/ {precio} cada {medida}, \t un total de S/ {total:04.2f}".format( 
				cantidad=i[0], 
				nombre=i[1], 
				precio=i[2], 
				total=float(i[0])*float(i[2]), 
				medida=i[3]))

#consulta
def prod_disp(cursor):
	consulta = """SELECT productos.cantidad, productos.nombre, productos.precio, medidas.medida 
	FROM productos 
	INNER JOIN medidas 
	ON(medidas.id = productos.tipo_medida) 
	WHERE (medidas.medida = 'un' AND cantidad BETWEEN 1 AND 4) 
	OR ((medidas.medida = 'kg' OR medidas.medida = 'lt') 
	AND cantidad BETWEEN 0.01 AND 0.5) 
	"""

	datos = cursor.execute(consulta).fetchall()
	res_long(datos)
	print(datos)

prod_disp(cursor)

#cerrar la conexion
conexion.close()