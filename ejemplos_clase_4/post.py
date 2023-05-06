'''
API Post [Python]
---------------------------
Autor: Inove Coding School
Version: 2.0
 
Descripcion:
Se utiliza request para generar un HTTP post al servidor Flask
'''

import requests

url = f'http://127.0.0.1:5000/registro'

if __name__ == "__main__":
    try:
        nombre = str(input('Ingrese el nombre de la persona:'))
        pulso = int(input('Ingrese el ritmo cardiago:'))
        post_data = {"nombre": nombre, "pulso": pulso}        
        x = requests.post(url, data = post_data)
        print('POST enviado a:',url)
        print('Datos:')
        print(post_data)
    except:
        print('Error, POST no efectuado')