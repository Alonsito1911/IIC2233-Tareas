def encriptar(msg: bytearray) -> bytearray:
    #  Completar con el proceso de encriptación
    a = msg[::3]
    mensaje_desde_i_1 = msg[1:]
    b = mensaje_desde_i_1[::3]

    mensaje_desde_i_2 = msg[2:]
    c = mensaje_desde_i_2[::3]
    suma = a[0] + c[-1]
    if len(b) % 2 == 0:
        numero_central = int(len(b) / 2)

        suma += b[numero_central] + b[numero_central - 1]
    else:
        indice_central = int(len(b) / 2 + 0.5)
        suma += b[indice_central]

    if suma % 2 == 0:
        code = b"\x00" + c + a + b
        return code
    else:
        code = b"\x01" + a + c + b
        return code


def desencriptar(msg: bytearray) -> bytearray:
    #  Completar con el proceso de desencriptación
    largo = len(msg[1:])
    mensaje_a_leer = msg[1:]
    # largo // 3 es la cantidad de bytes que tiene hasta que no se vuelve multipo de 3
    largo_bytes = largo // 3
    # en caso de que no sea nuestro mensaje divisible por 3, si el resto == 1 significa que A tiene asignado
    # un valor y si es resto == 2 signifca que A y B tienen asignado un Byte
    resto = largo % 3
    A = []
    B = []
    C = []
    a = 0
    b = 1
    c = 2
    for j in range(largo_bytes):
        A.append(a)
        B.append(b)
        C.append(c)
        a += 3
        b += 3
        c += 3

    if resto == 1:
        print()
    elif resto == 2:
        ultimo_valor_a = A[-1]
        ultimo_valor_b = B[-1]
        ultimo_valor_a += 3
        ultimo_valor_b += 3
        A.append(ultimo_valor_a)
        B.append(ultimo_valor_b)
    diccionario_byte = {}
    # sabiendo las coordenadas
    if msg[0] == 0:
        print("CBA")
        for coordenada in range(len(C)):
            diccionario_byte[f"{C[coordenada]}"] = mensaje_a_leer[coordenada]

        for coordenada in range(len(B)):
            diccionario_byte[f"{B[coordenada]}"] = mensaje_a_leer[len(C):][coordenada]

        for coordenada in range(len(B)):
            diccionario_byte[f"{A[coordenada]}"] = mensaje_a_leer[len(B) + len(C):][coordenada]

        # ordenamos

        lista_byte = bytearray()
        for byte in range(len(mensaje_a_leer)):
            lista_byte.append(diccionario_byte.get(f"{byte}"))

        return lista_byte[0:]
    else:

        for coordenada in range(len(A)):
            diccionario_byte[f"{A[coordenada]}"] = mensaje_a_leer[coordenada]

        for coordenada in range(len(C)):
            diccionario_byte[f"{C[coordenada]}"] = mensaje_a_leer[len(A):][coordenada]

        for coordenada in range(len(B)):
            diccionario_byte[f"{B[coordenada]}"] = mensaje_a_leer[len(A) + len(C):][coordenada]

        # ordenamos

        lista_byte = bytearray()
        for byte in range(len(mensaje_a_leer)):
            lista_byte.append(diccionario_byte.get(f"{byte}"))

        return lista_byte[0:]


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

    # Testear desencriptar

    msg_desencriptado = desencriptar(msg_esperado)

    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")

