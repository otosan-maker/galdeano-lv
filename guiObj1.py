import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase
import eigenmath
import galdeanolib as gal

class guiObj1(guiBase):
    def __init__(self):
        super().__init__()
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(guiObj1, cls).__new__(cls)
        return cls.instance
    
    
    cmdList  = []
    cmdIndex = 0
    
    taText = ''
    labelText=''
    ta = None
    
    def emathp_exe(self,e,ta,label):
        if ( ta.get_text() == ''):
            return
        self.labelText = ">>> "+ ta.get_text() +"\n" + eigenmath.run(ta.get_text()) +"\n" + label.get_text()
        label.set_text( self.labelText )
        self.cmdList.append(ta.get_text())
        self.cmdIndex+=1
        ta.set_text("")
        taText = ''
    
    def tecladoCalc(self,key,ta,label):
        if(key=='down'):
            if (self.cmdIndex>0):
                self.cmdIndex-=1
            else:
                self.cmdIndex=len(self.cmdList)-1
            ta.set_text(self.cmdList[self.cmdIndex])
        if(key=='up'):
            if (self.cmdIndex<len(self.cmdList)-1):
                self.cmdIndex+=1
            else:
                self.cmdIndex=0
            ta.set_text(self.cmdList[self.cmdIndex])
        

    def execScreen(self):
        miTeclado = teclado.teclado()
        import pantallas
        miTeclado.selectMenuFunc=pantallas.select
        
        #Interfaz grafico
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Galdeano CAS"
        self.miCabecera.setHeader()

        styleTAInput = lv.style_t()
        styleTAInput.init()
        #styleTAInput.set_bg_color(lv.color_hex(0xF0F0FF))
        styleTAInput.set_pad_top(0)
        #styleTAInput.set_pad_bottom(8)
        self.ta = lv.textarea(lv.scr_act())
        self.ta.align(lv.ALIGN.TOP_LEFT, 0, 23)
        self.ta.set_one_line(True)
        self.ta.set_width(319)
        self.ta.set_placeholder_text( 'write here' )
        if self.taText!= '':
            self.ta.set_text( self.taText )
        self.ta.add_state(lv.STATE.FOCUSED)
        self.ta.add_style(styleTAInput, 0)
        miTeclado.taWidget=self.ta
        
        style = lv.style_t()
        style.init()
        style.set_pad_top(2)
        style.set_pad_left(4)
        style.set_text_font(lv.galdeano_14)
        obj = lv.obj(lv.scr_act())
        obj.set_size(319, 155)
        obj.align(lv.ALIGN.TOP_LEFT, 0, 55)
        obj.add_style(style, 0)
        label = lv.label(obj)
        label.set_text(self.labelText)
        miTeclado.outputWidget=label
        miTeclado.execFunc = lambda e: self.emathp_exe(e,self.ta,label)
        miTeclado.graphCursor = lambda e: self.tecladoCalc(e,self.ta,label)
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("CLS")
        btn1.add_event_cb(lambda e: self.cls(e,self.ta,label), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("Funct")
        btn2.add_event_cb(lambda e: self.dic(e,self.ta,btn2) , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "Trigon" )
        btn3.add_event_cb(lambda e: self.trig2(e,self.ta), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("Exec")
        btn4.add_event_cb(lambda e: self.emathp_exe(e,self.ta,label), lv.EVENT.CLICKED, None)
    
    def execScreenConf(self):
        self.miCabecera.strTitle="Galdeano CAS"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("execScreenConf OBJ1")
        label.center()

    def clearScreen(self):
        if self.ta!=None:
            self.taText = self.ta.get_text()
        super().clearScreen()
        self.ta=None

        