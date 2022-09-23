import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase
import comunication
import math
import errorMsgBox as error


#####################################
#             PESO
#####################################

class guiObj6(guiBase):
    def __init__(self):
        super().__init__()
    
    valores5=None


    def get_peso(self,e,lbl):
        self.valores5 = comunication.getPesoService()
        #print(valores5)
        texto=""
        for valores in self.valores5:
            texto = texto + valores['t_medida'][0:10] + '\t' + "{:.1f}".format(valores['peso']) + '\n'
        lbl.set_text( texto )

    def calStd(self,e,lbl,lblStd):
        if self.valores5==None:
            get_peso(e,lbl)
        suma=0
        for valores in self.valores5:
            suma = suma + valores['peso']
        incremento=self.valores5[-1]['peso'] - self.valores5[0]['peso']
        texto = "Media: "+"{:.2f}".format(suma/len(self.valores5)) +"\n\nEvolucion:"+"{:.2f}".format(incremento)
        lblStd.set_text(texto)
        if incremento <0:
            lblStd.set_style_text_color(lv.color_hex(0xFF0000),0)
        else:
            lblStd.set_style_text_color(lv.color_hex(0x329C58),0)

    def peso_exe(self,e,ta):
        comunication.altaPesoService(ta.get_text())
        ta.set_text("Msg sent")
        

    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Peso"
        self.miCabecera.setHeader()
        if not comunication.sta_if.isconnected():
            error.errorMsgBox("First starts Wifi")
            return
        
        ta = lv.textarea(lv.scr_act())
        ta.align(lv.ALIGN.TOP_LEFT, 0, 30)
        ta.set_one_line(True)
        ta.set_width(160)
        ta.set_placeholder_text( "peso")
        ta.add_state(lv.STATE.FOCUSED)
        miTeclado.taWidget=ta
        ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        miTeclado.execFunc = lambda e: self.peso_exe(e,ta)
        
        lbl = lv.label(lv.scr_act())
        lbl.set_size(160, 155)
        lbl.align(lv.ALIGN.TOP_LEFT, 10, 70)
        lbl.set_text("")
        
        lblStd = lv.label(lv.scr_act())
        lblStd.align(lv.ALIGN.TOP_LEFT, 165, 70)
        lblStd.set_text("")
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("Exe")
        btn1.add_event_cb(lambda e: self.peso_exe(e,ta), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("Last 7")
        btn2.add_event_cb(lambda e: self.get_peso(e,lbl) , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "Std" )
        btn3.add_event_cb(lambda e: self.calStd(e,lbl,lblStd), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text(" ")
        #btn4.add_event_cb(lambda e: emathp_exe(e,ta,label), lv.EVENT.CLICKED, None)


        
        
    
    def execScreenConf(self):
        self.miCabecera.strTitle="Peso"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("execScreenConf peso")
        label.center()
