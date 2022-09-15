import lvgl as lv
import json
import teclado
import network


class guiHeader:
    
    strTitle=""
    miTeclado = teclado.teclado()
    sta_if = network.WLAN(network.STA_IF)
    
    styleHeader = None
    
    objHeader   = None
    titulo      = None
    modeLabel   = None
    cntLabel    = None
    wifiLabel   = None
    
    def __init__(self):
        self.ta = None
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(guiHeader, cls).__new__(cls)
        return cls.instance

    def setHeader(self):
        self.objHeader = lv.obj(lv.scr_act())
        self.objHeader.set_size(320, 22)
        self.objHeader.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 0, 0)
        
        self.styleHeader = lv.style_t()
        self.styleHeader.init()
        self.styleHeader.set_bg_color(lv.color_hex(0xE0E0FF))
        self.styleHeader.set_pad_top(0)
        self.styleHeader.set_pad_bottom(0)
        self.styleHeader.set_radius(0)
        self.objHeader.add_style(self.styleHeader, 0)
            
        self.titulo=lv.label(self.objHeader)
        self.titulo.align_to(self.objHeader, lv.ALIGN.TOP_LEFT, 65, 0)
        self.titulo.set_text(self.strTitle)
        self.modeLabel=lv.label(self.objHeader)
        self.modeLabel.align_to(self.objHeader, lv.ALIGN.TOP_LEFT, 1, 0)
        self.modeLabel.set_text( self.miTeclado.getModeString() )
        self.miTeclado.modeWidget=self.modeLabel
        
        self.cntLabel=lv.label(self.objHeader)
        self.cntLabel.align_to(self.objHeader, lv.ALIGN.TOP_LEFT, 240, 0)
        self.cntLabel.set_text(self.miTeclado.getCntString())
        self.miTeclado.cntWidget=self.cntLabel
        
        self.wifiLabel=lv.label(self.objHeader)
        self.wifiLabel.align_to(self.objHeader, lv.ALIGN.TOP_LEFT, 270, 0)
        self.setWifi()
        

    def setWifi(self):
        if self.wifiLabel==None:
            return
        if self.sta_if.isconnected():
            self.wifiLabel.set_text(lv.SYMBOL.WIFI)
        else:
            self.wifiLabel.set_text("")
        return