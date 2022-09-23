import lvgl as lv
import json
import teclado
import guiHeader
from guiBase import guiBase
import galdeanolib as gal
import urequests
import comunication as comu
from math import ceil
import errorMsgBox as error


class guiObj4(guiBase):
    def __init__(self):
        super().__init__()
    
    def getPhilipHubAddr(self):
        try:
            info = urequests.get("https://34.117.13.189/").json() # No responde a la ip, solo al dominio
            print(info["internalipaddress"])
            return info["internalipaddress"]
        except:
            print("Excecpion en getPhilipHubAddr")
            return "192.168.1.106"
        
    def ligthOn(self,e,group,PhilipsHubAddr):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            if obj.has_state(lv.STATE.CHECKED):
                print("State: on")
                post_data='{"on":true}'
            else:
                print("State: off")
                post_data='{"on":false}'
            res = urequests.put("http://"+PhilipsHubAddr+"/api/C5R6hZKkOB5ZqzXeQiCilzeTXnjriuYMVEaVGEnY/groups/"+str(group)+"/action",  data = post_data)
            print(res.json())

    def slider_event_cb(self,e,group,PhilipsHubAddr):
        slider = e.get_target()
        print("{:d}%".format(slider.get_value()))
        bri=slider.get_value() * 2.55
        post_data='{"bri":'+str(ceil(bri))+'}'
        print(post_data)
        res = urequests.put("http://"+PhilipsHubAddr+"/api/C5R6hZKkOB5ZqzXeQiCilzeTXnjriuYMVEaVGEnY/groups/"+str(group)+"/action",  data = post_data)
        print(res.json())

    

    def execScreen(self):
        miTeclado = teclado.teclado()
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Philips Hue"
        self.miCabecera.setHeader()
        
        if not comu.sta_if.isconnected():
            error.errorMsgBox("First starts Wifi")
            return
        
        PhilipsHubAddr = self.getPhilipHubAddr()
        
        groups = urequests.get("http://"+PhilipsHubAddr+"/api/C5R6hZKkOB5ZqzXeQiCilzeTXnjriuYMVEaVGEnY/groups/").json()
            
        mesaLbl=lv.label(lv.scr_act())
        mesaLbl.align(lv.ALIGN.TOP_LEFT, 6, 57)
        mesaLbl.set_text("Mesa:")
        mesaSsw = lv.switch(lv.scr_act())
        mesaSsw.align(lv.ALIGN.TOP_LEFT, 65, 50)
        if(groups["2"]['action']['on']==True):
            mesaSsw.add_state(lv.STATE.CHECKED)
        mesaSsw.add_event_cb(lambda e: self.ligthOn(e,2,PhilipsHubAddr) ,lv.EVENT.ALL, None)
        mesaSlider = lv.slider(lv.scr_act())
        mesaSlider.align(lv.ALIGN.TOP_LEFT, 135, 57)
        mesaSlider.set_width(150)
        mesaSlider.set_value(ceil(groups["2"]["action"]["bri"] /2.55),lv.ANIM.OFF)
        mesaSlider.add_event_cb(lambda e: self.slider_event_cb(e,2,PhilipsHubAddr) , lv.EVENT.VALUE_CHANGED, None)
        
        
        pianoLbl=lv.label(lv.scr_act())
        pianoLbl.align(lv.ALIGN.TOP_LEFT, 6, 93)
        pianoLbl.set_text("Piano:")
        pianoSsw = lv.switch(lv.scr_act())
        pianoSsw.align(lv.ALIGN.TOP_LEFT, 65, 86)
        if(groups["3"]['action']['on']==True):
            pianoSsw.add_state(lv.STATE.CHECKED)
        pianoSsw.add_event_cb(lambda e: self.ligthOn(e,3,PhilipsHubAddr) ,lv.EVENT.ALL, None)
        pianoSlider = lv.slider(lv.scr_act())
        pianoSlider.align(lv.ALIGN.TOP_LEFT, 135, 93)
        pianoSlider.set_width(150)
        pianoSlider.set_value(ceil(groups["3"]["action"]["bri"] /2.55),lv.ANIM.OFF)
        pianoSlider.add_event_cb(lambda e: self.slider_event_cb(e,3,PhilipsHubAddr) , lv.EVENT.VALUE_CHANGED, None)
            
        sofaLbl=lv.label(lv.scr_act())
        sofaLbl.align(lv.ALIGN.TOP_LEFT, 6, 127)
        sofaLbl.set_text("Sofa:")
        sofaSsw = lv.switch(lv.scr_act())
        sofaSsw.align(lv.ALIGN.TOP_LEFT, 65, 120)
        if(groups["4"]['action']['on']==True):
            sofaSsw.add_state(lv.STATE.CHECKED)
        sofaSsw.add_event_cb(lambda e: self.ligthOn(e,4,PhilipsHubAddr),lv.EVENT.ALL, None)
        sofaSlider = lv.slider(lv.scr_act())
        sofaSlider.align(lv.ALIGN.TOP_LEFT, 135, 127)
        sofaSlider.set_width(150)
        sofaSlider.set_value(ceil(groups["4"]["action"]["bri"] /2.55),lv.ANIM.OFF)
        sofaSlider.add_event_cb(lambda e: self.slider_event_cb(e,4,PhilipsHubAddr) , lv.EVENT.VALUE_CHANGED, None)
            
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text(" ")
        #btn1.add_event_cb(lambda e: setGraph(e,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text(" ")
        #btn2.add_event_cb(lambda e: gal.dic(e,ta,btn2) , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( " " )
        #btn3.add_event_cb(lambda e: gal.trig2(e,ta), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text(" ")
        #btn4.add_event_cb(lambda e: saveDataGraf(e,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT), lv.EVENT.CLICKED, None)

