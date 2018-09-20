from flask import Flask
from flask import request
from flask import render_template

from conexiones import leerString

app = Flask(__name__)


#Esta es la ruta del index
@app.route('/')
def index():
	lista = []
	for i in range(0,299):
		var = leerString("192.168.1.35",i,"Medida")
		if len(var) > 1:
			lista.append(var)
		else:
			break
	return render_template('plantilla2.html', lista=lista)

if __name__ == '__main__':
	app.run( debug=True, port=8000 )