import PyQt5
import json
import socket
from threading import Thread, Lock
from PyQt5.QtCore import QObject, pyqtSignal
from codificacion import codificar, decodificar


class Client(QObject):
    senal_enviar_usuario = pyqtSignal(str)
    senal_iniciar_thread = pyqtSignal(bool)
    senal_iniciar_thread_juego = pyqtSignal(bool)
    senal_enviar5_cartas = pyqtSignal(list)
    senal_enviar_resultado = pyqtSignal(str, list)
    senal_cambiar_label_nombre = pyqtSignal(str, str)
    senal_enviar_ficha = pyqtSignal(str, int, str)
    senal_enviar_resultado_partida = pyqtSignal(str)
    senal_cambiar_label_nombre_venta_juego = pyqtSignal(str, str)
    senal_enviar_carta_oponente = pyqtSignal(str)

    def __init__(self, port, host):
        print("Inicializando cliente...")
        super().__init__()
        self.cartas = []
        self.nombre = ""
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lock = Lock()

        try:
            self.connect_to_server()
            self.listen()

        except ConnectionError:
            print("Conexión terminada.")
            self.socket_client.close()
            exit()

    def connect_to_server(self):
        """Crea la conexión al servidor."""

        self.socket_client.connect((self.host, self.port))
        print("Cliente conectado exitosamente al servidor.")

    def listen(self):
        thread = Thread(target=self.listen_thread, daemon=True)
        thread.start()
    def enviar(self, usuario):

        msg = codificar(usuario)

        self.socket_client.sendall(msg)

    def asignar_nombre_usuario(self, usuario):
        self.nombre = usuario

    def listen_thread(self):
        while True:

            response_bytes_length = self.socket_client.recv(4)

            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')

            response_bytes = self.socket_client.recv(4096)

            response = decodificar(response_length, response_bytes)

            received = response.decode()

            print(received)
            if received != "":
                print("aqui en cliente")
                self.handle_command(received)

    def handle_command(self, received):
        print(f"En  cliente {received}")
        json_dic = json.loads(received)
        print(f"tipo {type(json_dic)}")
        comando = json_dic["comando"]
        print(f"tipo {comando}")
        if comando == "iniciar_timer":
            self.senal_iniciar_thread.emit(True)

            usuario = json_dic["oponente"]
            self.senal_cambiar_label_nombre.emit("oponente", usuario)

        if comando == "jugador":
            usuario = json_dic["usuario"]
            self.senal_cambiar_label_nombre.emit("jugador", usuario)

        if comando == "iniciar_juego":
            oponente = json_dic["oponente"]
            usuario = json_dic["usuario"]
            self.senal_iniciar_thread_juego.emit(True)
            self.senal_cambiar_label_nombre_venta_juego.emit(usuario, oponente)
        if comando == "parar":
            self.senal_iniciar_thread.emit(False)
        if comando == "5cartas":
            lista = json_dic["cartas"]
            print(json_dic["cartas"])
            print("cartas  recibida")
            self.senal_enviar5_cartas.emit(lista)
        if comando == "ganador":
            baraja = json_dic["baraja"]
            rutas_barajas = self.obtener_rutas(baraja)
            self.senal_enviar_resultado.emit("ganador", rutas_barajas)

        if comando == "perdedor":

            baraja = json_dic["baraja"]
            rutas_barajas = self.obtener_rutas(baraja)
            self.senal_enviar_resultado.emit("perdedor", rutas_barajas)

        if comando == "empate":
            baraja = json_dic["baraja"]
            rutas_barajas = self.obtener_rutas(baraja)
            self.senal_enviar_resultado.emit("empate", rutas_barajas)

        if comando == "ficha_mismo_elemento":
            ruta = json_dic["ruta"]
            index = json_dic["index_ficha"]

            self.senal_enviar_ficha.emit(ruta, index, "mismo")

        if comando == "ficha_diferente_elemento":
            ruta = json_dic["ruta"]
            index = json_dic["index_ficha"]
            self.senal_enviar_ficha.emit(ruta, index, "diferente")

        if comando == "iniciar_siguiente_ronda":
            self.senal_iniciar_thread_juego.emit(True)
            pass
        if comando == "ganador_partida":
            self.senal_enviar_resultado_partida.emit("ganador_partida")

        if comando == "perdedor_partida":

            self.senal_enviar_resultado_partida.emit("perdedor_partida")

        if comando == "carta_oponente":
            ruta_carta = json_dic["ruta_carta"]
            self.senal_enviar_carta_oponente.emit(ruta_carta)
            pass
        return received

    def enviar_senal_para_otorgar_mazos(self, string):
        print("string")
        dic_ = {"comando": "otorgar"}
        if string == "otorgar":
            self.enviar(dic_)

    def combate(self):
        dic_ = {"comando": "combate"}
        self.enviar(dic_)

    def recibir_carta_seleccionada(self, numero_carta):
        print(f"el numero de la carta seleccionada es {numero_carta}")
        dict_ = {"comando": "carta_seleccionada", "numero": numero_carta}
        self.enviar(dict_)

    def eleccion_mazo_triunfos(self, eleccion):
        print("aqui")
        if eleccion == "mismo":
            dic_ = {"comando": "mismo_elemento"}
            self.enviar(dic_)
        if eleccion == "diferente":
            dic_ = {"comando": "distinto_elemento"}
            self.enviar(dic_)

        if eleccion == "descartar":
            dic_ = {"comando": "descartar_elemento"}
            self.enviar(dic_)

    def siguiente_ronda(self, string):
        if string == "siguiente":
            dict_ = {"comando": "siguiente"}
            self.enviar(dict_)

    def obtener_rutas(self, lista_dic_):
        lista_ruta_cartas = []
        for i in range(5):
            elemento = lista_dic_[i]["elemento"]
            color = lista_dic_[i]["color"]
            puntos = lista_dic_[i]["puntos"]
            ruta = color + elemento + puntos
            rutaupper = ruta.upper()
            lista_ruta_cartas.append(rutaupper)
        return lista_ruta_cartas



