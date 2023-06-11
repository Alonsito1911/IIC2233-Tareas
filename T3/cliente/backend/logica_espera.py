
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

import socket
import threading
from time import sleep
from manejop import cargar_datos
# Inicia un thread que realiza la cuenta regresiva cuando el server detecta ya dos jugadores conectados

class LogicaEspera(QObject):

    senal_abrir_ventana_juego = pyqtSignal(str)
    senal_enviar_numeros = pyqtSignal(str)
    senal_otorgar_mazo = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.indice = 1
        self.thread = None
        self.tiempo = 1
        self.timer = QTimer()
        self.timer.setInterval(int(self.tiempo * 1000))
        self.timer.timeout.connect(self.cuenta_regresiva)
    def iniciar_cuenta_regresiva(self, bool):
        # thread = threading.Thread(target=self.cuenta_regresiva)
        # thread.start()
        if bool == True:
            self.timer.start()

        else:
            self.indice = 0
            self.timer.stop()

    def cuenta_regresiva(self):
        if self.indice <= cargar_datos("CUENTA_REGRESIVA_INICIO"):
            print(self.indice)
            self.senal_enviar_numeros.emit(str(self.indice))
            self.indice += 1
        else:

            self.senal_abrir_ventana_juego.emit("abrir")
            self.senal_otorgar_mazo.emit("otorgar")
            self.indice = 0
            self.timer.stop()





