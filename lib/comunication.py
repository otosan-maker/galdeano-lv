import network
import ubinascii
import machine
from machine import Timer
from umqttsimple import MQTTClient
import urequests
import json

sta_if = network.WLAN(network.STA_IF)
client = None


def startUpWifi():
    try:
        f=open('/data/wifi.txt','r')
        netw = json.load(f)
        f.close()
        if netw["startupInit"]:
            sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
            sta_if.connect(netw["network"], netw["password"])
    except:
      print("Wifi file setting error")

def connectWifi():
    global sta_if
    
    if sta_if.isconnected():
        return
    
    print("Connect WIFI")
    f=open('/data/wifi.txt','r')
    netw = json.load(f)
    f.close()
    
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    sta_if.connect(netw["network"], netw["password"])
    

def disConnectWifi():
    global sta_if
    sta_if.disconnect()
    
def onTimerWifi():
    import guiHeader
    
    miCabecera = guiHeader.guiHeader()
    tim1 = Timer(2)
    tim1.init(period=8000, mode=Timer.PERIODIC, callback=lambda t:miCabecera.setWifi())
    
def getSSIDList():
    sta_if = network.WLAN(network.STA_IF);
    sta_if.active(True)
    lst_network = sta_if.scan()
    listSSID = []
    for u_network in lst_network:
        listSSID.append(u_network[0].decode('UTF-8'))
    print(listSSID)
    return listSSID

def connectMQTT():
    global client
    mqtt_server = '192.168.1.34'
    msg         = 'lorrrr'
    client_id = "galdeano"
    print(str(ubinascii.hexlify(machine.unique_id())))
    client = MQTTClient(client_id, mqtt_server)
    client.connect()
    
def send_msg_MQTT(topic_pub,msg):
    global client
    client.publish(topic_pub, msg)

def cibusTabulaConsulta(producto,localizacion):
    URL='http://192.168.1.34:1880/listado?localizacion='+str(localizacion)
    #URL='http://192.168.1.34:1880/listado?localizacion=carne'
    print(URL)
    response = urequests.get(URL)
    return response.json()

def cibusTabulaAlta(producto,localizacion):
    URL='http://192.168.1.34:1880/alta?localizacion='+str(localizacion)+'&producto='+str(producto)
    #URL='http://192.168.1.34:1880/listado?localizacion=carne'
    print(URL)
    response = urequests.get(URL)
    return True


def cibusTabulaConsume(productoID):
    URL='http://192.168.1.34:1880/consumeID?id='+str(productoID)
    print(URL)
    response = urequests.get(URL)
    return True


def altaPesoService(peso):
    URL='http://192.168.1.34:1880/alta_peso?valor='+str(peso)
    response = urequests.get(URL).json()
    print(response)
    return True

def getPesoService():
    URL='http://192.168.1.34:1880/get_peso'
    response = urequests.get(URL).json()
    print(response)
    return response