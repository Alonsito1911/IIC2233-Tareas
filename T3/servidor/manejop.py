import json

def cargar_datos(dato):
    with open('servidor/parametros.json') as contenido:
        datos = json.load(contenido)


        return  datos.get(dato)

