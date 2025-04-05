from machine import Pin
from myKeyboardCLASSIC import Caracteres
import time
#import pantallas

class teclado:
    strLastKey="Inicio"
    def __init__(self):
        self.ta = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            import uos
            HOSTTYPE = uos.uname()[4]
            if HOSTTYPE== 'GALDEANO M5 DEV with ESP32':
                import tecladoM5
                cls.instance = tecladoM5.teclado()
            elif HOSTTYPE== 'GALDEANO CLASSIC DEV with ESP32':
                import tecladoCLASSIC
                cls.instance =tecladoCLASSIC.teclado()
            elif HOSTTYPE== 'GALDEANO CIVER with ESP32S3':
                import tecladoCIVER
                cls.instance =tecladoCIVER.teclado()
            super(teclado, cls).__new__(cls)
        return cls.instance

    