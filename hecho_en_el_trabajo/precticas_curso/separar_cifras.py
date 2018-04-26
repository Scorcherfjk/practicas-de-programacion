############ descomponer un numero de 4 cifras ############
n = '1234'
if len(n) == 4:
	numero = int(n)
	if 0 < numero <= 9999:
		valor1 = n
		valor1 = valor1[::-1]
		for posicion, valor in enumerate(valor1):
			print("{:04d}".format(int(valor) * 10 ** posicion ))
	else:
		print("Error - Número es incorrecto")
else:
	print("Error - Introduce los argumentos correctamente")