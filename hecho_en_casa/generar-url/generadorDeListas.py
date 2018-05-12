import pickle

ABC = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abc = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mayusculas = open('abecedarioMayusculas.pckl','wb')
pickle.dump(ABC,mayusculas)
mayusculas.close()

minusculas = open('abecedarioMinusculas.pckl','wb')
pickle.dump(abc,minusculas)
minusculas.close()

numeros = open('numeros.pckl','wb')
pickle.dump(num,numeros)
numeros.close()