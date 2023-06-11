
from PyQt5.QtGui import QPixmap
from manejop import cargar_datos



from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QRadioButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QIcon
import sys


class VentanaEspera(QWidget):
    senal_enviar_usuario = pyqtSignal(str, str)
    senal_volver_inicio = pyqtSignal(dict)
    senal_iniciar_juego = pyqtSignal(str)
    senal_abrir_juego = pyqtSignal(bool)
    senal_iniciar_cuenta_regresiva = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Geometría
        self.setGeometry(200, 100, 1600, 800)
        # FONDO MENU
        self.escenario = None
        self.usuario = QLabel("", self)
        self.setWindowTitle('Ventana PRINCIPAL')

        self.crear_elementos()

    def crear_elementos(self):

        self.fondo = QLabel(self)
        ruta_imagen = cargar_datos("RUTA_INDEX2")
        pixeles = QPixmap(ruta_imagen)
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 1600, 800)



        self.label_trasero = QLabel(self)
        self.label_trasero.setGeometry(0, 0, 1600, 750)

        self.label_trasero.setStyleSheet("background-color: rgba(0, 0, 0, 125); border-radius: 25px")

        self.label_blanco = QLabel(self)
        self.label_blanco.setGeometry(1000, 100, 500, 500)

        self.label_blanco.setStyleSheet("background-color : white; border-radius: 25px")



        self.jugador2 = QLabel("Jugador 2", self)

        self.jugador2.setGeometry(1200, 100, 500, 500)

        self.jugador2.setFont(QFont('Arial Black', 20))
        self.jugador2.setStyleSheet("color: black;")

        self.label_blanco2 = QLabel(self)
        self.label_blanco2.setGeometry(100, 100, 500, 500)

        self.label_blanco2.setStyleSheet("background-color : white; border-radius: 25px")

        self.jugador1 = QLabel("Jugador 1", self)

        self.jugador1.setGeometry(230, 100, 500, 500)

        self.jugador1.setFont(QFont('Arial Black', 20))
        self.jugador1.setStyleSheet("color: black;")


        self.boton_volver = QPushButton(self)

        self.boton_volver.clicked.connect(self.volver_ventana_inicio)
        self.boton_volver.setStyleSheet("border-radius: 25px")
        imagen = cargar_datos("RUTA_BACK_BUTTON")
        self.boton_volver.setIcon(QIcon(imagen))
        self.boton_volver.setIconSize(QSize(100, 100))
        self.boton_volver.setGeometry(720, 650, 120, 40)

        self.escenario = QLabel("SALA DE ESPERA", self)
        self.escenario.setStyleSheet("color: white;")
        self.escenario.move(530, 20)

        self.escenario.setFont(QFont('Arial Black', 30))

    def cuenta_regresiva(self, numero):
        self.escenario.setText(f'{numero}')
        self.escenario.setGeometry(800, 20, 100, 100)
        if numero == "5":
            self.hide()

    # necesitamos verificar que eliga uno True o False ????
    def inicar_juego(self):
        self.hide()
        self.senal_iniciar_juego.emit(self.escenario)
        self.senal_abrir_juego.emit(True)

        pass
    def mostrar_ventana(self, usuario):

        self.show()

    def volver_ventana_inicio(self):
        #Se transcribe el label usuario :/
        dic_ = {"comando": "volver",
                "booleano": True}
        self.senal_volver_inicio.emit(dic_)
        self.usuario = QLabel(" ", self)
        self.hide()
    def cambiar_label_nombre(self, string, usuario):
        if string == "jugador":
            self.jugador2.setText(f'{usuario}')

        if string == "oponente":
            self.jugador1.setText(f'{usuario}')

