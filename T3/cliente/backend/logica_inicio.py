
from PyQt5.QtCore import QObject, pyqtSignal

# cambiar a la logica en el escritorio del servidor



class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool)
    senal_abrir_ventana_principal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()


    def comprobar_usuario(self, usuario):

        print(f"diccionario {usuario}")
        print(usuario["usuario"])
        if usuario["usuario"].isalnum() == True:

             self.senal_respuesta_validacion.emit(True)
             self.senal_abrir_ventana_principal.emit(usuario)
        if usuario["usuario"].isalnum() == False:
            self.senal_respuesta_validacion.emit(False)