#####################################
#
#           Configuracion WIFI
#
#####################################
    
    
    def autoStartup(self,e):
        code = e.get_code()
        obj  = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED:
            f=open('/data/wifi.txt','r')
            netw = json.load(f)
            f.close()
            f=open('/data/wifi.txt','w')
            txt = obj.get_text()
            if obj.get_state() & lv.STATE.CHECKED:
                netw["startupInit"]   = True
            else:
                netw["startupInit"]   = False
            json.dump(netw,f)
            f.close()

    def scanWifi(self,e,dd):
        listaSSDI=comu.getSSIDList()
        #quitamos las entradas vacias
        dd.set_options("\n".join(filter(None, listaSSDI)))


    def event_handler_DD(self,e):
        code = e.get_code()
        obj = e.get_target()
        if code == lv.EVENT.VALUE_CHANGED: 
            option = " "*10 # should be large enough to store the option
            obj.get_selected_str(option, len(option))
            # .strip() removes trailing spaces
            print("Option: \"%s\"" % option.strip())


    def saveWifiConf(self,e,networkLbl,dd,ta):
        option = " "*32
        dd.get_selected_str(option, len(option))
        optionString = option.strip()

        f=open('/data/wifi.txt','r')
        netw = json.load(f)
        f.close()
        
        netw["network"]   = optionString[:-1] # hemos copiado una cadena de C y viene terminada en cero, dump de json lo nota
        netw["password"]  = ta.get_text()
        f=open('/data/wifi.txt','w')
        json.dump(netw,f)
        f.close()
        
        
        networkLbl.set_text("Saved NetW: "+netw["network"]+" // "+netw["password"])
        return

    def execScreenConf(self):
        miTeclado = teclado.teclado()
        self.miCabecera.strTitle="WIFI"
        self.miCabecera.setHeader()
        
        f=open('/data/wifi.txt','r')
        netw = json.load(f)
        f.close()
        
        networkLbl=lv.label(lv.scr_act())
        networkLbl.align(lv.ALIGN.TOP_LEFT, 6, 23)
        networkLbl.set_text("Saved NetW: "+netw["network"]+" // "+netw["password"])
        
        scanLbl=lv.label(lv.scr_act())
        scanLbl.align(lv.ALIGN.TOP_LEFT, 6, 56)
        scanLbl.set_text("Scaned NetW:")
        
        
        dd = lv.dropdown(lv.scr_act())
        dd.set_options("\n".join(["Empty"]))

        dd.align(lv.ALIGN.TOP_LEFT, 130, 46)
        dd.add_event_cb(self.event_handler_DD, lv.EVENT.ALL, None)
        
        passLbl=lv.label(lv.scr_act())
        passLbl.align(lv.ALIGN.TOP_LEFT, 16, 100)
        passLbl.set_text("Passwd:")
        
        ta = lv.textarea(lv.scr_act())
        ta.align(lv.ALIGN.TOP_LEFT, 130, 90)
        ta.set_one_line(True)
        ta.set_width(120)
        ta.set_placeholder_text( "passwd")
        ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        ta.set_text( str(netw["password"]) )
        
        cb = lv.checkbox(lv.scr_act())
        cb.set_text("Startup WIFI")
        cb.align(lv.ALIGN.TOP_LEFT, 16, 140)
        if netw["startupInit"]:
            cb.add_state(lv.STATE.CHECKED)
        cb.add_event_cb(self.autoStartup, lv.EVENT.ALL, None)

        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("WifiOn")
        btn1.add_event_cb(lambda e:comu.connectWifi(), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("WifiOff")
        btn2.add_event_cb(lambda e: comu.disConnectWifi() , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "Scan" )
        btn3.add_event_cb(lambda e: self.scanWifi(e,dd), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("Save")
        btn4.add_event_cb(lambda e: self.saveWifiConf(e,networkLbl,dd,ta), lv.EVENT.CLICKED, None)


