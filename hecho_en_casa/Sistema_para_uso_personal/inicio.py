import sqlite3

#abrir la conexion
conexion = sqlite3.connect('almacen.db')



#cerrar la conexion
conexion.close()