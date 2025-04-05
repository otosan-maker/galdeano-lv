import lvgl as lv
import guiObj1
import comunication as comu
import teclado
from machine import Timer

miTeclado = teclado.teclado()
tim0 = Timer(1)
tim0.init(period=100, mode=Timer.PERIODIC, callback=lambda t:miTeclado.key_loop())



meGuiObj = guiObj1.guiObj1()
meGuiObj.execScreen()
#miTeclado.ObjActive = meGuiObj
