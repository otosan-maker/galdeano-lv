import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase
from imagetools import get_png_info, open_png

    

#####################################
#             demo
#####################################



class guiObj0(guiBase):
    def __init__(self):
        super().__init__()
    
    # window msg code
    btns = ["Close",  ""]
    def eMsgBox(self,e):
        mbox = e.get_current_target()
        self.mbox1.close()
    def exeButton(self,event,msgTxt):
        self.mbox1 = lv.msgbox(lv.scr_act(), "MSG", msgTxt , self.btns, True)
        self.mbox1.add_event_cb(self.eMsgBox, lv.EVENT.VALUE_CHANGED, None)
        self.mbox1.center()


    #DEMO screen code
    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="DEMO"
        self.miCabecera.setHeader()        
        
        
        
        ta = lv.textarea(lv.scr_act())
        ta.align(lv.ALIGN.TOP_LEFT, 0, 25)
        ta.set_one_line(True)
        ta.set_width(300)
        ta.set_placeholder_text( "producto")
        ta.add_state(lv.STATE.FOCUSED)
        ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        miTeclado.taWidget=ta
        
        style = lv.style_t()
        style.init()
        style.set_text_font(lv.galdeano_14)
        
        
        # Register PNG image decoder
        decoder = lv.img.decoder_create()
        decoder.info_cb = get_png_info
        decoder.open_cb = open_png
        try:
            with open('/img/otosan.png','rb') as f:
                png_data = f.read()
            img_otosan = lv.img_dsc_t({
              'data_size': len(png_data),
              'data': png_data 
            })
            img1 = lv.img(lv.scr_act())
            img1.set_src(img_otosan)
            img1.align(lv.ALIGN.TOP_LEFT, 0, 65)
            img1.set_size(201, 140)
        except:
            print("Could not find otosan.png")
            labelGaldeano = lv.label(lv.scr_act())
            labelGaldeano.set_text("GALDEANO")
            labelGaldeano.align(lv.ALIGN.TOP_LEFT, 10, 65)
            
            
        

        
        
        labelVersion = lv.label(lv.scr_act())
        labelVersion.set_text("Firmware 1.0")
        labelVersion.align(lv.ALIGN.TOP_LEFT, 205, 65)
        
        labelVersion2 = lv.label(lv.scr_act())
        labelVersion2.set_text("uPython 19")
        labelVersion2.align(lv.ALIGN.TOP_LEFT, 205, 85)
        
        # we will exec this function when we press exe button
        miTeclado.execFunc = lambda e: self.exeButton(e,"exec button pressed")
        
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("btn1")
        btn1.add_event_cb(lambda e:self.exeButton(e,"graphic button 1 pressed"), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("btn2")
        btn2.add_event_cb(lambda e: self.exeButton(e,"graphic button 2 pressed") , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "" )
        #btn3.add_event_cb(lambda e: gal.trig2(e,ta), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("")
        #btn4.add_event_cb(lambda e: emathp_exe(e,ta,label), lv.EVENT.CLICKED, None)
            
    
    def execScreenConf(self):
        self.miCabecera.strTitle="DEMO"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("configuration screen DEMO")
        label.center()
