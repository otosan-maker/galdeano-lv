import lvgl as lv
import json
import network

f=open('/data/graf.txt','r')
data = json.load(f)
f.close()

#############################
# funciones de los botones
#############################
def cls(e,ta,label):
    ta.set_text("")
    if(label!=None):
        label.set_text("")

def event_handler(evt,ta):
    global btnm1
    code = evt.get_code()
    obj  = evt.get_target()

    if code == lv.EVENT.VALUE_CHANGED :
        id = obj.get_selected_btn()
        txt = obj.get_btn_text(id)
        ta.add_text(txt)
        ta.cursor_left()
        btnm1.delete()
        

def trig2(e,ta):
    global btnm1
    btnm_map = ["sin()", "cos()", "tan()", "\n",
                "arcsin()", "arccos()", "arctan()", "\n",
                "sinh()", "cosh()", "tanh()", "\n",
                "arcsinh()", "arccosh()", "arctanh()", ""]

    btnm1 = lv.btnmatrix(lv.scr_act())
    btnm1.set_map(btnm_map)
    btnm1.align(lv.ALIGN.CENTER, 0, 0)
    btnm1.add_event_cb(lambda e: event_handler(e,ta), lv.EVENT.ALL, None)

def insertDicFun(e,ta):
    global cont_col
    obj2  = e.get_target()
    ta.add_text(obj2.get_child(0).get_text())
    ta.cursor_left()
    cont_col.delete()
    



def dic(e,ta,btn2):
    dicVal    = ["last","roots()","factor()","abs()","integral()","d()","defint()","sqrt()","clear","inv()","quote()","eval()","outer()","simplify()","factorial()","float()","sum()","product()"]
    global cont_col
    col_dsc = [90, lv.GRID_TEMPLATE.LAST]
    row_dsc = [20]
    for i in range(len(dicVal)):
        row_dsc.append(20)
    row_dsc.append(lv.GRID_TEMPLATE.LAST)
    cont_col = lv.obj(lv.scr_act())
    cont_col.move_foreground()
    cont_col.set_size(150, 150)
    cont_col.align_to(btn2, lv.ALIGN.OUT_BOTTOM_MID, 0, -170)
    
    cont_col.set_grid_dsc_array(col_dsc, row_dsc)
    for index,item in enumerate(dicVal):
        # Add items to the column
        obj = lv.btn(cont_col)
        obj.set_grid_cell(lv.GRID_ALIGN.STRETCH, 0, 1,
                      lv.GRID_ALIGN.STRETCH, index, 1)
        obj.add_event_cb(lambda e: insertDicFun(e,ta), lv.EVENT.CLICKED, None)
        label = lv.label(obj)
        label.set_text(item)
        label.center()

############################################
#  control ta del teclado
############################################
def ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.taWidget=ta
    if code == lv.EVENT.DEFOCUSED:
        kb.taWidget=None

