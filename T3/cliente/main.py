import sys

from Conexiones import DCC

if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook
    juego = DCC(sys.argv)

    juego.iniciar()
    sys.exit(juego.exec())
