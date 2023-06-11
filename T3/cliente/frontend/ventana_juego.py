from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QRadioButton
)
from PyQt5.QtGui import QPixmap, QIcon, QFont


from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QEventLoop


from random import randint
from manejop import cargar_datos


class VentanaJuego(QWidget):

    senal_enviar_carta_seleccionada = pyqtSignal(int)
    senal_mismo_elemento = pyqtSignal(str)
    senal_diferente_elemento = pyqtSignal(str)
    senal_descartar_elemento = pyqtSignal(str)
    senal_siguiente_ronda = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.label_cuadro = QLabel(self)
        self.label_cuadro1 = QLabel(self)
        self.label_verde = QLabel(self)

        self.labels_mismo_elemento = {}
        self.label_diferente_elemento = {}


        self.label_texto = QLabel(self)

        self.carta_seleccionada = None
        self.estado_siguiente_ronda = False
        self.seleccion_carta_bool = False
        self.seleccion_mazo_triunfo = False
        self.ruta_cartas = []

    def init_gui(self):
        print("aqui")
        self.fondo = QLabel(self)
        ruta_imagen = cargar_datos("RUTA_DOJO1")
        pixeles = QPixmap(ruta_imagen)
        self.fondo.setPixmap(pixeles)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 1600, 800)
        self.label_trasero = QLabel(self)
        self.label_trasero.setGeometry(0, 0, 1600, 750)

        self.label_trasero.setStyleSheet("background-color: rgba(0, 0, 0, 125); border-radius: 25px")
        self.label_tabla = QLabel(self)
        ruta_imagen_tabla = cargar_datos("RUTA_TABLE")
        pixeles2 = QPixmap(ruta_imagen_tabla)
        self.label_tabla.setPixmap(pixeles2)
        self.label_tabla.setScaledContents(True)
        self.label_tabla.setGeometry(150,  100, 1200, 700)

        self.escenario = QLabel("SALA DE JUEGO", self)
        self.escenario.setStyleSheet("color: white;")
        self.escenario.move(600, 20)

        self.escenario.setFont(QFont('Arial Black', 30))

        # carta 2

        self.label_carta1 = QLabel(self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta1.setPixmap(pixeles4)
        self.label_carta1.setScaledContents(True)
        self.label_carta1.setGeometry(210, 670, 80, 70)
        self.label_carta1.setFont(QFont('Arial Black', 10))
        self.label_carta1.setStyleSheet("color: white;")

        self.label_carta1_boton = QRadioButton("1", self)
        self.label_carta1_boton.setGeometry(240, 750, 100, 50)

        self.label_carta1_boton.clicked.connect(self.carta_elegida_1)

        self.label_carta2 = QLabel("Carta2", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta2.setPixmap(pixeles4)
        self.label_carta2.setScaledContents(True)
        self.label_carta2.setGeometry(310, 670, 80, 70)
        self.label_carta2.setFont(QFont('Arial Black', 10))
        self.label_carta2.setStyleSheet("color: white;")

        self.label_carta2_boton = QRadioButton(self)
        self.label_carta2_boton.setGeometry(340, 750, 100, 50)
        self.label_carta2_boton.clicked.connect(self.carta_elegida_2)

        # carta 3

        self.label_carta3 = QLabel("carta3", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta3.setPixmap(pixeles4)
        self.label_carta3.setScaledContents(True)
        self.label_carta3.setGeometry(410, 670, 80, 70)
        self.label_carta3.setFont(QFont('Arial Black', 10))
        self.label_carta3.setStyleSheet("color: white;")
        self.label_carta3_boton = QRadioButton(self)
        self.label_carta3_boton.setGeometry(440, 750, 100, 50)
        self.label_carta3_boton.clicked.connect(self.carta_elegida_3)
        self.label_carta4 = QLabel("Carta 4", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta4.setPixmap(pixeles4)
        self.label_carta4.setScaledContents(True)

        self.label_carta4.setGeometry(510, 670, 80, 70)

        self.label_carta4.setFont(QFont('Arial Black', 10))
        self.label_carta4.setStyleSheet("color: white;")

        self.label_carta4_boton = QRadioButton(self)

        self.label_carta4_boton.setGeometry(540, 750, 100, 50)

        self.label_carta4_boton.clicked.connect(self.carta_elegida_4)

        self.label_carta5 = QLabel("carta 5", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta5.setPixmap(pixeles4)
        self.label_carta5.setScaledContents(True)
        self.label_carta5.setGeometry(610, 670, 80, 70)
        self.label_carta5.setFont(QFont('Arial Black', 10))
        self.label_carta5.setStyleSheet("color: white;")

        self.label_carta5_boton = QRadioButton(self)
        self.label_carta5_boton.setGeometry(640, 750, 100, 50)
        self.label_carta5_boton.clicked.connect(self.carta_elegida_5)

        self.boton = QPushButton('SELECCIONAR', self)
        self.boton.setGeometry(1000, 700, 100, 30)
        self.boton.clicked.connect(self.enviar_carta_seleccionada)

        self.boton_misma_elemento = QPushButton("MISMO_ELEMENTO", self)
        self.boton_diferente_elemento = QPushButton("DISTINTO_ELEMENTO", self)
        self.boton_misma_elemento.setGeometry(700, 700, 140, 20)
        self.boton_diferente_elemento.setGeometry(700, 725, 140, 20)

        self.boton_siguiente_ronda = QPushButton('SIGUIENTE RONDA', self)

        self.boton_siguiente_ronda.setGeometry(1150, 700, 140, 30)
        self.boton_siguiente_ronda.clicked.connect(self.siguiente_ronda)

        self.boton_descartar = QPushButton('DESCARTAR', self)
        self.boton_descartar.setGeometry(700, 750, 140, 20)

        self.label_carta_elegida = QLabel(self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_elegida.setPixmap(pixeles4)
        self.label_carta_elegida.setScaledContents(True)
        self.label_carta_elegida.setGeometry(1000, 100, 300, 400)
        self.label_carta_elegida.setFont(QFont('Arial Black', 10))
        self.label_carta_elegida.setStyleSheet("color: white;")

        self.label_carta_elegida_contricante = QLabel(self)
        ruta_carta = cargar_datos(f"RUTA_BACK_CARTA")

        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_elegida_contricante.setPixmap(pixeles4)
        self.label_carta_elegida_contricante.setScaledContents(True)
        self.label_carta_elegida_contricante.setGeometry(300, 100, 300, 400)
        self.label_carta_elegida_contricante.setFont(QFont('Arial Black', 10))
        self.label_carta_elegida_contricante.setStyleSheet("color: white;")

        self.nombre_oponente = QLabel("OPONENTE", self)
        self.nombre_oponente.setStyleSheet("color: white;")
        self.nombre_oponente.move(400, 50)
        self.nombre_oponente.setFont(QFont('Arial Black', 15))

        self.nombre = QLabel("JUGADOR", self)
        self.nombre.setStyleSheet("color: white;")
        self.nombre.move(1100, 50)
        self.nombre.setFont(QFont('Arial Black', 15))

        self.label_carta_contricante = QLabel("carta c", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_contricante.setPixmap(pixeles4)
        self.label_carta_contricante.setScaledContents(True)
        self.label_carta_contricante.setGeometry(200, 100, 50, 30)
        self.label_carta_contricante.setFont(QFont('Arial Black', 10))
        self.label_carta_contricante.setStyleSheet("color: white;")
        self.label_carta_contricante2 = QLabel("carta c", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_contricante2.setPixmap(pixeles4)
        self.label_carta_contricante2.setScaledContents(True)
        self.label_carta_contricante2.setGeometry(200, 150, 50, 30)
        self.label_carta_contricante2.setFont(QFont('Arial Black', 10))
        self.label_carta_contricante2.setStyleSheet("color: white;")

        self.label_carta_contricante3 = QLabel("carta c", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_contricante3.setPixmap(pixeles4)
        self.label_carta_contricante3.setScaledContents(True)
        self.label_carta_contricante3.setGeometry(200, 200, 50, 30)
        self.label_carta_contricante3.setFont(QFont('Arial Black', 10))
        self.label_carta_contricante3.setStyleSheet("color: white;")
        self.label_carta_contricante4 = QLabel("carta c", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_contricante4.setPixmap(pixeles4)
        self.label_carta_contricante4.setScaledContents(True)
        self.label_carta_contricante4.setGeometry(200, 250, 50, 30)
        self.label_carta_contricante4.setFont(QFont('Arial Black', 10))
        self.label_carta_contricante4.setStyleSheet("color: white;")
        self.label_carta_contricante5 = QLabel("carta c", self)
        ruta_carta = cargar_datos("RUTA_BACK_CARTA")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_contricante5.setPixmap(pixeles4)
        self.label_carta_contricante5.setScaledContents(True)
        self.label_carta_contricante5.setGeometry(200, 300, 50, 30)
        self.label_carta_contricante5.setFont(QFont('Arial Black', 10))
        self.label_carta_contricante5.setStyleSheet("color: white;")

        self.boton_volver = QPushButton(self)

        self.boton_volver.clicked.connect(self.volver_ventana_inicio)
        self.boton_volver.setStyleSheet("border-radius: 25px")
        imagen = cargar_datos("RUTA_BACK_BUTTON")
        self.boton_volver.setIcon(QIcon(imagen))
        self.boton_volver.setIconSize(QSize(100, 100))
        self.boton_volver.hide()

        self.boton_volver.setGeometry(720, 500, 120, 40)
        # jejeje
        self.labels_mismo_elemento = {
            i: QLabel(self)
            for i in range(0, 3)}

        self.label_diferente_elemento = {
            i: QLabel(self)
            for i in range(0, 3)}
        coordenada = 50
        for k in range(3):
            self.labels_mismo_elemento[k].setGeometry(1400, coordenada, 80, 40)

            self.label_diferente_elemento[k].setGeometry(1300, coordenada, 80, 40)
            coordenada += 50
        # Configuramos las propiedades de la ventana.
        self.setWindowTitle('Ejemplo threads')
        self.setGeometry(200, 100, 1600, 800)
        self.show()

    # Funcion actualizar_parametros que pretende actualizar los labels a medida que avanza el juego
    def actualizar_fichas(self, ruta, index, tipo):
        if tipo == "mismo":
            print("MISMO")
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.labels_mismo_elemento[index].setPixmap(pixeles4)
            self.labels_mismo_elemento[index].setScaledContents(True)


        if tipo == "diferente":
            print("DIFERENTE")
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.label_diferente_elemento[index].setPixmap(pixeles4)
            self.label_diferente_elemento[index].setScaledContents(True)



    def actualizar_cartas(self, rutas_cartas):
        self.ruta_cartas = rutas_cartas
        for carta in range(5):
            if carta == 0:
                ruta = rutas_cartas[0]
                ruta_carta = cargar_datos(f"{ruta}")
                pixeles4 = QPixmap(ruta_carta)
                self.label_carta1.setPixmap(pixeles4)
                self.label_carta1.setScaledContents(True)
            if carta == 1:
                ruta = rutas_cartas[1]
                ruta_carta = cargar_datos(f"{ruta}")
                pixeles4 = QPixmap(ruta_carta)
                self.label_carta2.setPixmap(pixeles4)
                self.label_carta2.setScaledContents(True)

            if carta == 2:
                ruta = rutas_cartas[2]
                ruta_carta = cargar_datos(f"{ruta}")
                pixeles4 = QPixmap(ruta_carta)
                self.label_carta3.setPixmap(pixeles4)
                self.label_carta3.setScaledContents(True)

            if carta == 3:
                ruta = rutas_cartas[3]
                ruta_carta = cargar_datos(f"{ruta}")
                pixeles4 = QPixmap(ruta_carta)
                self.label_carta4.setPixmap(pixeles4)
                self.label_carta4.setScaledContents(True)
            if carta == 4:
                ruta = rutas_cartas[4]
                ruta_carta = cargar_datos(f"{ruta}")
                pixeles4 = QPixmap(ruta_carta)
                self.label_carta5.setPixmap(pixeles4)
                self.label_carta5.setScaledContents(True)

    def cuenta_regresiva(self, numero):
        self.escenario.setText(f'{numero}')
        self.escenario.setGeometry(800, 20, 100, 100)
        print(numero)
        print(f" estado carta seleccionada {self.seleccion_carta_bool}")
        if numero == "5":
            if self.seleccion_carta_bool == False:

                self.carta_seleccionada = randint(0, 4)
                self.senal_enviar_carta_seleccionada.emit(self.carta_seleccionada)
                if self.carta_seleccionada == 0:
                    self.carta_elegida_1()
                    self.seleccion_carta_bool = True
                elif self.carta_seleccionada == 1:
                    self.carta_elegida_2()
                    self.seleccion_carta_bool = True

                elif self.carta_seleccionada == 2:
                    self.carta_elegida_3()
                    self.seleccion_carta_bool = True

                elif self.carta_seleccionada == 3:
                    self.carta_elegida_4()
                    self.seleccion_carta_bool = True

                elif self.carta_seleccionada == 4:
                    self.carta_elegida_5()
                    self.seleccion_carta_bool = True



    def cambiar_label_nombre(self,  usuario, oponente):
        print("AQUU")

        self.nombre.setText(f'{usuario}')
        self.nombre_oponente.setText(f'{oponente}')

    def carta_elegida_1(self):
        print("carta elegida 1")
        if self.seleccion_carta_bool == False:
            self.carta_seleccionada = 0
            ruta = self.ruta_cartas[0]
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.label_carta_elegida.setPixmap(pixeles4)
            self.label_carta_elegida.setScaledContents(True)

    def carta_elegida_2(self):
        print("carta elegida 2")
        if self.seleccion_carta_bool == False:
            self.carta_seleccionada = 1
            ruta = self.ruta_cartas[1]
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.label_carta_elegida.setPixmap(pixeles4)
            self.label_carta_elegida.setScaledContents(True)

    def carta_elegida_3(self):
        print("carta elegida 3")
        if self.seleccion_carta_bool == False:
            self.carta_seleccionada = 2
            ruta = self.ruta_cartas[2]
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.label_carta_elegida.setPixmap(pixeles4)
            self.label_carta_elegida.setScaledContents(True)

    def carta_elegida_4(self):
        print("carta elegida 4")
        if self.seleccion_carta_bool == False:
            self.carta_seleccionada = 3
            ruta = self.ruta_cartas[3]
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.label_carta_elegida.setPixmap(pixeles4)
            self.label_carta_elegida.setScaledContents(True)

    def carta_elegida_5(self):
        print("carta elegida 5")
        if self.seleccion_carta_bool == False:
            self.carta_seleccionada = 4
            ruta = self.ruta_cartas[4]
            ruta_carta = cargar_datos(f"{ruta}")
            pixeles4 = QPixmap(ruta_carta)
            self.label_carta_elegida.setPixmap(pixeles4)
            self.label_carta_elegida.setScaledContents(True)


    # se repite codigo(solucionar)
    def resultado(self, resultado, baraja):
        self.estado_siguiente_ronda = False
        self.label_cuadro1 = QLabel(self)
        self.label_cuadro1.setGeometry(560, 350, 450, 130)
        self.label_cuadro1.setStyleSheet("background-color : white; border-radius: 25px")
        self.label_texto = QLabel(self)
        self.label_texto.setGeometry(620, 400, 400, 20)
        self.label_texto.setFont(QFont('Arial Black', 15))
        self.label_texto.setStyleSheet("color: black;")
        if resultado == "ganador":
            self.actualizar_cartas(baraja)
            print(baraja)
            self.label_texto.setText("GANASTE ESTA RONDA")

            self.boton_misma_elemento.clicked.connect(self.mismo_elemento)
            self.boton_diferente_elemento.clicked.connect(self.diferente_elemento)
            self.boton_descartar.clicked.connect(self.descartar_elemento)
        elif resultado == "perdedor":
            self.actualizar_cartas(baraja)

            print(baraja)
            self.label_texto.setText("PERDISTE ESTA RONDA")
        elif resultado == "empate":
            self.actualizar_cartas(baraja)
            self.label_texto.setText("EMPATE EN ESTA RONDA")

        elif resultado == "perdedor_partida":
            self.label_cuadro1.setGeometry(0, 0, 1600, 750)
            self.label_texto.setText("PERDISTE ESTA PARTIDA! :c")
            self.boton_volver.show()
        elif resultado == "ganador_partida":
            self.label_cuadro1.setGeometry(0, 0, 1600, 750)
            self.label_texto.setText("!FELICIDADES HAS GANADO! ")
            self.boton_volver.show()
        else:
            self.actualizar_cartas(baraja)
            print(baraja)
            self.label_texto.setText("EMPATE")


        self.label_cuadro.show()
        self.label_cuadro1.show()
        self.label_texto.show()

        # self.boton_diferente_elemento.show()
        # self.boton_misma_elemento.show()
    def enviar_carta_seleccionada(self):
        self.seleccion_carta_bool = True
        self.senal_enviar_carta_seleccionada.emit(self.carta_seleccionada)
    def desconectar_botones(self):
        self.boton_misma_elemento.clicked.disconnect(self.mismo_elemento)
        self.boton_diferente_elemento.clicked.disconnect(self.diferente_elemento)
        self.boton_descartar.clicked.disconnect(self.descartar_elemento)
    def mismo_elemento(self):


        print("mismo")
        self.senal_mismo_elemento.emit("mismo")
        self.desconectar_botones()


    def diferente_elemento(self):

        print("diferente")
        self.senal_diferente_elemento.emit("diferente")
        self.desconectar_botones()

    def descartar_elemento(self):

        print("diferente")
        self.senal_descartar_elemento.emit("descartar")
        self.desconectar_botones()
    def cambiar_label_carta_oponente(self, ruta):
        ruta_carta = cargar_datos(f"{ruta}")
        pixeles4 = QPixmap(ruta_carta)
        self.label_carta_elegida_contricante.setPixmap(pixeles4)
        self.label_carta_elegida_contricante.setScaledContents(True)

    def siguiente_ronda(self):
        if self.estado_siguiente_ronda == False:
            ruta_carta = cargar_datos("RUTA_BACK_CARTA")
            pixeles4 = QPixmap(ruta_carta)
            self.label_carta_elegida.setPixmap(pixeles4)
            self.label_carta_elegida.setScaledContents(True)
            self.label_carta_elegida_contricante.setPixmap(pixeles4)
            self.label_carta_elegida_contricante.setScaledContents(True)
            self.label_texto.setText("")
            self.label_cuadro.hide()
            self.label_cuadro1.hide()
            self.label_texto.hide()
            self.carta_seleccionada = None
            self.seleccion_carta_bool = False
            self.seleccion_mazo_triunfo = False
            self.senal_siguiente_ronda.emit("siguiente")
            self.estado_siguiente_ronda = True
    def volver_ventana_inicio(self):
        pass