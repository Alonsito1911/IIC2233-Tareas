from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from cliente_ import Client
from frontend.ventana_espera import VentanaEspera
import socket
from backend.logica_espera import LogicaEspera

class DCC(QApplication):

    def __init__(self, argv):
        super().__init__(argv)
        self.port = 55556
        self.host = socket.gethostname()


        self.ventana_inicio = VentanaInicio()
        self.ventana_espera = VentanaEspera()
        self.cliente = Client(self.port, self.host)
        self.ventana_juego = VentanaJuego()



        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaJuego()
        self.logica_espera = LogicaEspera()


        self.conectar_inicio()
        self.conectar_juego()
        self.conectar_principal()
        self.conectar_postjuego()

    def conectar_inicio(self):

        self.ventana_inicio.senal_enviar_usuario.connect(self.logica_inicio.comprobar_usuario)
        self.ventana_inicio.senal_enviar_usuario.connect(self.cliente.enviar)
        self.logica_inicio.senal_respuesta_validacion.connect(self.ventana_inicio.recibir_validacion)
        self.logica_inicio.senal_abrir_ventana_principal.connect(self.ventana_espera.mostrar_ventana)
        pass

    def conectar_principal(self):

        self.ventana_espera.senal_volver_inicio.connect(self.iniciar)
        self.ventana_espera.senal_volver_inicio.connect(self.cliente.enviar)
        self.cliente.senal_iniciar_thread.connect(self.logica_espera.iniciar_cuenta_regresiva)
        self.logica_espera.senal_enviar_numeros.connect(self.ventana_espera.cuenta_regresiva)
        self.logica_espera.senal_abrir_ventana_juego.connect(self.ventana_juego.init_gui)
        self.logica_espera.senal_otorgar_mazo.connect(self.cliente.enviar_senal_para_otorgar_mazos)
        self.cliente.senal_cambiar_label_nombre.connect(self.ventana_espera.cambiar_label_nombre)



    def conectar_juego(self):
        self.cliente.senal_cambiar_label_nombre_venta_juego.connect(self.ventana_juego.cambiar_label_nombre)
        self.cliente.senal_iniciar_thread_juego.connect(self.logica_juego.iniciar_cuenta_regresiva_logica_juego)
        self.logica_juego.senal_enviar_numeros_ventana_juego.connect(self.ventana_juego.cuenta_regresiva)
        self.cliente.senal_enviar5_cartas.connect(self.logica_juego.recibir_5_cartas)
        self.logica_juego.senal_enviar_rutas_cartas.connect(self.ventana_juego.actualizar_cartas)
        self.ventana_juego.senal_enviar_carta_seleccionada.connect(self.cliente.recibir_carta_seleccionada)
        self.logica_juego.senal_combate.connect(self.cliente.combate)
        self.cliente.senal_enviar_resultado.connect(self.ventana_juego.resultado)
        self.ventana_juego.senal_diferente_elemento.connect(self.cliente.eleccion_mazo_triunfos)
        self.ventana_juego.senal_mismo_elemento.connect(self.cliente.eleccion_mazo_triunfos)
        self.ventana_juego.senal_descartar_elemento.connect(self.cliente.eleccion_mazo_triunfos)
        self.ventana_juego.senal_siguiente_ronda.connect(self.cliente.siguiente_ronda)
        self.cliente.senal_enviar_ficha.connect(self.ventana_juego.actualizar_fichas)
        self.cliente.senal_enviar_resultado_partida.connect(self.ventana_juego.resultado)

        self.cliente.senal_enviar_carta_oponente.connect(self.ventana_juego.cambiar_label_carta_oponente)

    def conectar_postjuego(self):

        # self.logica_juego.senal_abrir_ventana_postronda.connect(self.ventana_postjuego.crear_elementos)
        pass


    def iniciar(self):
        self.ventana_inicio.show()
