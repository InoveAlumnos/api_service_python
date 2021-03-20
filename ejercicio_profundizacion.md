# Ejercicios de profundización [Python]
EL propósito de este ejercicio es que el alumno ponga sus habilidades JSON, matplotlib, bases de datos, request API JSON y Rest API.

# Enunciado
El objetivo es realizar un ejercicio muy similar al realizado en el pasado con la API de jsonplaceholder. Deberan consumir toda la información que retorna el request de la API y almacenarla en una db.

url = https://jsonplaceholder.typicode.com/todos

Deberá generar una base de datos SQL que posea los siguientes campos:
- id --> [número] id de la consulta
- userId --> [número] id del usuario
- title --> [texto] nombre del título
- completed --> [bool] completado o no el título

Luego la información relativa

## clear()
Deben crear una función "clear" la cual borre todos los campos existentes en la DB, esto les permitirá realizar cada prueba desde cero.

## fill()
Deben crear una función "fill" que lea los datos provenientes del JSON request y complete la base de datos. Si se fijan los datos que retorna el JSON en el request son exactamente los mismos que se solicitan en el ejercicio, por lo que pueden utilizar los campos como lo leen de la consulta e insertarlos en su DB.

## title_completed_count(userId)
Deben crear una función que lea la DB y cuente (count) cuantos usuarios con "userId" han completado sus títulos. Para esta query deberá tener dos campos condicionales en su "filter" (userId y completed) y utilizar el método count para contar los casos favorables.

## Esquema del ejercicio
Deben crear su archivo de python "app.py" y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí lanzar el server Flask. Deberán crear y completar la base de datos para ser utilizar invocar a los endpoints que explorarán los datos, para eso antes de comenzar deben crear el endopint "reset" tal como se vi en clase, en dicho endopint deben llamar a "clear" y "fill"
```
# Ruta que se ingresa por la ULR 127.0.0.1:5000/reset
@app.route("/reset")
def reset():
    try:
        # Borrar y crear la base de datos
        usuarios.clear()
        usuarios.fill()
        result = "<h3>Base de datos re-generada!</h3>"
        return (result)
    except:
        return jsonify({'trace': traceback.format_exc()})
```

# API

## Endpoints
__[GET] /user/{id}/titles__
- Esta ruta es la encargada a informar al solicitante cuantos titulos completó el usuario cuyo id es el pasado como parámetro en la URL estática. Deben imprimir en el HTML cuantos títulos completó ese usuario.\
NOTA: Utilice "title_completed_count" para obtener la información necesaria.

__[GET] /user/graph__
- Esta ruta es la encargada a informar el reporte y comparativa de cuantos títulos completó cada usuario en un gráfico. Debe obtener la información de todos los usuarios (la cantidad de títulos que completó cada uno) para armar el gráfico que usted crea mejor que resuelve el reporte solicitado.
NOTA: Pueden recorrer toda la base de datos y contar cuantos títulos completó cada uno.

__[GET] /user/titles__
- Esta ruta es la encargada a informar cuantos títulos completó cada usuario en un JSON (queda a su criterio). Debe recolectar la misma información solicitada en el anterior punto pero cambiar la estrategía de visualización.



