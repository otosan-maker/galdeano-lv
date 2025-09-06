from machine import Pin
from myKeyboardCIVER import Caracteres
import time
#import pantallas


class teclado:
    def __init__(self):
        self.ta = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(teclado, cls).__new__(cls)
        return cls.instance

    F1 = Pin(02, Pin.OUT)
    F2 = Pin(04, Pin.OUT)
    F3 = Pin(06, Pin.OUT)
    F4 = Pin(07, Pin.OUT)
    F5 = Pin(03, Pin.OUT)
    F6 = Pin(21, Pin.OUT)
    F7 = Pin(47, Pin.OUT)
    
    F1.off()
    F2.off()
    F3.off()
    F4.off()
    F5.off()
    F6.off()
    F7.off()
    
    C1 = Pin(05, Pin.IN, Pin.PULL_DOWN)
    C2 = Pin(38, Pin.IN, Pin.PULL_DOWN)
    C3 = Pin(39, Pin.IN, Pin.PULL_DOWN)
    C4 = Pin(40, Pin.IN, Pin.PULL_DOWN)
    C5 = Pin(41, Pin.IN, Pin.PULL_DOWN)
    C6 = Pin(18, Pin.IN, Pin.PULL_DOWN)
    C7 = Pin(42, Pin.IN, Pin.PULL_DOWN)

    modeLabelTxt=["Math","alp","ALP"]
    
    Columns = [ C1, C2, C3, C4, C5, C6 , C7]
    Files = [ F1, F2, F3, F4, F5, F6, F7]
    shift_key  =(0,3)
    alt_key    =(5,0)
    idMode=1
    idCntl=False
    
    taWidget    = None  # el textarea donde escribimos los caracteres
    modeWidget  = None	# textarea (del header) donde ponemos en que modo esta el teclado
    cntWidget   = None  # textarea (del header) donde ponemos que estamos en la pantalla de cfg
    execFunc    = None  # la funcion que ejecutamos cuando pulsamos exec
    ObjActive   = None	# la pantalla que estamos usando, para poder poner el modo cfg
    graphCursor = None  # gestiona los cursores en modo grafico
    selectMenuFunc = None # la funcion que llamamos cuando vamos al lanzador
    strLastKey  =  ['a']
    lastKeyPressed = 0
    keyPressed = 0
    keyTimeout=500
    
    # obtenemos las coordenadas de los botones pulsados
    def get_switch(self):
        interruptores = [""]
        for idFil,file in enumerate( self.Files):
            file.on()
            for idCol,col in enumerate(self.Columns):
                if col.value() == 1:
                    interruptores.append((idFil,idCol))
                    self.keyPressed=time.ticks_ms()
                    #print("tecla F:"+str(idFil)+" C:"+str(idCol))
            file.off()
        return interruptores
    
    
    #una funciona auxiliar que saca el caracter de la lista de botones pulsados y
    # lo transforma en un caracter.
    def get_char(self,listKeyCoord):
        if (self.shift_key in listKeyCoord):
            listKeyCoord.remove(self.shift_key)
            b=listKeyCoord.pop()
            if b == "":
                return ""
            else:
                return Caracteres[2][b[0]][b[1]]
        elif (self.alt_key in listKeyCoord):
            listKeyCoord.remove(self.alt_key)
            b=listKeyCoord.pop()
            if b == "":
                return ""
            else:
                return Caracteres[3][b[0]][b[1]]
        b=listKeyCoord.pop()
        if b == "":
            return ""
        else:
            return Caracteres[self.idMode][b[0]][b[1]]
        
    #obtener las tecla a partir de los botones
    #algunos botones pueden modificarlo, lo hacemos aqui.
    def get_key(self):
        strValue=[""]
        strValue = self.get_switch()
        if (strValue == self.strLastKey):
            #print("lastKeyPressed: "+str( self.lastKeyPressed )+" keyPressed: "+str( self.keyPressed ))
            if  (self.keyPressed-self.lastKeyPressed<self.keyTimeout):
                return ""
            else:
                #print("2 lastKeyPressed: "+str( self.lastKeyPressed )+" keyPressed: "+str( self.keyPressed ))
                self.lastKeyPressed=self.keyPressed
                return self.get_char(strValue)
        else:
            self.strLastKey=strValue.copy()
            #print("2:")
            #print(strValue)
            #print(self.strLastKey)
            self.lastKeyPressed=self.keyPressed
            return self.get_char(strValue)

        
        
    #bucle para actualizar el textArea, hay que definir un timer
    def key_loop(self):
        c = ""
        c = self.get_key()
        #c = teclas.pop()
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
                    self.taWidget.delete_char()
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