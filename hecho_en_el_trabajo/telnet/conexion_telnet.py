"""Verificador de disponibilidad de puertos por Telnet 

Uso Correcto

	python conexion_telnet.py direccionIP puerto

	"""
from sys import argv
from conexion import conexion

if __name__=="__main__":
	if 4 > len(argv) > 2:
		conexion(argv[1],argv[2])
	else:
		print("""Ingrese los datos correctamente

	python conexion_telnet.py direccionIP puerto""")