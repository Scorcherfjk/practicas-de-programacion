from subprocess import run
from inventario.operaciones_consulta import *
from inventario.CRUD import *

#menu de consultas
def menu_consulta(cursor):

	while True:
		try:
			run("clear")
			opcion = int(input("""\nSeleccione la opcion requerida

1) productos disponibles
2) productos con poca existencia
3) productos sin existencia
4) todos los productos
0) salir
"""))

		except:
			run("clear")
			print("ingrese un valor valido")
			continue

		if opcion == 1:
			prod_disp(cursor)
		elif opcion == 2:
			prod_poca_exis(cursor)
		elif opcion == 3:
			prod_exis(cursor)
		elif opcion == 4:
			prod_total(cursor)
		elif opcion == 0:
			run("clear")
			break
		else:
			print("\nIntentelo de nuevo")


# menu de modificaciones
def menu_crud(cursor):

	while True:
		try:
			run("clear")
			opcion = int(input("""\nSeleccione la opcion requerida

1) agregar producto
2) modificar producto existente
3) eliminar producto
0) salir
"""))

		except:
			run("clear")
			print("ingrese un valor valido")
			continue

		if opcion == 1:
			agregar_prod(cursor)
		elif opcion == 2:
			modificar_prod(cursor)
		elif opcion == 3:
			eliminar_prod(cursor)
		elif opcion == 0:
			run("clear")
			break
		else:
			print("\nIntentelo de nuevo")


def menu_general(cursor):

	while True:
		try:
			run("clear")
			opcion = int(input("""\nSeleccione la opcion requerida

1) consultas
2) modificaciones
0) salir
"""))

		except:
			run("clear")
			print("ingrese un valor valido")
			continue

		if opcion == 1:
			menu_consulta(cursor)
		elif opcion == 2:
			menu_crud(cursor)
		elif opcion == 0:
			run("clear")
			print("\nadios!")
			break
		else:
			print("\nIntentelo de nuevo")