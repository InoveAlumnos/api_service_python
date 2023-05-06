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
from flask import Flask, request, jsonify, render_template, Response

# Crear el server Flask
app = Flask(__name__)

# Variable global para poner a prueba el método [GET]
# IMPORTANTE: Esta no es una buena forma de manejar datos,
# se debe usar una base de datos (se verá en otro ejemplo más adelante)
base_de_datos = [
    {
        "nombre": "Inove",
        "pulso": 80
    },
    {
        "nombre": "Python",
        "pulso": 65
    },
    {
        "nombre": "Max",
        "pulso": 110
    }
]

# ------------ Rutas o endpoints ----------------- #
# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h3>[GET] /pulsaciones?limit=[]&offset=[] --> mostrar últimas pulsaciones registradas (limite and offset are optional)</h3>"
        result += "<h3>[GET] /pulsaciones/[nombre] --> mostrar el histórico de pulsaciones de una persona</h3>"
        return(result)
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/pulsaciones
@app.route("/pulsaciones")
def pulsaciones():
    try:
        # Obtener de la query string los valores de limit y offset
        limit_str = str(request.args.get('limit'))
        offset_str = str(request.args.get('offset'))

        limit = len(base_de_datos)
        offset = 0

        if(limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)

        if(offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)

        # Obtener el reporte
        inicio = offset
        fin = offset + limit
        data = base_de_datos[inicio:fin]

        print("Dato solicitados")
        print(data)

        # Transformar json a json string para enviar al HTML
        return jsonify(data)
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/pulsaciones/<nombre>
@app.route("/pulsaciones/<nombre>")
def pulsaciones_historico(nombre):
    try:
        # Obtener el historial de la persona
        datos_persona = {}
        for dato in base_de_datos:
            if dato["nombre"] == nombre:
                datos_persona = dato

        print("Dato solicitado para el nombre", nombre)
        print(datos_persona)

        # Transformar json a json string para enviar al HTML
        return jsonify(datos_persona)
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    print('Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000, debug=True)
