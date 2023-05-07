'''
Flask [Python]
Ejercicios de práctica

Autor: Inove Coding School
Version: 2.0
 
Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
las personas registradas.

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''

# Realizar HTTP POST con --> post.py

import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect

import utils
import persona

app = Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///personas.db"
# Asociamos nuestro controlador de la base de datos con la aplicacion
persona.db.init_app(app)


@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h2>Ejercicio Nº1:</h2>"
        result += "<h3>[GET] /personas?limit=[]&offset=[] --> mostrar el listado de personas (limite and offset are optional)</h3>"
        result += "<h2>Ejercicio Nº2:</h2>"
        result += "<h3>[POST] /registro --> ingresar una nueva persona por JSON, implementar la captura de los valores</h3>"
        result += "<h2>Ejercicio Nº3:</h2>"
        result += "<h3>[GET] /comparativa --> mostrar un gráfico con las edades de todas las personas"
        
        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


# ejercicio de practica Nº1
@app.route("/personas")
def personas():
    try:
        # Alumno:
        # Implementar la captura de limit y offset de los argumentos
        # de la URL
        # limit = ...
        # offset = ....

        # Debe verificar si el limit y offset son válidos cuando
        # no son especificados en la URL

        limit = 0
        offset = 0

        result = persona.report(limit=limit, offset=offset)
        return jsonify(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


# ejercicio de practica Nº2
@app.route("/registro", methods=['POST'])
def registro():
    if request.method == 'POST':
        try:
            name = ""
            age = 0
            # Alumno:
            # Obtener del HTTP POST JSON el nombre y los pulsos
            # name = ...
            # age = ...

            # Alumno: descomentar la linea persona.insert una vez implementado
            # lo anterior:
            # persona.insert(name, int(age))
            return Response(status=200)
        except:
            return jsonify({'trace': traceback.format_exc()})


# ejercicio de practica Nº3
@app.route("/comparativa")
def comparativa():
    try:
        # Alumno:
        # Implementar una función en persona.py llamada "dashboard"
        # Lo que desea es realizar un gráfico de linea con las edades
        # de todas las personas en la base de datos

        # Para eso, su función "dashboard" debe devolver dos valores:
        # - El primer valor que debe devolver es "x", que debe ser
        # los Ids de todas las personas en su base de datos
        # - El segundo valor que debe devolver es "y", que deben ser
        # todas las edades respectivas a los Ids que se encuentran en "x"

        # Descomentar luego de haber implementado su función en persona.py:

        # x, y = persona.dashboard()
        # image_html = utils.graficar(x, y)
        # return Response(image_html.getvalue(), mimetype='image/png')

        return "Alumno --> Realice la implementacion"
    except:
        return jsonify({'trace': traceback.format_exc()})


# Este método se ejecutará solo una vez
# la primera vez que ingresemos a un endpoint
@app.before_first_request
def before_first_request_func():
    # Crear aquí todas las bases de datos
    persona.db.create_all()
    print("Base de datos generada")


if __name__ == '__main__':
    print('Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
