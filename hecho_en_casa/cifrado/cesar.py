ABC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
		'H', 'I', 'J', 'K', 'L', 'M', 'N', 
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
		'V', 'W', 'X', 'Y', 'Z']

abc = [ 'a', 'b', 'c', 'd', 'e', 'f', 
		'g', 'h', 'i', 'j', 'k', 'l', 
		'm', 'n', 'o', 'p', 'q', 'r', 
		's', 't', 'u', 'v', 'w', 'x', 
		'y', 'z']

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# cadena = input("introduce una cadena de texto:\n")
#d = int( input("introduce el dezplazamiento:\n") )

d = 2

for may in ABC:
	for n, minu in enumerate(abc):
		if may.lower() == minu:
			try:
				print(may, "-", abc[n+d])
			except:
				pass




