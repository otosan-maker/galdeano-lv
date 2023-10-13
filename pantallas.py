import lvgl as lv
import guiObj1
import guiObj2
import guiObj3
import guiObj0
import teclado

#####################################
#
#           PANTALLA
#
#####################################

pantalla_sel = None


Gal_pantallas = [{"Name":"Calculator","function":guiObj1.guiObj1}
                 ,{"Name":"Editor","function":guiObj3.guiObj3 }
                 ,{"Name":"Graphics","function":guiObj2.guiObj2}
                 ,{"Name":"Demo","function":guiObj0.guiObj0}
                 ]


def pantalla_sel_event_handler(evt):
    global pantalla_sel
    code = evt.get_code()
    obj  = evt.get_target()

    if code == lv.EVENT.VALUE_CHANGED :
        id = obj.get_selected_btn()
        txt = obj.get_btn_text(id)
        if(txt == "Void"):
            return
        pantalla_sel.delete()
        miTeclado = teclado.teclado()
        miTeclado.graphCursor = None
        
        
        for pantalla in Gal_pantallas:
            if pantalla['Name'] == txt:
                pantalla_sel=None
                meGuiObj = pantalla['function']()
                meGuiObj.clearScreen()
                meGuiObj.execScreen()
                miTeclado.ObjActive = meGuiObj

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
        print( pantalla['Name'] )
        i=i+1
        if i > iColumnas:
            btnm_map.append("\n")
            i=0
    if (len(Gal_pantallas)%2==1):   # screen number odd
        print("3 screens")
        btnm_map.append("Void")
    else:                           # screen number even
        btnm_map[len(btnm_map)-1]=""
    
    pantalla_sel = lv.btnmatrix(lv.scr_act())
    pantalla_sel.set_size(300, 200)
    pantalla_sel.set_map(btnm_map)
    pantalla_sel.align(lv.ALIGN.CENTER, 0, 0)
    pantalla_sel.add_event_cb(pantalla_sel_event_handler, lv.EVENT.ALL, None)


def openWifiConf():
    obj=lv.scr_act()
    obj.clean()
    mObj = guiObj4.guiObj4()
    mObj.execScreenConf()