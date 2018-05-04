from inventario.menu_consulta import *
from subprocess import run
from sqlite3 import connect

#abrir la conxion
conexion = connect('almacen.db')
cursor = conexion.cursor()

#menu de consulta
menu_consulta(cursor)


del(cursor)
conexion.close()