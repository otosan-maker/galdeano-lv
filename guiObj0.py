import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase

    

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
        self.mbox1 = lv.msgbox(lv.screen_active(), "MSG", msgTxt , self.btns, True)
        self.mbox1.add_event_cb(self.eMsgBox, lv.EVENT.VALUE_CHANGED, None)
        self.mbox1.center()


    #DEMO screen code
    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="DEMO"
        self.miCabecera.setHeader()        
        
        
        
        ta = lv.textarea(lv.screen_active())
        ta.align(lv.ALIGN.TOP_LEFT, 0, 25)
        ta.set_one_line(True)
        ta.set_width(300)
        ta.set_placeholder_text( "producto")
        ta.add_state(lv.STATE.FOCUSED)
        ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        miTeclado.taWidget=ta
        
        style = lv.style_t()
        style.init()
        #style.set_text_font(lv.galdeano_14)
        
        
        # Register PNG image decoder
        #decoder = lv.img.decoder_create()

        
        print("Could not find otosan.png")
        labelGaldeano = lv.label(lv.screen_active())
        labelGaldeano.set_text("GALDEANO")
        labelGaldeano.align(lv.ALIGN.TOP_LEFT, 10, 65)

        
        labelVersion = lv.label(lv.screen_active())
        labelVersion.set_text("Firmware 2.0")
        labelVersion.align(lv.ALIGN.TOP_LEFT, 205, 65)
        
        labelVersion2 = lv.label(lv.screen_active())
        labelVersion2.set_text("uPython 24")
        labelVersion2.align(lv.ALIGN.TOP_LEFT, 205, 85)
        
        # we will exec this function when we press exe button
        miTeclado.execFunc = lambda e: self.exeButton(e,"exec button pressed")
        
        
        btn1 = lv.button(lv.screen_active())
        btn1.align_to(lv.screen_active(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("btn1")
        btn1.add_event_cb(lambda e:self.exeButton(e,"graphic button 1 pressed"), lv.EVENT.CLICKED, None)
        
        btn2 = lv.button(lv.screen_active())
        btn2.align_to(lv.screen_active(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("btn2")
        btn2.add_event_cb(lambda e: self.exeButton(e,"graphic button 2 pressed") , lv.EVENT.CLICKED, None)
        
        btn3 = lv.button(lv.screen_active())
        btn3.align_to(lv.screen_active(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "" )
        #btn3.add_event_cb(lambda e: gal.trig2(e,ta), lv.EVENT.CLICKED, None)
        
        btn4 = lv.button(lv.screen_active())
        btn4.align_to(lv.screen_active(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("")
        #btn4.add_event_cb(lambda e: emathp_exe(e,ta,label), lv.EVENT.CLICKED, None)
            
    
    def execScreenConf(self):
        self.miCabecera.strTitle="DEMO"
        self.miCabecera.setHeader()
        label = lv.label(lv.screen_active())
        label.set_text("configuration screen DEMO")
        label.center()
