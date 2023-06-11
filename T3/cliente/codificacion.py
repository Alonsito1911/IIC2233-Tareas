import json
from manejop import cargar_datos
diccionari = {'0': {'elemento': 'fuego', 'color': 'azul', 'puntos': '5'}, '1': {'elemento': 'nieve', 'color': 'verde', 'puntos': '4'}, '2': {'elemento': 'nieve', 'color': 'verde', 'puntos': '3'}, '3': {'elemento': 'agua', 'color': 'azul', 'puntos': '1'}, '4': {'elemento': 'nieve', 'color': 'azul', 'puntos': '5'}, '5': {'elemento': 'nieve', 'color': 'verde', 'puntos': '1'}, '6': {'elemento': 'agua', 'color': 'verde', 'puntos': '5'}, '7': {'elemento': 'nieve', 'color': 'rojo', 'puntos': '5'}, '8': {'elemento': 'agua', 'color': 'azul', 'puntos': '2'}, '9': {'elemento': 'nieve', 'color': 'azul', 'puntos': '5'}, '10': {'elemento': 'nieve', 'color': 'rojo', 'puntos': '5'}, '11': {'elemento': 'agua', 'color': 'rojo', 'puntos': '1'}, '12': {'elemento': 'fuego', 'color': 'azul', 'puntos': '2'}, '13': {'elemento': 'nieve', 'color': 'azul', 'puntos': '1'}, '14': {'elemento': 'agua', 'color': 'rojo', 'puntos': '3'}}
def codificar(value):
    dic_ = json.dumps(value)
    print(f"desde usuario estamos enviando {dic_}")
    msg_bytes = dic_.encode()

    msg_length = len(msg_bytes).to_bytes(4, byteorder='big')

    response_length = int.from_bytes(
        msg_length, byteorder='big')

    msg_final = msg_length


    TAMANO_CHUNK = 32
    contador = 0
    for i in range(0, len(msg_bytes), TAMANO_CHUNK):
        contador += 1

        numero_bloque = bytearray()
        numero_bloque.append(contador)
        #xd
        for k in range(3):
            numero_bloque.append(0)
        msg_final += numero_bloque[0:]

        # Aqui obtenemos nuestro chunk
        chunk = bytearray(msg_bytes[i:i + TAMANO_CHUNK])

        if len(chunk) != 32:

            bytes_agregar = 32 - len(chunk)

            for b in range(bytes_agregar):
                chunk.append(0)
        msg_final += chunk[0:]


    return msg_final

def decodificar(response_length, response_bytes):

    TAMANO_CHUNK = 36

    response = bytearray()


    contador = 0
    while len(response) < response_length:

        # print(f"bytes a leer {response_bytes}")

        # read_length = min(4096, response_length - len(response))
        # print(read_length)
        cantidad_de_chunks = response_length // 32
        # cantidad de bytes importantes del ultimo chunk
        bytes_ultimo_chunk = response_length % 32
        # print(f"bytes {bytes_ultimo_chunk}")
        for i in range(0, len(response_bytes), TAMANO_CHUNK):
            # print(f"i: {i}")
            contador += 1
            # print(contador)
            # Aqui obtenemos nuestro chunk
            chunk = bytearray(response_bytes[i:i + TAMANO_CHUNK])

            # print(chunk)
            if contador <= cantidad_de_chunks:
                # print(f"parte 1")
                # print(chunk)
                response.extend(chunk[4:])
                # print(response, len(response))
            else:
                # print(f"parte 2")

                response.extend(chunk[4:4 + bytes_ultimo_chunk])
                # print(response, len(response))



    return response

