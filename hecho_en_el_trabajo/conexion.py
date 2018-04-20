import datetime, pytz, locale
locale.setlocale(locale.LC_ALL, 'es-ES')
dt = datetime.datetime.now(pytz.timezone('America/Caracas'))

def conexion(direccion, puerto):
	"""realiza una conexion Telnet a un host y un puerto especifico. recibiendo solo 2 parametros para ello.
	
	Manejando errores:
		si el puerto no esta disponible o no puede acceder a este.

	Recibiendo argumentos externos:
		argumento 1 = la direccion IP
		argumento 2 = el puerto

	Condicionado:
		solo deben pasarse 2 argumentos, sino mostrara el uso correcto del script.
	
	Documentacion
		Generando al final un log de resultados de transaccion"""

	from telnetlib import Telnet
	from io import open
	log = open('conexion_telnet.log','a+')
	try:
		with Telnet(direccion, puerto) as tn:
			tn.close()
			mensaje = dt.strftime("[%d/%m/%Y - %H:%M:%S] se ha conectado correctamente")
			print(mensaje)
	except ConnectionRefusedError:
		mensaje = dt.strftime("[%d/%m/%Y - %H:%M:%S] no ha logrado conectarse")
		print(mensaje)
	except TimeoutError:
		mensaje = dt.strftime("[%d/%m/%Y - %H:%M:%S] no ha logrado conectarse, posiblemente se encuentre apagado")
		print(mensaje)

	mensaje = mensaje + " al host {} por el puerto {}\n".format(direccion,puerto)
	log.write(mensaje)
	log.close()