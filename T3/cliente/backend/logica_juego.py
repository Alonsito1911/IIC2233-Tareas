import sys

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QEventLoop

from manejop import cargar_datos

from time import sleep
class LogicaJuego(QObject):

    senal_cargar_datos_iniciales = pyqtSignal(str, str, str, str, str)
    senal_enviar_zombies = pyqtSignal(object, object)
    senal_mover_zombies = pyqtSignal(int, str, int, int)
    senal_mover_zombies2 = pyqtSignal(int, str, int, int)
    senal_mover_plantas = pyqtSignal(int, str)
    senal_mover_plataforma = pyqtSignal(tuple)
    senal_mover_proyectil = pyqtSignal(int, str,  int, int)
    senal_agregar_proyectil = pyqtSignal(int)
    senal_enviar_ubicacion = pyqtSignal(int)
    senal_mover_pelota = pyqtSignal(tuple)
    senal_eliminar_bloque = pyqtSignal(int)
    senal_bajar_vida = pyqtSignal(int)
    senal_terminar_juego = pyqtSignal(dict)
    senal_cerrar_ventana_juego = pyqtSignal()
    senal_reset_ventana = pyqtSignal()
    senal_zombie_llegaron_a_tu_casa = pyqtSignal(bool)
    senal_abrir_ventana_postronda = pyqtSignal(str, int, int, int, int, int)
    senal_enviar_numeros_ventana_juego = pyqtSignal(str)
    senal_enviar_rutas_cartas = pyqtSignal(list)
    senal_combate = pyqtSignal()
    def __init__(self):
        super().__init__()

        self._puntaje = 0
        self.puntaje_total = 0

        self.indice = 1

        self.timer = QTimer()



        self.tiempo = 1
        self.timer = QTimer()
        self.timer.setInterval(int(self.tiempo * 1000))
        self.timer.timeout.connect(self.cuenta_regresiva_logica_juego)

    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, valor):
        if valor <= 0:
            self._puntaje = 0
        else:
            self._puntaje = valor

    def iniciar_cuenta_regresiva_logica_juego(self, bool):


        if bool == True:
            if self.timer.isActive() == True:
                return
            self.timer.start()

        else:
            self.timer.stop()

    def cuenta_regresiva_logica_juego(self):
        if self.indice <= cargar_datos("CUENTA_REGRESIVA_JUEGO"):

            self.senal_enviar_numeros_ventana_juego.emit(str(self.indice))
            self.indice += 1
        else:
            self.indice = 0
            self.senal_combate.emit()
            self.timer.stop()

    def recibir_5_cartas(self, lista_dic_):
        lista_ruta_cartas = []
        for i in range(5):
            ruta = ""
            elemento = lista_dic_[i]["elemento"]
            color = lista_dic_[i]["color"]
            puntos = lista_dic_[i]["puntos"]
            ruta = color + elemento + puntos
            rutaupper = ruta.upper()
            lista_ruta_cartas.append(rutaupper)
        self.senal_enviar_rutas_cartas.emit(lista_ruta_cartas)

















