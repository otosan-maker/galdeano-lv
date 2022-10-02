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


# spi = lv_spi.SPI(mosi=23, miso=19, clk=18)
# sd = sdcard.SDCard(spi, machine.Pin(5))
# os.mount(sd, "/sd")
# print(os.listdir('/sd'))
    
# sd = sdcard.SDCard(lv_spi.SPI(), machine.Pin(5))
# os.mount(sd, "/sd")
# print(os.listdir('/sd'))

# def logTime():
#     f=open("/data/time.log","a")
#     f.write("600000 milisegundos\n")
#     f.close()

miTeclado = teclado.teclado()

tim0 = Timer(1)
tim0.init(period=100, mode=Timer.PERIODIC, callback=lambda t:miTeclado.key_loop())

# logger = Timer(3)
# logger.init(period=60000, mode=Timer.PERIODIC, callback=lambda t:logTime())


comu.startUpWifi()
comu.onTimerWifi()

meGuiObj = guiObj1.guiObj1()
meGuiObj.execScreen()
miTeclado.ObjActive = meGuiObj
