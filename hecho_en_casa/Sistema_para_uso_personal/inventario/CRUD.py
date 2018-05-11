"""CRUD"""

from sqlite3 import connect
from inventario.operaciones_consulta import *
from inventario.menus import *

# recolectar los datos del nuevo producto
def datos_prod():
	while True:
		try:
			nombre = input( "introduzca el nombre del producto: \t" )
			precio = float( input( "introduzca el precio del producto: \t") )
			cantidad = float( input( "introduzca la cantidad de productos: \t" ) )
			tipo_medida = int( input( """introduzca el tipo de medida del producto
1) kg
2) lt
3) unidad
""" ) )
			if tipo_medida == 1:
				medida= "kg"
			elif tipo_medida == 2:
				medida= "lt"
			elif tipo_medida == 3:
				medida= "unidad"
		except:
			print("\nha ingresado un valor incorrecto, intentelo de nuevo\n")
			continue
	
		confirma = int( 
			input( """confirma los cambios
se a#adira {cantidad} {medida} de {nombre} a S/{precio} cada {medida}

1) confirmar
2) cancelar
""".format(
	cantidad=cantidad,
	medida=medida,
	nombre=nombre,
	precio=precio
			) 
				) 
					)
		valores = [nombre, precio, cantidad, tipo_medida]
		return valores, confirma


# selecciona un producto de acuerdo a su identificador y pide verificacion
def seleccion_prod(cursor):
	while True:
		codigo = []
		try:
			cd = int(input( "introduzca el codigo del producto: \t" ))
			codigo.append(cd)
			datos = cursor.execute("""
				SELECT productos.nombre, productos.precio, medidas.medida, productos.id 
				FROM productos 
				INNER JOIN medidas 
				ON(medidas.id = productos.tipo_medida) 
				WHERE (productos.id = ?)""", 
				codigo).fetchall()
			if datos == []:
				raise ValueError
		except:
			print("\nha seleccionado un registro inexistente, intentelo de nuevo\n")
			continue

		res_short(datos)
		confirmacion = int( 
		input( """desea modificar el registro encontrado

1) confirmar
2) intentar de nuevo
3) volver al menu anterior
"""))
		if confirmacion == 1:
			return codigo
		if confirmacion == 3:
			codigo = None
			return codigo

# agrega un producto nuevo
def agregar_prod(cursor):
	valores, confirma = datos_prod()
	if confirma == 1:
		datos = cursor.execute("""
			INSERT INTO productos
			VALUES (null, ?, ?, ?, ? )""", 
			valores).fetchall()
		print("\nProducto anadido satisfactoriamente")
	else:
		print("proceso cancelado")

#modificar producto
def modificar_prod(cursor):
	
	codigo = seleccion_prod(cursor)
	if codigo != None:
		
		valores, confirma = datos_prod()
		final = valores + codigo
		
		if confirma == 1:
			datos = cursor.execute("""
				UPDATE productos
				SET nombre = ?, precio = ?, cantidad = ?, tipo_medida = ?
				WHERE id = ?""", 
				final)
			print("\nProducto modificado satisfactoriamente")
		else:
			print("proceso cancelado")

#eliminar producto
def eliminar_prod(cursor):
	
	codigo = seleccion_prod(cursor)
	if codigo != None:
		datos = cursor.execute("""
			DELETE FROM productos
			WHERE id = ?
			""", codigo)

		print("\nProducto eliminado satisfactoriamente")