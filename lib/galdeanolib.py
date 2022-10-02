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

