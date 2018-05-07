#CRUD
from sqlite3 import connect

#abrir la conexion
conexion = connect('almacen.db')
cursor = conexion.cursor()

#añadir producto
def agregar_prod(cursor):
	nombre = input( "introduzca el nombre del producto" )
	precio = float( input( "introduzca el precio del producto" ) )
	cantidad = int( input( "introduzca la cantidad de productos" ) )
	tipo_medida = int( input( """introduzca el tipo de medida del producto
1) kg
2) lt
3) unidad
""" ) )

	confirma = int( input( """confirma los cambios
se a#adira {cantidad} {medida} de {nombre} a S/{precio} cada {medida}

1) confirmar
2) cancelar
""".format(
	cantidad=cantidad,
	medida=tipo_medida,
	nombre=nombre,
	precio=precio) ) )
	datos = cursor.execute("""
		INSERT (nombre, precio, cantidad, tipo_medida)   
		INTO productos
		VALUES ( ?, ?, ?, ? )
		""", nombre, precio, cantidad, tipo_medida ).fetchall()

#modificar producto
def modificar_prod(cursor):
codigo = int( input( "introduzca el codigo del producto" ) )
datos = cursor.execute("""
		UPDATE FROM productos
		WHERE id = ?
		""", codigo).fetchall()
		print("se fue!")


#eliminar producto
def eliminar_prod(cursor):
codigo = int( input( "introduzca el codigo del producto" ) )
datos = cursor.execute("""
		DELETE FROM productos
		WHERE id = {}
		""".format(codigo)).fetchall()

#cerrando conexion
del(cursor)
conexion.close()
