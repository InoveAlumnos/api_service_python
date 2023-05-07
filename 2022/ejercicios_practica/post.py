'''
API Post [Python]
---------------------------
Autor: Inove Coding School
Version: 1.0
 
Descripcion:
Se utiliza request para generar un HTTP post al servidor Flask
'''

__author__ = "Inove Coding School"
__email__ = "INFO@INOVE.COM.AR"
__version__ = "1.0"

import requests

endpoint = 'registro'

url = f'http://127.0.0.1:5000/{endpoint}'

if __name__ == "__main__":
    try:
        name = str(input('Ingrese el nombre de la persona:'))
        age = int(input('Ingrese la edad:'))
        post_data = {"name": name, "age": age}        
        x = requests.post(url, data = post_data)
        print('POST enviado a:',url)
        print('Datos:')
        print(post_data)
    except:
        print('Error, POST no efectuado')
