#!/usr/bin/env python
'''
Heart DB manager
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para administrar la base de datos de registro de personas
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import os
import sqlite3

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func

from config import config
# Obtener la path de ejecución actual del script
script_path = os.path.dirname(os.path.realpath(__file__))

# Obtener los parámetros del archivo de configuración
config_path_name = os.path.join(script_path, 'config.ini')
db = config('db', config_path_name)

base = declarative_base()
# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine(f"sqlite:///{db['database']}")

class Persona(base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    nationality = Column(String)
    
    def __repr__(self):
        return f"Persona:{self.name} con nacionalidad {self.nacionalidad}"


def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos
    base.metadata.drop_all(engine)

    # Crear las tablas
    base.metadata.create_all(engine)


def insert(name, age, nationality):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear una nueva persona
    person = Persona(name=name, age=age, nationality=nationality)

    # Agregar la persona a la DB
    session.add(person)
    session.commit()


def report(limit=0, offset=0):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener todas las personas
    query = session.query(Persona)
    if limit > 0:
        query = query.limit(limit)
        if offset > 0:
            query = query.offset(offset)

    json_result_list = []

    # De los resultados obtenidos pasar a un diccionario
    # que luego será enviado como JSON
    # TIP --> la clase Persona podría tener una función
    # para pasar a JSON/diccionario
    for person in query:
        json_result = {'name': person.name, 'age': person.age, 'nationality': person.nationality}
        json_result_list.append(json_result)

    return json_result_list
