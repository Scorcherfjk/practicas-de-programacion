#CRUD
from sqlite3 import connect
from inventario.operaciones_consulta import *

#añadir producto
def datos_prod():
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

def agregar_prod(cursor):
	valores, confirma = datos_prod()
	if confirma == 1:
		datos = cursor.execute("""
			INSERT INTO productos
			VALUES (null, ?, ?, ?, ? )
			""", valores).fetchall()
		print("\nfin del proceso")
	else:
		print("proceso cancelado")

#eliminar producto
def eliminar_prod(cursor):
	codigo = int( input( "introduzca el codigo del producto" ) )
	datos = cursor.execute("""
		DELETE FROM productos
		WHERE id = {}
		""".format(codigo)).fetchall()
