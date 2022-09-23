import lvgl as lv
import teclado
import json
import galdeanolib as gal
import guiHeader



def setGraph(event,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT):
    gal.data["function"]     = ta.get_text(  )
    gal.data["function_x_t"] = taXT.get_text(  )
    gal.data["function_y_t"] = taYT.get_text(  )
    gal.data["Xmax"]         = eval(ta2.get_text( ))
    gal.data["Xmin"]         = eval(ta3.get_text( ))
    gal.data["Ymax"]         = eval(ta4.get_text( ))
    gal.data["Ymin"]         = eval(ta5.get_text( ))
    gal.data["Tmax"]         = eval(ta6.get_text( ))
    gal.data["Tmin"]         = eval(ta7.get_text( ))
    gal.data["parametric"]   = ta8.get_state( )
    import pantallas   as pan
    pan.openGraf(event)


def saveDataGraf(event,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT):
    print(gal.data)
    gal.data["function"]     = ta.get_text(  )
    gal.data["function_x_t"] = taXT.get_text(  )
    gal.data["function_y_t"] = taYT.get_text(  )
    gal.data["Xmax"]         = eval(ta2.get_text( ))
    gal.data["Xmin"]         = eval(ta3.get_text( ))
    gal.data["Ymax"]         = eval(ta4.get_text( ))
    gal.data["Ymin"]         = eval(ta5.get_text( ))
    gal.data["Tmax"]         = eval(ta6.get_text( ))
    gal.data["Tmin"]         = eval(ta7.get_text( ))
    gal.data["parametric"]   = ta8.get_state()
    f=open('/data/graf.txt','w')
    json.dump(gal.data,f)
    f.close()

def cb_event_handler(e,ta,taXT,taYT):
    code = e.get_code()
    obj = e.get_target()
    if code == lv.EVENT.VALUE_CHANGED:
        if obj.get_state() & lv.STATE.CHECKED:
            ta.add_flag(ta.FLAG.HIDDEN)
            taXT.clear_flag(taXT.FLAG.HIDDEN)
            taYT.clear_flag(taYT.FLAG.HIDDEN)
        else:
            taXT.add_flag(taXT.FLAG.HIDDEN)
            taYT.add_flag(taYT.FLAG.HIDDEN)
            ta.clear_flag(ta.FLAG.HIDDEN)

        
