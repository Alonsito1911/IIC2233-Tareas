from manejop import cargar_datos

from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QLineEdit)
from PyQt5.QtGui import QPixmap, QIcon
import sys

class VentanaInicio(QWidget):

    senal_enviar_usuario = pyqtSignal(dict)
    senal_ver_ranking = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Geometría
        self.setGeometry(200, 50, 1600, 1000)
        # FONDO MENU

        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("")
        self.crear_elementos()

    def crear_elementos(self):

        self.fondo = QLabel(self)
        ruta_imagen = cargar_datos("RUTA_INDEX1")
        pixeles = QPixmap(ruta_imagen)
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 1600, 1000)


        self.input = QLineEdit('', self)
        self.input.setGeometry(630, 750, 400, 35)
        self.input.setStyleSheet("border-radius: 25px")
        # Qlabel
        self.ingresar_nombre_usuario = QLabel('Ingresa tu nombre de usuario:', self)
        self.ingresar_nombre_usuario.move(100, 500)
        self.ingresar_nombre_usuario.repaint()

        # Qpushbutton
        self.boton = QPushButton('Jugar', self)
        self.boton.resize(self.boton.sizeHint())
        self.boton.clicked.connect(self.enviar_usuario)
        self.boton.move(780, 700)





        # self.boton_puerta = QPushButton(self)
        # self.boton_puerta.resize(self.boton_puerta.sizeHint())
        # self.boton_puerta.clicked.connect(self.enviar_usuario)
        # imagen = cargar_datos("RUTA_DOOR")


        # self.boton_puerta.setIcon(QIcon(imagen))
        # self.boton_puerta.setIconSize(QSize(100, 100))
        # self.boton_puerta.setGeometry(720, 440, 300, 500)







    def enviar_usuario(self):
        usuario = self.input.text()
        dic = {"comando" : "usuario",
                "usuario": usuario}
        self.senal_enviar_usuario.emit(dic)

        # COMPLETAR
        pass

    def recibir_validacion(self, valid: bool) -> None:
        if valid == True:
            self.hide()
        if valid == False:
            self.input.setText("")
            self.input.setPlaceholderText("NO ENTREGASTE USUARIO O TU USUARIO NO FUE ALFANUMERICO")
        # COMPLETAR

    def ver_ranking(self):
        self.hide()
        self.senal_ver_ranking.emit("Ver")

    def otorgar_labales_5_cartas(self):
        pass
    def salir(self):
        sys.exit()