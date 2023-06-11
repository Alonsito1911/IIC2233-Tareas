import socket
import threading
import json
from cartas import get_penguins

from manejop import cargar_datos
from codificacion import codificar, decodificar
from lista_ligada import ColaCarta
from logica import combate

class Server:
    def __init__(self, port, host):
        print("Inicializando servidor...")
        # self.cantidad_clientes = 0
        self.clientes = []  # limpiar
        # self.clientes_id = {}
        self.usernames = {}  # limpiar
        self.mazos = {}  # limpiar
        self.lista_5_cartas = {}  # limpiar
        self.cartas_seleccionadas = {} #limpiar
        self.mazos_triunfos = {}
        self.resultado = None
        self.host = host
        self.port = port
        self.confirmaciones_siguiente_ronda = 0
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock = threading.Lock()
        self.bind_and_listen()
        self.accept_connections()


    def bind_and_listen(self):

        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self):
        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self):
        print("Servidor aceptando conexiones...")

        while True:
            try:
                client_socket, _ = self.socket_server.accept()
                listening_client_thread = threading.Thread(
                    target=self.listen_client_thread, args=(client_socket, ),
                    daemon=True)
                listening_client_thread.start()
            except ConnectionError:
                return

    @staticmethod
    def send(value, sock):

        msg = codificar(value)

        sock.sendall(msg)

    def listen_client_thread(self, client_socket):
        if len(self.clientes) < 2:
            print("Servidor conectado a un nuevo cliente...")
            self.clientes.append(client_socket)
            while True:
                try:
                    response_bytes_length = client_socket.recv(4)
                    response_length = int.from_bytes(
                        response_bytes_length, byteorder='big')
                    response_bytes = client_socket.recv(4096)
                    response = decodificar(response_length, response_bytes)
                    received = response.decode()
                    if received != "":
                        self.handle_command(received, client_socket)
                except:
                    if len(self.usernames) > 0:
                        username = self.usernames[client_socket]
                        self.usernames.pop(client_socket)
                        self.clientes.remove(client_socket)
                        if len(self.mazos_triunfos) >= 1:
                            self.mazos_triunfos.pop(client_socket)
                        if len(self.mazos) >= 1:
                            self.mazos.pop(client_socket)
                        if len(self.lista_5_cartas) >= 1:
                            self.lista_5_cartas.pop(client_socket)
                        print(f"usuario {username} desconectado")
                    print(f"Cliente desconectado")
                    client_socket.close()
                    break

        else:
            print("maximo clientes")
            return

    def handle_command(self, received, client_socket):
        json_dic = json.loads(received)

        comando = json_dic["comando"]


        if comando == "usuario":
            usuario = json_dic["usuario"]
            print(f"usuario recibido:{usuario} ")
            self.usernames[client_socket] = usuario
            self.mazos_triunfos[client_socket] = {"mismo_elemento": [], "distinto_elemento": []}
            dict_ = {"comando": "jugador", "usuario": self.usernames[client_socket]}
            self.send(dict_, client_socket)
            self.verificar_clientes()
        if comando == "volver":
            dic_ = {"comando": "parar"}
            self.usernames.pop(client_socket)
            self.mazos_triunfos.pop(client_socket)
            self.enviar_a_todos(dic_)


        if comando == "otorgar":

            dic_ = get_penguins()
            mazo_lista_ligada = self.lista_ligada_mazo(dic_)
            self.mazos[client_socket] = mazo_lista_ligada
            self.enviar_usuarios("juego")

            self.enviar_5_cartas(client_socket)
        if comando == "carta_seleccionada":

            numero = json_dic["numero"]

            if len(self.cartas_seleccionadas) < 2:


                baraja = self.lista_5_cartas[client_socket]

                carta_seleccionada = baraja.pop(numero)
                print(f"la carta seleccionada por ",self.usernames[client_socket],
                      " fue ", carta_seleccionada["elemento"],
                      f" de color ",carta_seleccionada["color"]," con un puntaje de ", carta_seleccionada["puntos"])

                ruta_carta = self.obtener_ruta_carta(carta_seleccionada)
                dict_ = {"comando": "carta_oponente", "ruta_carta": ruta_carta}
                self.notificar_a_otros_usuarios(dict_, client_socket)
                self.cartas_seleccionadas[client_socket] = {"carta": carta_seleccionada, "numero": numero}


            else:
                print("MAXIMO DE CARTAS SELECCIONADAS")
                return
        if comando == "combate":
            cliente_entregar = self.obtener_cliente(client_socket)

            if len(self.cartas_seleccionadas) == 2:
                resultado = combate(client_socket, cliente_entregar,  self.cartas_seleccionadas)
                self.resultado_combate(resultado, client_socket)
            else:
                print("por alguna razon no se elegieron las dos cartas para combatir")



        if comando == "mismo_elemento":
            self.eleccion_mazo_triunfos_mismo_elemento(client_socket)

        if comando == "distinto_elemento":
            self.eleccion_mazo_triunfos_distino_elemento(client_socket)
        if comando == "descartar_elemento":
            self.eleccion_mazo_triunfos_descartar_elemento(client_socket)

        if comando == "siguiente":
            dic_ = {"comando": "iniciar_siguiente_ronda"}

            self.siguiente_ronda(dic_)
            self.resetear()
    def verificar_clientes(self):
        print("Cliente conectado")
        print(f"Numero de usernames {(len(self.usernames))}")
        if len(self.usernames) == 2:

            print(f"SE HAN CONECTADO TODOS LOS CLIENTES A JUGAR !")

            self.enviar_usuarios("espera")
    def siguiente_ronda(self, dict_):
        self.confirmaciones_siguiente_ronda += 1
        if self.confirmaciones_siguiente_ronda == 2:
            self.enviar_a_todos(dict_)
            self.confirmaciones_siguiente_ronda = 0
    def obtener_cliente(self, cliente_socket):
        for cliente in self.clientes:
            if cliente != cliente_socket:
                return cliente
    def obtener_ruta_carta(self, carta):
        color = carta["color"]
        elemento = carta["elemento"]
        puntos = carta["puntos"]
        ruta = color + elemento + puntos
        ruta_final = ruta.upper()
        return ruta_final

    def enviar_usuarios(self, ventana):

        for clientes in self.clientes:
            oponente = self.obtener_cliente(clientes)
            usuario_oponente = self.usernames[oponente]
            usuario = self.usernames[clientes]
            if ventana == "espera":
                iniciar_thread = {"comando": "iniciar_timer", "oponente": usuario_oponente}
                self.send(iniciar_thread, clientes)
            elif ventana == "juego":
                iniciar_thread = {"comando": "iniciar_juego", "usuario": usuario, "oponente": usuario_oponente}
                self.send(iniciar_thread, clientes)

    def enviar_a_todos(self, dic_):

        for clientes in self.clientes:

            self.send(dic_, clientes)

    def notificar_a_otros_usuarios(self, dic_, client_socket):
        for cliente in self.clientes:
            if cliente != client_socket:
                self.send(dic_, cliente)

    def lista_ligada_mazo(self, diccionario):
        mazo = ColaCarta()
        for j in range(0, 15):
            carta = diccionario.get(f"{j}")
            mazo.tot_llega(carta)
            carta1 = mazo.obtener_tot(j)
        return mazo

    def enviar_5_cartas(self, client_socket):

        mazo = self.mazos[client_socket]
        lista = []
        for carta in range(5):
            carta1 = mazo.obtener_tot(carta)
            mazo.tot_se_va(carta)
            lista.append(carta1.nombre)
        self.lista_5_cartas[client_socket] = lista
        dict_ = {"comando": "5cartas", "cartas": self.lista_5_cartas[client_socket]}
        self.send(dict_, client_socket)

    def resultado_combate(self, resultado, client_socket):
        dic_ = resultado[client_socket]
        resultado = dic_["resultado"]
        largo = self.mazos[client_socket].obtener_largo()
        if resultado == "ganador":
            usuario = self.usernames[client_socket]
            self.resultado = dic_
            sacar_carta_mazo = self.mazos[client_socket].obtener_tot(0)
            self.mazos[client_socket].tot_se_va(0)
            self.lista_5_cartas[client_socket].append(sacar_carta_mazo.nombre)
            dict_ = {"comando": "ganador",
                     "baraja": self.lista_5_cartas[client_socket]}
            print(f"GANADOR DE LA RONDA {usuario}")
            self.send(dict_, client_socket)

        elif resultado == "perdedor":

            self.mazos[client_socket].tot_se_cola(dic_["carta"], largo)
            sacar_carta_mazo = self.mazos[client_socket].obtener_tot(0)
            self.mazos[client_socket].tot_se_va(0)
            self.lista_5_cartas[client_socket].append(sacar_carta_mazo.nombre)
            dict_ = {"comando": "perdedor",
                     "baraja": self.lista_5_cartas[client_socket]}
            self.send(dict_, client_socket)

        elif resultado == "empate":

            self.mazos[client_socket].tot_se_cola(dic_["carta"], largo)
            sacar_carta_mazo = self.mazos[client_socket].obtener_tot(0)
            self.mazos[client_socket].tot_se_va(0)
            self.lista_5_cartas[client_socket].append(sacar_carta_mazo.nombre)
            dict_ = {"comando": "empate", "baraja": self.lista_5_cartas[client_socket]}
            self.send(dict_, client_socket)
        else:
            print("erroneo")
            return

    def eleccion_mazo_triunfos_mismo_elemento(self, client_socket):
        resultado = self.resultado
        mazo_triunfos = self.mazos_triunfos[client_socket]
        elemento = resultado["carta"]["elemento"]
        color = resultado["carta"]["color"]
        ruta = elemento + color
        ruta_final = ruta.upper()
        mazo_triunfos["mismo_elemento"].append(ruta)
        print(mazo_triunfos["mismo_elemento"])
        index = len(mazo_triunfos["mismo_elemento"]) - 1
        dict_ = {"comando" : "ficha_mismo_elemento", "ruta": ruta_final, "index_ficha": index}
        self.send(dict_, client_socket)
        self.verificar_ganador(client_socket)


    def eleccion_mazo_triunfos_distino_elemento(self, client_socket):
        mazo_triunfos = self.mazos_triunfos[client_socket]
        resultado = self.resultado
        elemento = resultado["carta"]["elemento"]
        color = resultado["carta"]["color"]
        ruta = elemento + color
        ruta_final = ruta.upper()
        mazo_triunfos["distinto_elemento"].append(ruta)
        index = len(mazo_triunfos["distinto_elemento"]) - 1
        dict_ = {"comando": "ficha_diferente_elemento", "ruta": ruta_final, "index_ficha": index}
        self.send(dict_, client_socket)
        self.verificar_ganador(client_socket)

    def eleccion_mazo_triunfos_descartar_elemento(self, client_socket):
        largo = self.mazos[client_socket].obtener_largo()
        resultado = self.resultado
        self.mazos[client_socket].tot_se_cola(resultado["carta"], largo)
    def verificar_ganador(self, client_socket):
        mazo_triunfo = self.mazos_triunfos[client_socket]
        dict_1 = {"comando": "perdedor_partida"}
        dict_2 = {"comando": "ganador_partida"}
        oponente = self.obtener_cliente(client_socket)
        if len(mazo_triunfo["mismo_elemento"]) == 3 and len(mazo_triunfo["distinto_elemento"]) == 3:
            self.send(dict_1, client_socket)
            self.send(dict_2, oponente)

    def resetear(self):
        self.cartas_seleccionadas = {}



if __name__ == "__main__":
    port = 55556
    host = socket.gethostname()

    server = Server(port, host)