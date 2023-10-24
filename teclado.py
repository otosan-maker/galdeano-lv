from machine import Pin
from myKeyboard import Caracteres
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

    F1 = Pin(25, Pin.OUT)
    F2 = Pin(26, Pin.OUT)
    F3 = Pin(27, Pin.OUT)
    F4 = Pin(14, Pin.OUT)
    F5 = Pin(12, Pin.OUT)
    F6 = Pin(13, Pin.OUT)

    F1.off()
    F2.off()
    F3.off()
    F4.off()
    F5.off()
    F6.off()

    C1 = Pin(34, Pin.IN, Pin.PULL_DOWN)
    C2 = Pin(35, Pin.IN, Pin.PULL_DOWN)
    C3 = Pin(32, Pin.IN, Pin.PULL_DOWN)
    C4 = Pin(33, Pin.IN, Pin.PULL_DOWN)
    C5 = Pin(22, Pin.IN, Pin.PULL_DOWN)
    C6 = Pin(39, Pin.IN, Pin.PULL_DOWN)
    C7 = Pin(36, Pin.IN, Pin.PULL_DOWN)





    modeLabelTxt=["Num","alp","ALP"]
    
    Columns = [ C1, C2, C3, C4, C5, C6 , C7]
    Files = [ F1, F2, F3, F4, F5, F6]

    idMode=0
    idCntl=False
    
    taWidget    = None
    modeWidget  = None
    cntWidget   = None
    groupWidget = None
    outputWidget= None
    execFunc    = None
    ObjActive   = None
    graphCursor = None  #gestiona los cursores en modo grafico
    selectMenuFunc = None

    keyTimeout=1000
    
    #obtener la tecla
    def get_key(self):
        strValue=""
        keyPressed=0
        
        for idFil,file in enumerate( self.Files):
            file.on()
            for idCol,col in enumerate(self.Columns):
                if col.value() == 1:
                    strValue=Caracteres[self.idMode][idFil][idCol]
                    keyPressed=time.ticks_ms()
                    #print("tecla F:"+str(idFil)+" C:"+str(idCol))
            file.off()
        
        if (strValue == self.strLastKey):
            #print("self.lastKeyPressed-keyPressed: "+str( self.lastKeyPressed-keyPressed )+" keyTimeout: "+str( self.keyTimeout ))
            if  (keyPressed-self.lastKeyPressed<self.keyTimeout):
                return ""
            else:
                #print("key: "+strValue+" keyTimeout: "+str( self.keyTimeout ))
                self.keyTimeout=200
                return strValue
        else:
            #print("return key:"+strValue)
            self.keyTimeout=1000
            self.strLastKey=strValue
            self.lastKeyPressed=keyPressed
            return strValue
        
        
    #bucle para actualizar el textArea, hay que definir un timer
    def key_loop(self):
        c = self.get_key()
        if(c!=""):
            if(c=="menu"):
                if self.selectMenuFunc != None:
                    self.selectMenuFunc()
            elif(c=="cnt"):
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
            elif(c=="mode"):
                self.idMode=self.idMode+1
                if (self.idMode>2):
                    self.idMode=0
                if self.modeWidget!=None:
                    self.modeWidget.set_text(self.modeLabelTxt[self.idMode])
            elif( (c=="exe") or ( c=="eval")):
                    self.execFunc(1)
            else:
                #si estoy en modo grafico gestiono el cursor con la funcion que nos ha registrado
                if self.graphCursor != None:
                    self.graphCursor(c)
                #si no hay un textarea seleccionado no permitimos escribir
                if self.taWidget==None:
                    return
                if(c=="left"):
                    self.taWidget.cursor_left()
                elif(c=="rigth"):
                    self.taWidget.cursor_right()
                elif(c=="up"):
                    self.taWidget.cursor_up()
                elif(c=="down"):
                    self.taWidget.cursor_down()
                elif(c=="del"):
                    self.taWidget.del_char()
                else:
                    self.taWidget.add_text(c) 
    
    #obtenemos el estado del teclado
    def getModeString(self):
        return self.modeLabelTxt[self.idMode]
    
    def getCntString(self):
        if self.idCntl:
           return "cnt"
        else:
            return ""