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
    
    def emathp_exe(self,e,ta,label):
        label.set_text(eigenmath.run(ta.get_text()) )
    

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
        ta = lv.textarea(lv.scr_act())
        ta.align(lv.ALIGN.TOP_LEFT, 0, 23)
        ta.set_one_line(True)
        ta.set_width(319)
        ta.set_placeholder_text( "Escribe aqui")
        ta.add_state(lv.STATE.FOCUSED)
        ta.add_style(styleTAInput, 0)
        miTeclado.taWidget=ta
        
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
        label.set_text("")
        miTeclado.outputWidget=label
        miTeclado.execFunc = lambda e: self.emathp_exe(e,ta,label)
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("CLS")
        btn1.add_event_cb(lambda e: gal.cls(e,ta,label), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("Funct")
        btn2.add_event_cb(lambda e: gal.dic(e,ta,btn2) , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "Trigon" )
        btn3.add_event_cb(lambda e: gal.trig2(e,ta), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("Exec")
        btn4.add_event_cb(lambda e: self.emathp_exe(e,ta,label), lv.EVENT.CLICKED, None)
    
    def execScreenConf(self):
        self.miCabecera.strTitle="Galdeano CAS"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("execScreenConf OBJ1")
        label.center()