#####################################
#
#           Configuracion
#
#####################################
def execScreen():
    data = gal.data
    
    miTeclado = teclado.teclado()
    miCabecera = guiHeader.guiHeader()
    miCabecera.strTitle="Galdeano Graf Conf"
    miCabecera.setHeader()

    
    styleTAInput = lv.style_t()
    styleTAInput.init()
    styleTAInput.set_pad_top(0)
    
    #definimos el interfaz para parametricas
    
    taXT = lv.textarea(lv.scr_act())
    taXT.align(lv.ALIGN.TOP_LEFT, 10, 23)
    taXT.set_one_line(True)
    taXT.set_width(145)
    taXT.set_placeholder_text( "x(t)=")
    taXT.add_style(styleTAInput, 0)
    taXT.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    taXT.set_text( str(data["function_x_t"]) )
    taYT = lv.textarea(lv.scr_act())
    taYT.align(lv.ALIGN.TOP_LEFT, 160, 23)
    taYT.set_one_line(True)
    taYT.set_width(145)
    taYT.set_placeholder_text( "y(t)=")
    taYT.add_style(styleTAInput, 0)
    taYT.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    taYT.set_text( str(data["function_y_t"]) )

    #definimos el interfaz para funciones normales
    
    ta = lv.textarea(lv.scr_act())
    ta.align(lv.ALIGN.TOP_LEFT, 10, 23)
    ta.set_one_line(True)
    ta.set_width(290)
    ta.set_placeholder_text( "f(x)=")
    ta.add_style(styleTAInput, 0)
    ta.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    ta.set_text( str(data["function"]) )
    
    if data["parametric"] == lv.STATE.CHECKED:
        ta.add_flag(ta.FLAG.HIDDEN)
    else:
        taXT.add_flag(taXT.FLAG.HIDDEN)
        taYT.add_flag(taYT.FLAG.HIDDEN)
    
    XLabel=lv.label(lv.scr_act())
    XLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 10, 70)
    XLabel.set_text("X Axis:")
    
    ta2 = lv.textarea(lv.scr_act())
    ta2.align(lv.ALIGN.TOP_LEFT, 90, 66)
    ta2.set_one_line(True)
    ta2.set_width(100)
    ta2.set_placeholder_text( "Max X")
    ta2.set_text( str(data["Xmax"]) )
    ta2.add_style(styleTAInput, 0)
    ta2.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    
    ta3 = lv.textarea(lv.scr_act())
    ta3.align(lv.ALIGN.TOP_LEFT, 190, 66)
    ta3.set_one_line(True)
    ta3.set_width(100)
    ta3.set_placeholder_text( "Min X")
    ta3.set_text( str(data["Xmin"] ))
    ta3.add_style(styleTAInput, 0)
    ta3.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    
    YLabel=lv.label(lv.scr_act())
    YLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 10, 110)
    YLabel.set_text("Y Axis:")
    
    ta4 = lv.textarea(lv.scr_act())
    ta4.align(lv.ALIGN.TOP_LEFT, 90, 106)
    ta4.set_one_line(True)
    ta4.set_width(100)
    ta4.set_placeholder_text( "Max Y")
    ta4.set_text( str(data["Ymax"]) )
    ta4.add_style(styleTAInput, 0)
    ta4.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    
    ta5 = lv.textarea(lv.scr_act())
    ta5.align(lv.ALIGN.TOP_LEFT, 190, 106)
    ta5.set_one_line(True)
    ta5.set_width(100)
    ta5.set_placeholder_text( "Min Y")
    ta5.set_text( str(data["Ymin"]) )
    ta5.add_style(styleTAInput, 0)
    ta5.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    
    ta6 = lv.textarea(lv.scr_act())
    ta6.align(lv.ALIGN.TOP_LEFT, 90, 146)
    ta6.set_one_line(True)
    ta6.set_width(100)
    ta6.set_placeholder_text( "Max T")
    ta6.set_text( str(data["Tmax"]) )
    ta6.add_style(styleTAInput, 0)
    ta6.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    
    ta7 = lv.textarea(lv.scr_act())
    ta7.align(lv.ALIGN.TOP_LEFT, 190, 146)
    ta7.set_one_line(True)
    ta7.set_width(100)
    ta7.set_placeholder_text( "Min T")
    ta7.set_text( str(data["Tmin"]) )
    ta7.add_style(styleTAInput, 0)
    ta7.add_event_cb(lambda e: gal.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
    
    ta8 = lv.checkbox(lv.scr_act())
    ta8.set_text("Par")
    ta8.add_event_cb(lambda e: cb_event_handler(e,ta,taXT,taYT), lv.EVENT.ALL, None)
    ta8.add_state(data["parametric"])
    ta8.align(lv.ALIGN.TOP_LEFT, 10, 146)
    
    btn1 = lv.btn(lv.scr_act())
    btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
    btn1.set_size(75,25)
    label_btn1 = lv.label(btn1)
    label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn1.set_text("Graph")
    btn1.add_event_cb(lambda e: setGraph(e,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT), lv.EVENT.CLICKED, None)
    
    btn2 = lv.btn(lv.scr_act())
    btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
    btn2.set_size(75,25)
    label_btn2 = lv.label(btn2)
    label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn2.set_text("Funct")
    btn2.add_event_cb(lambda e: gal.dic(e,ta,btn2) , lv.EVENT.CLICKED, None)
    
    btn3 = lv.btn(lv.scr_act())
    btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
    btn3.set_size(75,25)
    label_btn3 = lv.label(btn3)
    label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn3.set_text( "Trigon" )
    btn3.add_event_cb(lambda e: gal.trig2(e,ta), lv.EVENT.CLICKED, None)
    
    btn4 = lv.btn(lv.scr_act())
    btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
    btn4.set_size(75,25)
    label_btn4 = lv.label(btn4)
    label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
    label_btn4.set_text("Save")
    btn4.add_event_cb(lambda e: saveDataGraf(e,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT), lv.EVENT.CLICKED, None)
