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
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(guiObj3, cls).__new__(cls)
        return cls.instance
    
    file_name   = ""
    file_text   = ""
    ta          = None
    
    workingDir  = "prog"
    taDir       = None
    edit_file_name = True
    mDir = []
    cont_col2   = None
    
    def clearScreen(self):
        if self.ta != None:  # pasamos de la pantalla de edicion a la de configuracion
            self.file_text = self.ta.get_text()
            
        if self.taDir != None:  # pasamos de la pantalla de configuracion a la de  edicion
            cont_col2 = None
            pass
        super().clearScreen()
        
    def enter(self,e,mta):
        mta.add_text("\n")

    def openFile(self,e):
        obj2  = e.get_target()
        self.file_name = str(obj2.get_child(0).get_text())
        longFileName = '/'+self.workingDir+'/'+self.file_name
        datafile = open(longFileName)
        self.ta.set_text(datafile.read())
        datafile.close()
        self.cont_col2.delete()
        self.cont_col2=None

    def abre(self,e):
        if self.cont_col2 != None:
            self.cont_col2.delete()
            self.cont_col2=None
            return
        dicVal = os.listdir(self.workingDir)
        
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
        if(self.file_name!=""):
            if(self.ta.get_text()!=""):
                self.file_text=self.ta.get_text()
                self.saveText(self.file_name)
            else:
                longFileName = '/'+self.workingDir+'/'+self.file_name
                os.remove(longFileName)
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
                self.ta2.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
                self.ta2.add_state(lv.STATE.FOCUSED)
                self.edit_file_name=False
            else:
                if(self.ta.get_text()!=""):
                    self.file_name=self.ta2.get_text()
                    longFileName = '/'+self.workingDir+'/'+self.file_name
                    self.ta2.delete()
                    if(self.ta.get_text()!=""):
                        self.file_text=self.ta.get_text()
                        self.saveText(longFileName)
                    else:
                        os.remove(longFileName)
    
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
            fileout_name="/"+self.workingDir+"/out.txt"
            fichero = open(fileout_name,"w")
            x=self.ta.get_text().split('\n')
            for line in x:
                fichero.write(eigenmath.run(line ))
            fichero.close()
            mbox1 = lv.msgbox(lv.scr_act(), "Fichero", "guardado out.txt", btns, True)
            mbox1.add_event_cb(self.event_msgBox, lv.EVENT.VALUE_CHANGED, None)
            mbox1.center()
            

    def execScreen(self):
        self.taDir = None
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Editor"
        self.miCabecera.setHeader()
        
        styleTAInput = lv.style_t()
        styleTAInput.init()
        styleTAInput.set_pad_top(0)
        styleTAInput.set_text_font(lv.galdeano_14)
        self.ta = lv.textarea(lv.scr_act())
        self.ta.align(lv.ALIGN.TOP_LEFT, 0, 23)
        self.ta.set_size(319,185)
        self.ta.set_placeholder_text( "Text editor")
        if self.file_text != "":
            self.ta.set_text( self.file_text )
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

    def newDir(self,e,taDir,dd):
        path='/'+self.taDir.get_text()
        os.mkdir(path)
        self.scanDir(dd)

    def scanDir(self,dd):
        self.mDir.clear()
        for file in os.ilistdir('/'):
            if file[1]== 0x4000 :
                self.mDir.append(file[0])
        dd.set_options("\n".join(self.mDir))
        index=self.mDir.index(self.workingDir)
        dd.set_selected(index)
    
    def saveAs(self,e,ta):
        self.file_name=ta.get_text()
        longFileName  = '/'+self.workingDir+'/'+self.file_name
        self.saveText(longFileName)
        
    def saveText(self,longFileName):
        longFileName  = '/'+self.workingDir+'/'+self.file_name
        print("Guardamos fichero: "+ longFileName)
        fichero = open(longFileName,"w")
        fichero.write(self.file_text)
        fichero.close()
        self.file_name = longFileName
                
    def event_handler_DD(self,e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED: 
            self.workingDir = self.mDir[obj.get_selected()]
    
    def execScreenConf(self):
        miTeclado = teclado.teclado()
        self.miCabecera.strTitle="Editor"
        self.miCabecera.setHeader()
        self.ta = None
        miTeclado.taWidget=self.taDir
        
        
        label = lv.label(lv.scr_act())
        label.set_text("Working Dir: ")
        label.align(lv.ALIGN.TOP_LEFT, 2, 30)
        dd = lv.dropdown(lv.scr_act())
        #dd.set_options("\n".join(["data"]))
        self.scanDir(dd)
        dd.align(lv.ALIGN.TOP_LEFT, 130, 23)
        dd.add_event_cb(self.event_handler_DD, lv.EVENT.ALL, None)
        
        
        label = lv.label(lv.scr_act())
        label.set_text("File Name: ")
        label.align(lv.ALIGN.TOP_LEFT, 2, 70)
        self.taFileName = lv.textarea(lv.scr_act())
        self.taFileName.align(lv.ALIGN.TOP_LEFT, 110, 63)
        self.taFileName.set_width(200)
        self.taFileName.set_one_line(True)
        self.taFileName.set_text( self.file_name )
        self.taFileName.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        
        
        label = lv.label(lv.scr_act())
        label.set_text("Create Dir: ")
        label.align(lv.ALIGN.TOP_LEFT, 2, 110)
        self.taDir = lv.textarea(lv.scr_act())
        self.taDir.align(lv.ALIGN.TOP_LEFT, 110, 103)
        self.taDir.set_width(200)
        self.taDir.set_one_line(True)
        self.taDir.set_text( "" )
        self.taDir.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 2, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.set_text("")
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, -2, -4)
        #btn1.add_event_cb(self.setDir, lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, -4, -4)
        label_btn2.set_text("Save as")
        btn2.add_event_cb(lambda e: self.saveAs(e,self.taFileName) , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, -5, -4)
        label_btn3.set_text( "New Dir" )
        btn3.add_event_cb(lambda e: self.newDir(e,self.taDir,dd), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text(" ")
        #btn4.add_event_cb(lambda e: self.emathp_exe(e,self.ta,label), lv.EVENT.CLICKED, None)
