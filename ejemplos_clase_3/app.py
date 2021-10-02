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

# Realizar HTTP POST con --> post.py

import traceback
from flask import Flask, request, jsonify, render_template, Response, redirect

# Crear el server Flask
app = Flask(__name__)

# Variable global para poner a prueba el método [GET]
# IMPORTANTE: Esta no es una buena forma de manejar datos,
# se debe usar base de dato (se verá en otro ejemplo más adelante)
base_de_datos = []

# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        # Imprimir los distintos endopoints disponibles
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Endpoints disponibles:</h2>"
        result += "<h3>[GET] /pulsaciones?limit=[]&offset=[] --> mostrar últimas pulsaciones registradas (limite and offset are optional)</h3>"
        result += "<h3>[GET] /pulsaciones/<name> --> mostrar el histórico de pulsaciones de una persona</h3>"
        result += "<h3>[POST] /registro --> ingresar nuevo registro de pulsaciones por JSON</h3>"
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
@app.route("/pulsaciones/<name>")
def pulsaciones_historico(name):
    try:
        # Obtener el historial de la persona
        datos_persona = {}
        for dato in base_de_datos:
            if dato["name"] == name:
                datos_persona = dato

        print("Dato solicitado para el nombre", name)
        print(datos_persona)

        # Transformar json a json string para enviar al HTML
        return jsonify(datos_persona)
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/registro
@app.route("/registro", methods=['POST'])
def registro():
    if request.method == 'POST':
        # Obtener del HTTP POST JSON el nombre y los pulsos
        nombre = str(request.form.get('name'))
        pulsos = str(request.form.get('heartrate'))

        datos_persona = {"name": nombre, "heartrate": pulsos}
        base_de_datos.append(datos_persona)
        print("Se agregó a la base de datos el siguiente registro:")
        print(datos_persona)
        return Response(status=200)

if __name__ == '__main__':
    print('Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000, debug=True)
