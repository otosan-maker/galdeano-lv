import lvgl as lv
import json
import teclado
import network
import guiHeader

class guiBase():
    def __init__(self):
        self.ta = None
        self.miCabecera = guiHeader.guiHeader()
    
    def clearScreen(self):
        obj=lv.scr_act()
        obj.clean()

    def ta_event_cb(self,e,kb):
        code = e.get_code()
        ta = e.get_target()
        if code == lv.EVENT.FOCUSED:
            kb.taWidget=ta
        if code == lv.EVENT.DEFOCUSED:
            kb.taWidget=None

    def execScreen(self):
        self.miCabecera.strTitle="GUI BASE"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("execScreen BASE")
        label.center()
    
    def execScreenConf(self):
        label = lv.label(lv.scr_act())
        label.set_text("execScreenConf")
        label.center()

