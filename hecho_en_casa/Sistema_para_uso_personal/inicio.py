from sqlite3 import connect

#abrir la conexion
conexion = connect('almacen.db')

#creando el cursor
cursor = conexion.cursor()

#consulta
cursor.execute("SELECT cantidad, nombre, precios FROM productos WHERE cantidad > 0")
datos = cursor.fetchall()
print(datos)

#cerrar la conexion
conexion.close()