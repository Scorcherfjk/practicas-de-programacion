from inventario.menu_consulta import *
from subprocess import run
from sqlite3 import connect

if __name__ == '__main__':
	#abrir la conxion
	conexion = connect('almacen.db')
	cursor = conexion.cursor()

	#menu de consulta
	menu_consulta(cursor)

	#cerrando conexion
	del(cursor)
	conexion.close()
