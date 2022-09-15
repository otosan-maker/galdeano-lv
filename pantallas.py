import lvgl as lv
import gui1
import gui1_2
import gui1_3
import gui1_4
import gui1_5
import gui1_6
import gui1_7
import teclado

#####################################
#
#           PANTALLA
#
#####################################

pantalla_sel = None

Gal_pantallas = [{"Name":"Calculadora","function":gui1.execScreen},
                 {"Name":"Editor","function":gui1_3.execScreen },
                 {"Name":"Graficas","function":gui1_2.execScreen},
                 {"Name":"Conf","function":gui1_4.execScreen },
                 {"Name":"Wifi","function":gui1_5.execScreenConf},
                 {"Name":"Domotica","function":gui1_5.execScreen},
                 {"Name":"CibusTab","function":gui1_6.execScreen},
                 {"Name":"Peso","function":gui1_7.execScreen}
                 ]


def pantalla_sel_event_handler(evt):
    global pantalla_sel
    code = evt.get_code()
    obj  = evt.get_target()

    if code == lv.EVENT.VALUE_CHANGED :
        id = obj.get_selected_btn()
        txt = obj.get_btn_text(id)
        pantalla_sel.delete()
        obj=lv.scr_act()
        obj.clean()
        miTeclado = teclado.teclado()
        miTeclado.graphCursor = None
        
        for pantalla in Gal_pantallas:
            if pantalla['Name'] == txt:
                pantalla_sel=None
                pantalla['function']()

def select():
    global pantalla_sel
    if pantalla_sel!=None:
        print("Hacemos select clean")
        pantalla_sel.delete()
        pantalla_sel=None
        return
    
    iColumnas=1
    i=0
    btnm_map =[]
    for pantalla in Gal_pantallas:
        btnm_map.append(pantalla['Name'])
        i=i+1
        if i > iColumnas:
            btnm_map.append("\n")
            i=0
    btnm_map[len(btnm_map)-1]=""    
    
    pantalla_sel = lv.btnmatrix(lv.scr_act())
    pantalla_sel.set_size(300, 200)
    pantalla_sel.set_map(btnm_map)
    pantalla_sel.align(lv.ALIGN.CENTER, 0, 0)
    pantalla_sel.add_event_cb(pantalla_sel_event_handler, lv.EVENT.ALL, None)

def openGraf(event):
    obj=lv.scr_act()
    obj.clean()
    gui1_2.execScreen()

def openWifiConf():
    obj=lv.scr_act()
    obj.clean()
    gui1_5.execScreenConf()