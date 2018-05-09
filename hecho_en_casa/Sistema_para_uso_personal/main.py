from inventario.menus import *
from sqlite3 import connect

if __name__ == '__main__':
	#abrir la conxion
	conexion = connect('almacen.db')
	cursor = conexion.cursor()

	#menu de consulta
	menu_general(cursor)

	#cerrando conexion
	del(cursor)
	conexion.commit()
	conexion.close()