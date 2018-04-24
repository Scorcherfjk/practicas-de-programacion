from signal import signal, SIGINT

def ctrl_c (signum, rfm):
	print("no puedes cerrar el programa presionando CTRL+C")

print("instalando virus...")
signal(SIGINT, ctrl_c)

while True:
	pass

print("Software instalado!")