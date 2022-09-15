import lvgl as lv
import eigenmath
import teclado
import galdeanolib as gal
import guiHeader
import comunication
import math
import errorMsgBox as error

#####################################
#             PESO
#####################################

valores5=None


def get_peso(e,lbl):
    global valores5
    valores5 = comunication.getPesoService()
    #print(valores5)
    texto=""
    for valores in valores5:
        texto = texto + valores['t_medida'][0:10] + '\t' + "{:.1f}".format(valores['peso']) + '\n'
    lbl.set_text( texto )

def calStd(e,lbl,lblStd):
    if valores5==None:
        get_peso(e,lbl)
    suma=0
    for valores in valores5:
        suma = suma + valores['peso']
    incremento=valores5[-1]['peso'] - valores5[0]['peso']
    texto = "Media: "+"{:.2f}".format(suma/len(valores5)) +"\n\nEvolucion:"+"{:.2f}".format(incremento)
    lblStd.set_text(texto)
    if incremento <0:
        lblStd.set_style_text_color(lv.color_hex(0xFF0000),0)
    else:
        lblStd.set_style_text_color(lv.color_hex(0x329C58),0)

def peso_exe(e,ta):
    comunication.altaPesoService(ta.get_text())
    ta.set_text("Msg sent")
    

def execScreen():
    global btn2,btn3,btn4
    miTeclado = teclado.teclado()
    import pantallas
    miTeclado.selectMenuFunc=pantallas.select
    
#     #Interfaz grafico
    miCabecera = guiHeader.guiHeader()
    miCabecera.strTitle="Peso"
    miCabecera.setHeader()
    if not comunication.sta_if.isconnected():
        error.errorMsgBox("First starts Wifi")
        return
    
    ta = lv.textarea(lv.scr_act())
    ta.align(lv.ALIGN.TOP_LEFT, 0, 30)
    ta.set_one_line(True)
    ta.set_width(160)
    ta.set_placeholder_text( "peso")
    ta.add_state(lv.STATE.FOCUSED)
    miTeclado.taWidget=ta
    ta.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    miTeclado.execFunc = lambda e: peso_exe(e,ta)
    
    lbl = lv.label(lv.scr_act())
    lbl.set_size(160, 155)
    lbl.align(lv.ALIGN.TOP_LEFT, 10, 70)
    lbl.set_text("")
    
    lblStd = lv.label(lv.scr_act())
    lblStd.align(lv.ALIGN.TOP_LEFT, 165, 70)
    lblStd.set_text("")
    
    btn1 = lv.btn(lv.scr_act())
    btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
    btn1.set_size(75,25)
    label_btn1 = lv.label(btn1)
    label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn1.set_text("Exe")
    btn1.add_event_cb(lambda e: peso_exe(e,ta), lv.EVENT.CLICKED, None)
    
    btn2 = lv.btn(lv.scr_act())
    btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
    btn2.set_size(75,25)
    label_btn2 = lv.label(btn2)
    label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn2.set_text("Last 7")
    btn2.add_event_cb(lambda e: get_peso(e,lbl) , lv.EVENT.CLICKED, None)
    
    btn3 = lv.btn(lv.scr_act())
    btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
    btn3.set_size(75,25)
    label_btn3 = lv.label(btn3)
    label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn3.set_text( "Std" )
    btn3.add_event_cb(lambda e: calStd(e,lbl,lblStd), lv.EVENT.CLICKED, None)
    
    btn4 = lv.btn(lv.scr_act())
    btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
    btn4.set_size(75,25)
    label_btn4 = lv.label(btn4)
    label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn4.set_text(" ")
    #btn4.add_event_cb(lambda e: emathp_exe(e,ta,label), lv.EVENT.CLICKED, None)


