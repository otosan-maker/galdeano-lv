import lvgl as lv
import json
import teclado
import network
import guiHeader

class guiBase():
    btnm1    = None
    cont_col = None
    
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
    
    def event_handler(self,evt,ta):
        code = evt.get_code()
        obj  = evt.get_target()

        if code == lv.EVENT.VALUE_CHANGED :
            id = obj.get_selected_btn()
            txt = obj.get_btn_text(id)
            ta.add_text(txt)
            ta.cursor_left()
            self.btnm1.delete()
            self.btnm1=None

    def trig2(self,e,ta):
        if self.btnm1 != None:
            self.btnm1.delete()
            self.btnm1=None
            return
        
        btnm_map = ["sin()", "cos()", "tan()", "\n",
                    "arcsin()", "arccos()", "arctan()", "\n",
                    "sinh()", "cosh()", "tanh()", "\n",
                    "arcsinh()", "arccosh()", "arctanh()", ""]

        self.btnm1 = lv.btnmatrix(lv.scr_act())
        self.btnm1.set_map(btnm_map)
        self.btnm1.align(lv.ALIGN.CENTER, 0, 0)
        self.btnm1.add_event_cb(lambda e: self.event_handler(e,ta), lv.EVENT.ALL, None)	

    
    def insertDicFun(self,e,ta):
        obj2  = e.get_target()
        ta.add_text(obj2.get_child(0).get_text())
        ta.cursor_left()
        self.cont_col.delete()
        self.cont_col=None

    def dic(self,e,ta,btn2):
        dicVal    = ["roots()","factor()","abs()","integral()","d()","defint()","sqrt()","clear","inv()","quote()","eval()","outer()","simplify()","factorial()","float()","sum()","product()"]
        if self.cont_col != None:
            self.cont_col.delete()
            self.cont_col=None
            return
        
        col_dsc = [90, lv.GRID_TEMPLATE.LAST]
        row_dsc = [20]
        for i in range(len(dicVal)):
            row_dsc.append(20)
        row_dsc.append(lv.GRID_TEMPLATE.LAST)
        self.cont_col = lv.obj(lv.scr_act())
        self.cont_col.move_foreground()
        self.cont_col.set_size(150, 150)
        self.cont_col.align_to(btn2, lv.ALIGN.OUT_BOTTOM_MID, 0, -170)
        
        self.cont_col.set_grid_dsc_array(col_dsc, row_dsc)
        for index,item in enumerate(dicVal):
            # Add items to the column
            obj = lv.btn(self.cont_col)
            obj.set_grid_cell(lv.GRID_ALIGN.STRETCH, 0, 1,
                          lv.GRID_ALIGN.STRETCH, index, 1)
            obj.add_event_cb(lambda e: self.insertDicFun(e,ta), lv.EVENT.CLICKED, None)
            label = lv.label(obj)
            label.set_text(item)
            label.center()
            
    def cls(self,e,ta,label):
        ta.set_text("")
        if(label!=None):
            label.set_text("")
