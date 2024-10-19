import lvgl as lv
from ili9XXX import ili9341
from xpt2046 import xpt2046
import guiObj1

import machine, os, lv_spi, sdcard

import teclado
from machine import Timer

#disp = ili9341(miso=19, mosi=23, clk=18, cs=15, dc=2, rst=4, power=-1, backlight=-1, backlight_on=0, power_on=0,
#        spihost=1, mhz=28, factor=4, hybrid=True, width=320, height=240, start_x=0, start_y=0, invert=False,rot=-4)

disp = ili9341(miso=13, mosi=11, clk=12, cs=10, dc=9, rst=14, power=0, backlight=0, backlight_on=0, power_on=0,
        spihost=1, spimode=0, mhz=40, factor=16, hybrid=True, width=320, height=240, start_x=0, start_y=0, rot=-4)

touch=xpt2046()
obj=lv.scr_act()


miTeclado = teclado.teclado()

tim0 = Timer(1)
tim0.init(period=100, mode=Timer.PERIODIC, callback=lambda t:miTeclado.key_loop())


meGuiObj = guiObj1.guiObj1()
meGuiObj.execScreen()
miTeclado.ObjActive = meGuiObj
