#importamos Flask al archivo Python
from flask import Flask
#importamos el modulo para recibir parametros
from flask import request
#importamos el modulo para trabajar con una plantilla html
from flask import render_template

#Instanciar un objeto de tipo Flask
app = Flask(__name__)

#para cambiarle la carpeta por default de busqueda de las plantillas se le asigna este parametro
#app = Flask(__name__, template_folder = "plantillas")


#Esta es la ruta del index
@app.route('/')
def index():
    return "Hola Mundo!"


#Esta es una ruta definida
@app.route('/saluda')
def saluda():
    return "Que lo Que Menor!"


#esta ruta recibe un parametro seguido del simbolo ? 
@app.route('/parametro')
def parametro():
	nombre = request.args.get('nombre', "no tiene ningun parametro")
	return "Que lo Que {}!".format(nombre)


#esta ruta recibe parametros entre los / de la url
#funciona si no se le pasa ningun parametro
@app.route('/nombre/')
#funciona si se le pasa solo un parametro
@app.route('/nombre/<nombre>')
#funciona completamente
@app.route('/nombre/<nombre>/<apellido>')
def nombre(nombre = "", apellido = ""):
	return "Que lo Que {} {}!".format(nombre,apellido)


#Llamando a una plantilla en html en la carpeta "templates"
@app.route('/plantilla')
def plantilla():
    return render_template('plantilla.html')


@app.route('/variables')
@app.route('/variables/<nombre_prueba>')
def variable(nombre_prueba=''):
	edad_persona = 21
	lista_prueba = [1,2,3,4,5,6,7,8,9,0]
	return render_template('plantilla2.html', nombre=nombre_prueba, edad=edad_persona, lista=lista_prueba)


#validacion que se ejecute desde este archivo
if __name__ == '__main__':
	#Se inicia el servidor
	app.run( debug=True, port=8000 )