import time
#import pantallas

class teclado:
    strLastKey="Inicio"
    def __init__(self):
        self.ta = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(teclado, cls).__new__(cls)
        return cls.instance
    
    
    modeLabelTxt=["Num","alp","ALP"]
    
    i2c = None

    idMode=0
    idCntl=False
    
    taWidget    = None
    modeWidget  = None
    cntWidget   = None
    groupWidget = None
    outputWidget= None
    execFunc    = None
    selectMenuFunc = None
    graphCursor = None  #gestiona los cursores en modo grafico
    
    keyTimeout=1000
    
    
    #obtener la tecla
    def get_key(self):
        return b'\x00'
        
        
    #bucle para actualizar el textArea, hay que definir un timer
    def key_loop(self):
        print(".")

    #obtenemos el estado del teclado
    def getModeString(self):
        return self.modeLabelTxt[self.idMode]
    
    def getCntString(self):
        if self.idCntl:
           return "cnt"
        else:
            return ""
