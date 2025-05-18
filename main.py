import lvgl as lv
import guiObj1
import comunication as comu
import teclado
import machine

miTeclado = teclado.teclado()
tim0 = machine.Timer(1)
tim0.init(period=100, mode=machine.Timer.PERIODIC, callback=lambda t:miTeclado.key_loop())



meGuiObj = guiObj1.guiObj1()
meGuiObj.execScreen()