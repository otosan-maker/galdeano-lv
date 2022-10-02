import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase
import lvgl as lv
import eigenmath
import galdeanolib as gal
import os

class guiObj3(guiBase):
    def __init__(self):
        super().__init__()
    
    
    file_name = ""
    edit_file_name = True
    cont_col2 = None
    
    def enter(self,e,mta):
        mta.add_text("\n")



    def openFile(self,e):
        self.cont_col2
        self.file_name
        obj2  = e.get_target()
        self.file_name = '/data/'+str(obj2.get_child(0).get_text())
        datafile = open(self.file_name)
        self.ta.set_text(datafile.read())
        datafile.close()
        self.cont_col2.delete()

    def abre(self,e):
        dicVal = os.listdir("data")
        self.cont_col2
        col_dsc = [200, lv.GRID_TEMPLATE.LAST]
        row_dsc = [20]
        for i in range(len(dicVal)):
            row_dsc.append(20)
        row_dsc.append(lv.GRID_TEMPLATE.LAST)
        # Create a container with COLUMN flex direction
        self.cont_col2 = lv.obj(lv.scr_act())
        self.cont_col2.move_foreground()
        self.cont_col2.set_size(250, 150)
        self.cont_col2.align(lv.ALIGN.TOP_LEFT, 0, 50)
        self.cont_col2.set_grid_dsc_array(col_dsc, row_dsc)
        for index,item in enumerate(dicVal):
            obj = lv.btn(self.cont_col2)
            obj.set_grid_cell(lv.GRID_ALIGN.STRETCH, 0, 1,lv.GRID_ALIGN.STRETCH, index, 1)
            obj.add_event_cb(self.openFile, lv.EVENT.CLICKED, None)
            label = lv.label(obj)
            label.set_text(item)
            label.center()



    def guarda(self,e):
        self.file_name
        self.edit_file_name
        if(self.file_name!=""):
            if(self.ta.get_text()!=""):
                fichero = open(self.file_name,"w")
                fichero.write(self.ta.get_text())
                fichero.close()
            else:
                os.remove(self.file_name)
        else:
            print("con que nombre")
            if(self.edit_file_name):
                self.ta2=lv.textarea(lv.scr_act())
                self.ta2.align(lv.ALIGN.TOP_LEFT, 3, 160)
                self.ta2.set_one_line(True)
                self.ta2.set_width(310)
                self.ta2.set_placeholder_text( "File Name")
                miTeclado = teclado.teclado()
                miTeclado.taWidget=self.ta2
                self.ta2.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
                self.ta2.add_state(lv.STATE.FOCUSED)
                self.edit_file_name=False
            else:
                if(self.ta.get_text()!=""):
                    self.file_name="/data/"+self.ta2.get_text()+".txt"
                    self.ta2.delete()
                    if(self.ta.get_text()!=""):
                        fichero = open(self.file_name,"w")
                        fichero.write(self.ta.get_text())
                        fichero.close()
                    else:
                        os.remove(self.file_name)
    
    def event_msgBox(self,e):
        mbox = e.get_current_target()
        print("Button %s clicked" % mbox.get_active_btn_text())

    def com(self,e):
        btns = [""]
        
        if(self.file_name==""):
            mbox1 = lv.msgbox(lv.scr_act(), "Exec File", "Primero tienes que guardar el fichero", btns, True)
            mbox1.add_event_cb(self.event_msgBox, lv.EVENT.VALUE_CHANGED, None)
            mbox1.center()
        else:
            fileout_name="/data/out.txt"
            fichero = open(fileout_name,"w")
            x=self.ta.get_text().split('\n')
            for line in x:
                fichero.write(eigenmath.run(line ))
            fichero.close()
            mbox1 = lv.msgbox(lv.scr_act(), "Fichero", "guardado out.txt", btns, True)
            mbox1.add_event_cb(self.event_msgBox, lv.EVENT.VALUE_CHANGED, None)
            mbox1.center()
            

    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Galdeano Editor"
        self.miCabecera.setHeader()
        
        styleTAInput = lv.style_t()
        styleTAInput.init()
        styleTAInput.set_pad_top(0)
        styleTAInput.set_text_font(lv.galdeano_14)
        self.ta = lv.textarea(lv.scr_act())
        self.ta.align(lv.ALIGN.TOP_LEFT, 0, 23)
        self.ta.set_size(319,185)
        self.ta.set_placeholder_text( "Text editor")
        self.ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        self.ta.add_state(lv.STATE.FOCUSED)
        self.ta.add_style(styleTAInput, 0)
        miTeclado.taWidget=self.ta
        miTeclado.execFunc = lambda e: self.enter(e,self.ta)
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 2, 212)
        btn1.set_size(65,25)
        label_btn1 = lv.label(btn1)
        label_btn1.set_text("Open")
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        btn1.add_event_cb(self.abre, lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 71, 212)
        btn2.set_size(65,25)
        label_btn2 = lv.label(btn2)
        label_btn2.set_text("Save")
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        btn2.add_event_cb(self.guarda, lv.EVENT.CLICKED, None)

        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 138, 212)
        btn3.set_size(65,25)
        label_btn3 = lv.label(btn3)
        label_btn3.set_text( "Com" )
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        btn3.add_event_cb(self.com, lv.EVENT.CLICKED, None)

        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 206, 212)
        btn4.set_size(53,25)
        label_btn4 = lv.label(btn4)
        label_btn4.set_text("Fun")
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        btn4.add_event_cb(lambda e: self.dic(e,self.ta,btn4), lv.EVENT.CLICKED, None)

        btn5 = lv.btn(lv.scr_act())
        btn5.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 261, 212)
        btn5.set_size(55,25)
        label_btn5 = lv.label(btn5)
        label_btn5.set_text("CLS")
        label_btn5.align_to(btn5, lv.ALIGN.TOP_LEFT, 0, -4)
        btn5.add_event_cb(lambda e: self.cls(e,self.ta,None), lv.EVENT.CLICKED, None)

        
    
    def execScreenConf(self):
        self.miCabecera.strTitle="Galdeano Editor"
        self.miCabecera.setHeader()
        label = lv.label(lv.scr_act())
        label.set_text("execScreenConf Editor")
        label.center()
