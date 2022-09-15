import lvgl as lv
import os
import eigenmath
import teclado
import galdeanolib as gal
import guiHeader




#####################################
#
#           EDITOR
#
#####################################

file_name = ""
edit_file_name = True

def enter(e,ta):
    ta.add_text("\n")



def openFile(e):
    global cont_col2
    global file_name
    obj2  = e.get_target()
    file_name = '/data/'+str(obj2.get_child(0).get_text())
    datafile = open(file_name)
    ta.set_text(datafile.read())
    datafile.close()
    cont_col2.delete()

def abre(e):
    dicVal = os.listdir("data")
    global cont_col2
    global btn1
    col_dsc = [200, lv.GRID_TEMPLATE.LAST]
    row_dsc = [20]
    for i in range(len(dicVal)):
        row_dsc.append(20)
    row_dsc.append(lv.GRID_TEMPLATE.LAST)
    # Create a container with COLUMN flex direction
    cont_col2 = lv.obj(lv.scr_act())
    cont_col2.move_foreground()
    cont_col2.set_size(250, 150)
    cont_col2.align(lv.ALIGN.TOP_LEFT, 0, 50)
    cont_col2.set_grid_dsc_array(col_dsc, row_dsc)
    for index,item in enumerate(dicVal):
        obj = lv.btn(cont_col2)
        obj.set_grid_cell(lv.GRID_ALIGN.STRETCH, 0, 1,lv.GRID_ALIGN.STRETCH, index, 1)
        obj.add_event_cb(openFile, lv.EVENT.CLICKED, None)
        label = lv.label(obj)
        label.set_text(item)
        label.center()



def guarda(e):
    global file_name
    global ta,ta2
    global edit_file_name
    if(file_name!=""):
        if(ta.get_text()!=""):
            fichero = open(file_name,"w")
            fichero.write(ta.get_text())
            fichero.close()
        else:
            os.remove(file_name)
    else:
        print("con que nombre")
        if(edit_file_name):
            ta2=lv.textarea(lv.scr_act())
            ta2.align(lv.ALIGN.TOP_LEFT, 3, 160)
            ta2.set_one_line(True)
            ta2.set_width(310)
            ta2.set_placeholder_text( "File Name")
            miTeclado = teclado.teclado()
            miTeclado.taWidget=ta2
            ta2.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
            ta2.add_state(lv.STATE.FOCUSED)
            edit_file_name=False
        else:
            if(ta.get_text()!=""):
                file_name="/data/"+ta2.get_text()+".txt"
                ta2.delete()
                if(ta.get_text()!=""):
                    fichero = open(file_name,"w")
                    fichero.write(ta.get_text())
                    fichero.close()
                else:
                    os.remove(file_name)
def event_msgBox(e):
    mbox = e.get_current_target()
    print("Button %s clicked" % mbox.get_active_btn_text())

def com(e):
    global ta
    btns = [""]
    
    if(file_name==""):
        mbox1 = lv.msgbox(lv.scr_act(), "Exec File", "Primero tienes que guardar el fichero", btns, True)
        mbox1.add_event_cb(event_msgBox, lv.EVENT.VALUE_CHANGED, None)
        mbox1.center()
    else:
        fileout_name="/data/out.txt"
        fichero = open(fileout_name,"w")
        x=ta.get_text().split('\n')
        for line in x:
            fichero.write(eigenmath.run(line ))
        fichero.close()
        mbox1 = lv.msgbox(lv.scr_act(), "Fichero", "guardado out.txt", btns, True)
        mbox1.add_event_cb(event_msgBox, lv.EVENT.VALUE_CHANGED, None)
        mbox1.center()
        
def execScreen():
    global ta,titulo
    global btn1
    global btn2
    global modeLabel
    #Interfaz grafico
    miTeclado = teclado.teclado()
    miCabecera = guiHeader.guiHeader()
    miCabecera.strTitle="Galdeano Editor"
    miCabecera.setHeader()
    
    styleTAInput = lv.style_t()
    styleTAInput.init()
    styleTAInput.set_pad_top(0)
    styleTAInput.set_text_font(lv.galdeano_14)
    ta = lv.textarea(lv.scr_act())
    ta.align(lv.ALIGN.TOP_LEFT, 0, 23)
    ta.set_size(319,185)
    ta.set_placeholder_text( "Text editor")
    ta.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    ta.add_state(lv.STATE.FOCUSED)
    ta.add_style(styleTAInput, 0)
    miTeclado.taWidget=ta
    miTeclado.execFunc = lambda e: enter(e,ta)
    
    btn1 = lv.btn(lv.scr_act())
    btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 2, 212)
    btn1.set_size(65,25)
    label_btn1 = lv.label(btn1)
    label_btn1.set_text("Open")
    label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
    btn1.add_event_cb(abre, lv.EVENT.CLICKED, None)
    
    btn2 = lv.btn(lv.scr_act())
    btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 71, 212)
    btn2.set_size(65,25)
    label_btn2 = lv.label(btn2)
    label_btn2.set_text("Save")
    label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
    btn2.add_event_cb(guarda, lv.EVENT.CLICKED, None)

    btn3 = lv.btn(lv.scr_act())
    btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 138, 212)
    btn3.set_size(65,25)
    label_btn3 = lv.label(btn3)
    label_btn3.set_text( "Com" )
    label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
    btn3.add_event_cb(com, lv.EVENT.CLICKED, None)

    btn4 = lv.btn(lv.scr_act())
    btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 206, 212)
    btn4.set_size(53,25)
    label_btn4 = lv.label(btn4)
    label_btn4.set_text("Dic")
    label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
    btn4.add_event_cb(lambda e: gal.dic(e,ta,btn4), lv.EVENT.CLICKED, None)

    btn5 = lv.btn(lv.scr_act())
    btn5.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 261, 212)
    btn5.set_size(55,25)
    label_btn5 = lv.label(btn5)
    label_btn5.set_text("CLS")
    label_btn5.align_to(btn5, lv.ALIGN.TOP_LEFT, 0, -4)
    btn5.add_event_cb(lambda e: gal.cls(e,ta,None), lv.EVENT.CLICKED, None)


