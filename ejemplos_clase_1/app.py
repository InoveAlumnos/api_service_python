'''
Flask [Python]
Ejemplos de clase

Autor: Inove Coding School
Version: 2.0

Descripcion:
Se utiliza Flask para crear un WebServer que levanta los datos de
las personas que registran su ritmo cardíaco.

Ingresar a la siguiente URL para ver los endpoints disponibles
http://127.0.0.1:5000/
'''

import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect

# Crear el server Flask
app = Flask(__name__)

# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    # Siempre es recomendable colocar nuestro
    # código entre try except para que el servidor
    # no se caiga si llega a fallar algo
    try:
        return "Hola mundo desde Flask!"
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    print('Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
