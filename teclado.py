
class teclado:
    strLastKey="Inicio"
    def __init__(self):
        self.ta = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            import uos
            import sys
            if sys.platform == 'linux':
                import tecladoLinux
                cls.instance = tecladoLinux.teclado()
            else:
                HOSTTYPE = uos.uname()[4]
                if HOSTTYPE.find('GALDEANO M5')>=0:
                    import tecladoM5
                    cls.instance = tecladoM5.teclado()
                elif HOSTTYPE.find('GALDEANO CLASSIC')>=0:
                    import tecladoCLASSIC
                    cls.instance =tecladoCLASSIC.teclado()
                elif HOSTTYPE.find('GALDEANO CIVER')>=0:
                    import tecladoCIVER
                    cls.instance =tecladoCIVER.teclado()
            super(teclado, cls).__new__(cls)
        return cls.instance

    