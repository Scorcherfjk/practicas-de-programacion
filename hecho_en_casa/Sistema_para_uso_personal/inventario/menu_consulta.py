from subprocess import run
from inventario.operaciones_consulta import *

#menu
def menu_consulta(cursor):
	opcion = None
	while True:
		try:
			try:
				run("clear")
			except:
				pass
			opcion = int(input("""\nSeleccione la opcion requerida

1) productos disponibles
2) productos con poca existencia
3) productos sin existencia
4) todos los productos
5) salir
"""))
		except ValueError:
			run("clear")
			print("ingrese un valor valido")
		if opcion == 1:
			prod_disp(cursor)
		elif opcion == 2:
			prod_poca_exis(cursor)
		elif opcion == 3:
			prod_exis(cursor)
		elif opcion == 4:
			prod_total(cursor)
		elif opcion == 5:
			run("clear")
			print("\nadios!")
			break
		else:
			print("\nIntentelo de nuevo")