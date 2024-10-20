import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase

#####################################
#             Help
#####################################



class guiObj4(guiBase):
    def __init__(self):
        super().__init__()
    
    ta = None
    helpWidget = None
    helpFileName = None
    
    # window msg code
    btns = ["Close",  ""]
    def eMsgBox(self,e):
        mbox = e.get_current_target()
        self.mbox1.close()
    def exeButton(self,event,msgTxt):
        self.mbox1 = lv.msgbox(lv.scr_act(), "GPL License", msgTxt , self.btns, True)
        self.mbox1.add_event_cb(self.eMsgBox, lv.EVENT.VALUE_CHANGED, None)
        self.mbox1.center()
    
    def findDef(self,event,hfn):
        #looking for function name
        hfn = "/help/"+self.ta.get_text()
        hfn = hfn.replace('(','')
        hfn = hfn.replace(')','')
        hfn = hfn + ".help"
        try:
            with open(hfn,'r') as f:
                helpData = f.read()
            self.helpWidget.set_text(helpData)
            f.close()
        except:
            self.helpWidget.set_text("No help for this funtion")
        
        
    
    #DEMO screen code
    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Help for Eigenmath"
        self.miCabecera.setHeader()        
        
        
        
        self.ta = lv.textarea(lv.scr_act())
        self.ta.align(lv.ALIGN.TOP_LEFT, 0, 23)
        self.ta.set_one_line(True)
        self.ta.set_width(319)
        self.ta.set_placeholder_text( "funtion name to get help")
        self.ta.add_state(lv.STATE.FOCUSED)
        self.ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
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
        self.helpWidget = lv.label(obj)
        self.helpWidget.set_text("Write the name of the function\n and press exe to get an explanation\n of this function.\n\n More help in:\nhttps://georgeweigt.github.io/")
        miTeclado.outputWidget=self.helpWidget
        
        # we will exec this function when we press exe button
        miTeclado.execFunc = lambda e: self.findDef(e,self.helpFileName) 
        
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("CLS")
        btn1.add_event_cb(lambda e: self.cls(e,self.ta,self.helpWidget), lv.EVENT.CLICKED, None)
        #btn1.add_event_cb(lambda e:self.exeButton(e,"graphic button 1 pressed"), lv.EVENT.CLICKED, None)
        
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
        label_btn3.set_text( "Licen" )
        btn3.add_event_cb(lambda e:self.exeButton(e,"This calculator is open hardware.\nCreated by Otosan-Maker"), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("Exec")
        btn4.add_event_cb(lambda e: self.findDef(e,self.helpFileName), lv.EVENT.CLICKED, None)
            
    
    def execScreenConf(self):
        self.miCabecera.strTitle="DEMO"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("configuration screen DEMO")
        label.center()

