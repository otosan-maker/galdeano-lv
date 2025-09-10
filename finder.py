import lvgl as lv
import json
import teclado
import guiHeader
import myAppMenu as appMenu
from guiBase import guiBase
import sys
    

#####################################
#             demo
#####################################



class finder(guiBase):
    def __init__(self):
        super().__init__()
    # window msg code
    btns = ["Close",  ""]
    
    lastAppExec = None
    
    def eMsgBox(self,e):
        mbox = e.get_current_target()
        self.mbox1.close()
    def exeButton(self,event,msgTxt):
        self.mbox1 = lv.msgbox(lv.screen_active())
        self.mbox1.add_title("Exec File")
        self.mbox1.add_text(msgTxt)
        self.mbox1.add_close_button()
        self.mbox1.add_event_cb(self.eMsgBox, lv.EVENT.VALUE_CHANGED, None)
        self.mbox1.center()

    def execApp(self,event,msgTxt):
        img = event.get_target_obj()
        txt = img.get_child(0).get_text()
        miTeclado = teclado.teclado()
        for pantalla in appMenu.Gal_pantallas:
            if pantalla['Name'] == txt:
                meGuiObj = pantalla['function']()
                if self.lastAppExec != None:
                    self.lastAppExec.clearScreen()
                else:
                    self.clearScreen()
                self.lastAppExec = meGuiObj
                miTeclado.ObjActive = meGuiObj
                meGuiObj.execScreen()
                
        
    def get_image_data(self,filename):
        with open(filename, 'rb') as f:
            imgdata = f.read()
        return imgdata
        
    def create_img_dsc(self,imgdata):
        imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
        return imgdsc

    #DEMO screen code
    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="FINDER"
        self.miCabecera.setHeader()        
        
        style = lv.style_t()
        style.init()
        style.set_text_font(lv.galdeano_14)
        style.set_bg_color(lv.color_hex(0xA0A0FF))
        #style.set_border_color(lv.color_hex(0x88FF88))
        
        # tabla de iconos 4x2
        col_dsc = [65, 65, 65,65, lv.GRID_TEMPLATE_LAST]
        row_dsc = [60,60,60,lv.GRID_TEMPLATE_LAST]
        tbl_iconos = lv.obj(lv.screen_active())
        tbl_iconos.move_foreground()
        tbl_iconos.set_size(320, 219)
        tbl_iconos.align_to(lv.screen_active(), lv.ALIGN.TOP_LEFT, 0, 21)
        tbl_iconos.set_grid_dsc_array(col_dsc, row_dsc)
        tbl_iconos.add_style(style,0)
        if sys.platform == 'linux':
            IMGPATH = "/home/angel/Documentos/Github/galdeano-lv/img/"
        else:
            IMGPATH = "/img/"
        for index,item in enumerate(appMenu.Gal_pantallas):
            try:
                some_image_data = self.get_image_data(IMGPATH+item["icon"])
                some_image_data_mv = memoryview(some_image_data)
                some_img_dsc = self.create_img_dsc(some_image_data_mv)
                img1 = lv.image(tbl_iconos)
                img1.set_src(some_img_dsc)
                img1.set_size(60, 60)
                lg=lv.label(img1)
                lg.set_text(item["Name"])
                lg.align_to(img1, lv.ALIGN.TOP_LEFT, 0, 80)
                img1.add_flag(lv.obj.FLAG.CLICKABLE)                
                img1.set_grid_cell(lv.GRID_ALIGN.START, index%4, 1,lv.GRID_ALIGN.START, index//4, 1)
                img1.add_event_cb(lambda e: self.execApp(e,item) , lv.EVENT.CLICKED, None)
            except:
                print("Could not find the file "+item["icon"])
                labelGaldeano = lv.label(tbl_iconos)
                labelGaldeano.set_text("NO IMG")
                labelGaldeano.set_grid_cell(lv.GRID_ALIGN.CENTER, index%4, 1,lv.GRID_ALIGN.CENTER, index//4, 1)
        # we will exec this function when we press exe button
        miTeclado.execFunc = lambda e: self.exeButton(e,"exec button pressed")
        miTeclado.selectMenuFunc=self.execScreen
        miTeclado.ObjActive = self
         
            
    
    def execScreenConf(self):
        self.miCabecera.strTitle="FINDER"
        self.miCabecera.setHeader()
        label = lv.label(lv.screen_active())
        label.set_text("configuration screen FINDER")
        label.center()
        # List the information from a .zip archive
        from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
        print('\nListing information')
        with ZipFile("/readme.zip", 'r') as archive: 
            for info in archive.infolist(): 
                print(info.filename)
                print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)') 
                print('\tZIP version:\t' + str(info.create_version)) 
                print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
                print('\tUncompressed:\t' + str(info.file_size) + ' bytes')
        
    def clearScreen(self):
        super().clearScreen()
        miTeclado = teclado.teclado()
        miTeclado.graphCursor = None
