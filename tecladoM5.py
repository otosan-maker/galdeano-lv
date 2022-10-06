import  machine 
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
        if self.i2c != None :
            strValue=self.i2c.readfrom(0x08,1)
            return strValue
        else:
            return b'\x00'
        
        
    #bucle para actualizar el textArea, hay que definir un timer
    def key_loop(self):
        c = self.get_key()
        if(c!=b'\x00'):
            print(c)
            if(c==b'~'):
                if self.selectMenuFunc != None:
                    self.selectMenuFunc()
            elif(c==b'|'):
                if self.idCntl:
                    self.idCntl=False
                    if self.cntWidget!=None:
                        self.cntWidget.set_text("")
                    if self.ObjActive !=None:
                        self.ObjActive.clearScreen()
                        self.ObjActive.execScreen()
                else:
                    self.idCntl=True
                    if self.cntWidget!=None:
                        self.cntWidget.set_text("conf")
                    if self.ObjActive !=None:
                        self.ObjActive.clearScreen()
                        self.ObjActive.execScreenConf()
            elif(c==b'0x200'):
                self.idMode=self.idMode+1
                if (self.idMode>2):
                    self.idMode=0
                if self.modeWidget!=None:
                    self.modeWidget.set_text(self.modeLabelTxt[self.idMode])
            elif(  c==b'\n'):
                    self.execFunc(1)
            elif(  c==b'\r') :
                    pass
            else:
                #si estoy en modo grafico gestiono el cursor con la funcion que nos ha registrado
                if self.graphCursor != None:
                    self.graphCursor(c)
                #si no hay un textarea seleccionado no permitimos escribir
                if self.taWidget==None:
                    return
                if(c==b'\xbf'):
                    self.taWidget.cursor_left()
                    print("left")
                elif(c==b'\xc1'):
                    self.taWidget.cursor_right()
                elif(c==b'\xb7'):
                    self.taWidget.cursor_up()
                elif(c==b'\xc0'):
                    self.taWidget.cursor_down()
                elif(c==b'\x08'):
                    self.taWidget.del_char()
                else:
                    self.taWidget.add_text(c.decode()) 
    
    #obtenemos el estado del teclado
    def getModeString(self):
        return self.modeLabelTxt[self.idMode]
    
    def getCntString(self):
        if self.idCntl:
           return "cnt"
        else:
            return ""