import lvgl as lv
import eigenmath
import teclado
import galdeanolib as gal
import guiHeader
import comunication
import errorMsgBox as error

#####################################
#             cibus tabula
#####################################
#decoracion

ct_locations = [" ","congelador","carne","pescado"]
ct_selected_location = None

def DeleteItem(e,localizacion,cibusTabula):
    obj = e.get_target()
    #obtenemos la etiq
    label=obj.get_child(0)
    comunication.cibusTabulaConsume(label.get_text())
    llenaCibusTabula(localizacion,cibusTabula)

def change_event_cb(e,ta,cibusTabula):
    obj = e.get_target()
    row = lv.C_Pointer()
    col = lv.C_Pointer()
    cibusTabula.get_selected_cell(row, col)
    #print("row: ",row.uint_val)
    if (col.uint_val == 0):
        ta.set_text('borrame')
    else:
        ta.set_text(cibusTabula.get_cell_value(row.uint_val,col.uint_val))
    #print(cibusTabula.get_cell_value(row.uint_val,col.uint_val))

#menu localizacion de cibus tabula
def ct_location_menu(e,cibusTabula):
    global ct_locations,ct_selected_location
    dropdown = e.get_target()
    print(dropdown.get_selected())
    print(ct_locations[dropdown.get_selected()])
    ct_selected_location=ct_locations[dropdown.get_selected()]
    llenaCibusTabula( ct_selected_location ,cibusTabula)
    

#boton exe
def tabula_exe(e,ta,cibusTabula):
    datos = comunication.cibusTabulaAlta(ta.get_text(),ct_selected_location)
    llenaCibusTabula(ct_selected_location,cibusTabula)
    
def llenaCibusTabula(localizacion,cibusTabula):
    #comunication.connect()
    #comunication.connectMQTT()
    #comunication.send_msg_MQTT('galdeano',ta.get_text())
    datos = comunication.cibusTabulaConsulta('doradas',localizacion)
    print(datos)
    #borramos los datos viejos
    cibusTabula.clean()
    
    for idx, product in enumerate(datos):
        btn1 = lv.btn(cibusTabula)
        btn1.set_size(33,18)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, -8, -8)
        btn1.add_event_cb(lambda e:DeleteItem(e,localizacion,cibusTabula), lv.EVENT.CLICKED, None)
        lbl_Prod  = lv.label(cibusTabula)
        lbl_fecha = lv.label(cibusTabula)
        btn1.align_to(cibusTabula,lv.ALIGN.TOP_LEFT,-7,20*idx -8)
        lbl_Prod.align_to(cibusTabula,lv.ALIGN.TOP_LEFT,30,20*idx-5)
        lbl_fecha.align_to(cibusTabula,lv.ALIGN.TOP_LEFT,202,20*idx-5)
        label_btn1.set_text(product["prod_id"])
        lbl_Prod.set_text(product["producto"][0:20])
        lbl_fecha.set_text(str(product["f_alta"])[0:10])
        


def execScreen():
    global ct_locations 
    
    miTeclado = teclado.teclado()
    import pantallas
    miTeclado.selectMenuFunc=pantallas.select
    
    #Interfaz grafico
    miCabecera = guiHeader.guiHeader()
    miCabecera.strTitle="CibusTabula"
    miCabecera.setHeader()
    if not comunication.sta_if.isconnected():
        error.errorMsgBox("First starts Wifi")
        return
    
    
    ta = lv.textarea(lv.scr_act())
    ta.align(lv.ALIGN.TOP_LEFT, 0, 25)
    ta.set_one_line(True)
    ta.set_width(160)
    ta.set_placeholder_text( "producto")
    ta.add_state(lv.STATE.FOCUSED)
    ta.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    miTeclado.taWidget=ta
    
    style = lv.style_t()
    style.init()
    style.set_text_font(lv.galdeano_14)

    cibusTabula = lv.obj(lv.scr_act())
    cibusTabula.set_size(319, 145)
    cibusTabula.align(lv.ALIGN.TOP_LEFT, 0, 65)
    cibusTabula.add_style(style, 0)
    miTeclado.execFunc = lambda e: tabula_exe(e,ta,cibusTabula)
    
    dropdown = lv.dropdown(lv.scr_act())
    dropdown.align(lv.ALIGN.TOP_LEFT, 165, 25)
    dropdown.set_options("\n".join(ct_locations))
    dropdown.add_event_cb(lambda e: ct_location_menu(e, cibusTabula) , lv.EVENT.VALUE_CHANGED, None)
    
    btn1 = lv.btn(lv.scr_act())
    btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
    btn1.set_size(75,25)
    label_btn1 = lv.label(btn1)
    label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn1.set_text("Alta")
    btn1.add_event_cb(lambda e:tabula_exe(e,ta,cibusTabula), lv.EVENT.CLICKED, None)
    
    btn2 = lv.btn(lv.scr_act())
    btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
    btn2.set_size(75,25)
    label_btn2 = lv.label(btn2)
    label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn2.set_text("")
    #btn2.add_event_cb(lambda e: gal.dic(e,ta,btn2) , lv.EVENT.CLICKED, None)
    
    btn3 = lv.btn(lv.scr_act())
    btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
    btn3.set_size(75,25)
    label_btn3 = lv.label(btn3)
    label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn3.set_text( "" )
    #btn3.add_event_cb(lambda e: gal.trig2(e,ta), lv.EVENT.CLICKED, None)
    
    btn4 = lv.btn(lv.scr_act())
    btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
    btn4.set_size(75,25)
    label_btn4 = lv.label(btn4)
    label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn4.set_text("")
    #btn4.add_event_cb(lambda e: emathp_exe(e,ta,label), lv.EVENT.CLICKED, None)

