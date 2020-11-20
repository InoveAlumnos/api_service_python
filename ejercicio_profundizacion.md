# Ejercicios de profundización [Python]
EL propósito de este ejercicio es que el alumno ponga sus habilidades JSON, matplotlib, bases de datos, request API JSON y Rest API.

# Enunciado
El objetivo es realizar un ejercicio muy similar al realizado en el pasado con la API de jsonplaceholder. Deberan consumir toda la información que retorna el request de la API y almacenarla en una db.

url = https://jsonplaceholder.typicode.com/todos

Deberá generar una base de datos SQL o NoSQL (queda a su elección) que posea los siguientes campos:
- userId --> [número] id del usuario
- id --> [número] id de la consulta (no es necesario que sea el "_id" de Mongo)
- title --> [texto] nombre del título
- completed --> [bool] completado o no el título

Luego la información relativa

## clear()
Deben crear una función "clear" la cual borre todos los campos existentes en la DB, esto les permitirá realizar cada prueba desde cero.

## fill()
Deben crear una función "fill" que lea los datos provenientes del JSON request y complete la base de datos. Si se fijan los datos que retorna el JSON en el request son exactamente los mismos que se solicitan en el ejercicio, por lo que pueden insertar el JSON tal cual les llega de la API en la base de datos (todos juntos o uno por uno)

## title_completed_count(userId)
Deben crear una función que lea la DB (find) y cuente (count) cuantos usuarios con "userId" han completado sus títulos. Para esto sentencia "find" de Mongo deberá tener dos campos condicionales (userId y completed) y utilizar el método count para contar los casos favorables.

## Esquema del ejercicio
Deben crear su archivo de python "app.py" y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa. El programa antes de lanzar el server Flask debe crear y completar la base de datos para ser utilizada luego por la API.
```
if __name__ == "__main__":
  # Borrar DB
  clear()

  # Completar la DB con el JSON request
  fill()

  # Lanzar server Flask
  app.run()

```

# API

## Endpoints
__[GET] /user/{id}/titles__
- Esta ruta es la encargada a informar al solicitante cuantos titulos completó el usuario cuyo id es el pasado como parámetro en la URL estática. Deben imprimir en el HTML cuantos títulos completó ese usuario.\
NOTA: Utilice "title_completed_count" para obtener la información necesaria.

__[GET] /user/graph__
- Esta ruta es la encargada a informar el reporte y comparativa de cuantos títulos completó cada usuario en un gráfico. Debe obtener la información de todos los usuarios (la cantidad de títulos que completó cada uno) para armar el gráfico que usted crea mejor que resuelve el reporte solicitado.
NOTA: Puede Utilizar "title_completed_count" para obtener la información necesaria o crear una nueva función.

__[GET] /user/table__
- Esta ruta es la encargada a informar cuantos títulos completó cada usuario en una tabla HTML o JSON (queda a su criterio). Debe recolectar la misma información solicitada en el anterior punto pero cambiar la estrategía de visualización.



