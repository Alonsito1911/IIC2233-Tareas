class Carta:

    def __init__(self, nombre: dict):
        self.nombre = nombre
        self.protagonista = False
        self.siguiente = None


class ColaCarta:


    def __init__(self):

        self.primero = None
        self.ultimo = None

    def tot_llega(self, nombre: dict):
        """
        Agrega un nodo al final de la cola
        """
        nuevo = Carta(nombre)

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = self.primero

        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = self.ultimo.siguiente

    def obtener_tot(self, posicion: int):

        tot_actual = self.primero

        for _ in range(posicion):
            if tot_actual is not None:
                tot_actual = tot_actual.siguiente
            else:
                return None

        return tot_actual

    def obtener_posicion_protagonista(self):
        posicion = 0
        nodo_actual = self.primero
        while nodo_actual.protagonista != True:
            nodo_actual = nodo_actual.siguiente

            posicion += 1

        return posicion

    def tot_se_cola(self, nombre: dict, posicion: int):
        cliente = Carta(nombre)
        cliente_actual = self.primero
        if posicion == 0:
            cliente.siguiente = self.primero
            self.primero = cliente
            if cliente.siguiente is None:
                self.ultimo = cliente

            return
        for _ in range(posicion - 1):
            if cliente_actual is not None:
                cliente_actual = cliente_actual.siguiente
        if cliente_actual is not None:
            cliente.siguiente = cliente_actual.siguiente
            cliente_actual.siguiente = cliente

            if cliente.siguiente is None:
                self.ultimo = cliente


    def tot_se_va(self, posicion: int):

        if posicion == 0:
            tot_nuevo = self.primero.siguiente
            self.primero.siguiente = None
            self.primero = tot_nuevo

            if tot_nuevo.siguiente is None:
                self.ultimo = tot_nuevo

            return

        tot_actual = self.obtener_tot(posicion - 1)
        tot_fuera = tot_actual.siguiente
        tot_actual.siguiente = tot_fuera.siguiente
        tot_fuera.siguiente = None
        if tot_actual.siguiente is None:
            self.ultimo = tot_actual

    def atender_tot(self):

        cliente = self.primero
        self.primero = cliente.siguiente

        return cliente

    def obtener_largo(self):
        posicion = 0
        nodo_actual = self.primero
        while nodo_actual != None:
            nodo_actual = nodo_actual.siguiente

            posicion += 1

        return posicion

    def __str__(self) -> str:

        string = "DULCES :) "
        tot_actual = self.primero
        while tot_actual:
            string += "<- " + tot_actual.nombre
            tot_actual = tot_actual.siguiente

        return string






diccionari = {'0': {'elemento': 'fuego', 'color': 'azul', 'puntos': '5'}, '1': {'elemento': 'nieve', 'color': 'verde', 'puntos': '4'}, '2': {'elemento': 'nieve', 'color': 'verde', 'puntos': '3'}, '3': {'elemento': 'agua', 'color': 'azul', 'puntos': '1'}, '4': {'elemento': 'nieve', 'color': 'azul', 'puntos': '5'}, '5': {'elemento': 'nieve', 'color': 'verde', 'puntos': '1'}, '6': {'elemento': 'agua', 'color': 'verde', 'puntos': '5'}, '7': {'elemento': 'nieve', 'color': 'rojo', 'puntos': '5'}, '8': {'elemento': 'agua', 'color': 'azul', 'puntos': '2'}, '9': {'elemento': 'nieve', 'color': 'azul', 'puntos': '5'}, '10': {'elemento': 'nieve', 'color': 'rojo', 'puntos': '5'}, '11': {'elemento': 'agua', 'color': 'rojo', 'puntos': '1'}, '12': {'elemento': 'fuego', 'color': 'azul', 'puntos': '2'}, '13': {'elemento': 'nieve', 'color': 'azul', 'puntos': '1'}, '14': {'elemento': 'agua', 'color': 'rojo', 'puntos': '3'}}
diccionari2 = {'0': {'elemento': 'agua', 'color': 'azul', 'puntos': '5'}, '1': {'elemento': 'nieve', 'color': 'verde', 'puntos': '4'}, '2': {'elemento': 'nieve', 'color': 'verde', 'puntos': '3'}, '3': {'elemento': 'agua', 'color': 'azul', 'puntos': '1'}, '4': {'elemento': 'nieve', 'color': 'azul', 'puntos': '5'}, '5': {'elemento': 'nieve', 'color': 'verde', 'puntos': '1'}, '6': {'elemento': 'agua', 'color': 'verde', 'puntos': '5'}, '7': {'elemento': 'nieve', 'color': 'rojo', 'puntos': '5'}, '8': {'elemento': 'agua', 'color': 'azul', 'puntos': '2'}, '9': {'elemento': 'nieve', 'color': 'azul', 'puntos': '5'}, '10': {'elemento': 'nieve', 'color': 'rojo', 'puntos': '5'}, '11': {'elemento': 'agua', 'color': 'rojo', 'puntos': '1'}, '12': {'elemento': 'fuego', 'color': 'azul', 'puntos': '2'}, '13': {'elemento': 'nieve', 'color': 'azul', 'puntos': '1'}, '14': {'elemento': 'agua', 'color': 'rojo', 'puntos': '3'}}

# def lista_ligada(diccionario):
  #  mazo = ColaCarta()
   # for j in range(0,  15):

    #    carta = diccionario.get(f"{j}")
     #   type(carta)

      #  mazo.tot_llega(carta)
       # carta1 = mazo.obtener_tot(j)
       # print(carta1.nombre)
    # return mazo
#print(mazo.obtener_largo())
#mazo.tot_se_va(1)
#print(mazo.obtener_largo())

# mazo = lista_ligada(diccionari)
# print("mazo2")
# mazo2 = lista_ligada(diccionari2)
#  dict_ = {"cliente1" : mazo,
  #      "cliente2": mazo2}
