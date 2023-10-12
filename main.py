import lvgl as lv
from ili9XXX import ili9341
from xpt2046 import xpt2046
import guiObj1
import comunication as comu
import machine, os, lv_spi, sdcard

import teclado
from machine import Timer

disp = ili9341()
touch=xpt2046()
obj=lv.scr_act()


miTeclado = teclado.teclado()

tim0 = Timer(1)
tim0.init(period=100, mode=Timer.PERIODIC, callback=lambda t:miTeclado.key_loop())


comu.startUpWifi()
comu.onTimerWifi()

meGuiObj = guiObj1.guiObj1()
meGuiObj.execScreen()
miTeclado.ObjActive = meGuiObj
