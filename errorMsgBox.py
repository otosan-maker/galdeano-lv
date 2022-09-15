import lvgl as lv
import pantallas

def eMsgBox(e):
    mbox = e.get_current_target()
    print("Button %s clicked" % mbox.get_active_btn_text())
    pantallas.openWifiConf()

btns = ["OK",  ""]


def errorMsgBox(strMesg):
    mbox1 = lv.msgbox(lv.scr_act(), "ERROR", strMesg , btns, True)
    mbox1.add_event_cb(eMsgBox, lv.EVENT.VALUE_CHANGED, None)
    mbox1.center()
