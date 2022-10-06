import lvgl as lv
import os
import eigenmath
from math import ceil,sin,cos,tan,log,sqrt,exp,pi
import random
import teclado
import galdeanolib as gal
import json
import guiHeader
from guiBase import guiBase
import time


class guiObj2(guiBase):
    def __init__(self):
        super().__init__()
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(guiObj2, cls).__new__(cls)
        return cls.instance
    
    Tpixel=0
    puntoLabel = None
    puntoCruz = None
    
    listPto = [] # es una lista de puntos donde guardamos las listas de puntos a dibujar.
    
    def gestTeclado(self,key):        
        line_points = [ {"x":0, "y":0}, 
                    {"x":0, "y":4}, 
                    {"x":4, "y":4}, 
                    {"x":4, "y":0}, 
                    {"x":0, "y":0}]
        
        if(key=="del"):
            self.puntoLabel.delete()
            self.puntoCruz.delete()
            self.puntoLabel = None
            return
        if(key=="left"):
            self.Tpixel=self.Tpixel-1
            if self.Tpixel<=0:
                self.Tpixel=0
        elif(key=="rigth"):
            self.Tpixel=self.Tpixel+1
            if self.Tpixel>=320:
                self.Tpixel=320
        if self.puntoLabel == None:
            #self.puntoLabel.delete()
            self.puntoLabel = lv.label(lv.scr_act())
            self.puntoLabel.set_recolor(True)
            self.puntoCruz = lv.line(lv.scr_act())
            self.puntoCruz.set_points(line_points, 5)
        rangoGraph=gal.data
        if rangoGraph["parametric"] == lv.STATE.CHECKED:
            FXT=rangoGraph['function_x_t']
            FYT=rangoGraph['function_y_t']
        else:
            F=rangoGraph['function']
        if rangoGraph["parametric"] == lv.STATE.CHECKED:
            Tgraph=rangoGraph['Tmin']+(rangoGraph['Tmax']-rangoGraph['Tmin'])*self.Tpixel/320
            EigenmathCMD = 'eval('+FXT+',t,'+str(Tgraph)+')'
            EigenmathResultXT = eigenmath.run(EigenmathCMD )
            EigenmathCMD = 'eval('+FYT+',t,'+str(Tgraph)+')'
            EigenmathResultYT = eigenmath.run(EigenmathCMD )
            try:
                #ponemos esto porque a veces eigenmath devuelve algo al estilo 2 * 10^-5, pero lo formatea en dos lineas y no se puede evaluar por `python
                Xgraph=eval(EigenmathResultXT)
                Xpixel=(Xgraph-rangoGraph['Xmax'])*320/(rangoGraph['Xmin']-rangoGraph['Xmax'])
                Ygraph=eval(EigenmathResultYT)
                Ypixel=(Ygraph-rangoGraph['Ymax'])*218/(rangoGraph['Ymin']-rangoGraph['Ymax'])
            except:
                print("Exception")
                Xpixel=-1
                Ypixel=-1
                return
        else:
            Xpixel=self.Tpixel
            Xgraph=rangoGraph['Xmin']+(rangoGraph['Xmax']-rangoGraph['Xmin'])*Xpixel/320
            EigenmathCMD = 'eval('+F+',x,'+str(Xgraph)+')'
            EigenmathResult = eigenmath.run(EigenmathCMD )
            try:
                #ponemos esto porque a veces eigenmath devuelve algo al estilo 2 * 10^-5, pero lo formatea en dos lineas y no se puede evaluar por `python
                Ygraph=eval(EigenmathResult)
                Ypixel=(Ygraph-rangoGraph['Ymax'])*218/(rangoGraph['Ymin']-rangoGraph['Ymax'])
            except:
                Ypixel=-1
                return
        Yoffset=0
        Xoffset=0
        if Ypixel <0:
            Ypixel=0
        if Ypixel <20:
            Yoffset=20
        if Xpixel <0:
            Xpixel=0
        if Ypixel >216:
            Ypixel=216
        if Xpixel >320:
            Xpixel =320
        if Xpixel >200:
            Xoffset=-120
        self.puntoLabel.set_pos(ceil(Xpixel+Xoffset), ceil(Ypixel+Yoffset))
        self.puntoCruz.set_pos(ceil(Xpixel)-2, ceil(Ypixel)+20)
        #print("Set text : "+str(Xpixel)+","+str(Ypixel) + "T:"+ str(self.Tpixel))
        self.puntoLabel.set_text("#ff0000 ("+str( Xgraph )+","+str( Ygraph )+")#")

    def calcPoints(self):
        rangoGraph=gal.data
        points =  [ ]
        
        if rangoGraph["parametric"] == lv.STATE.CHECKED:
            FXT=rangoGraph['function_x_t']
            FYT=rangoGraph['function_y_t']
        else:
            F=rangoGraph['function']

        for self.Tpixel in range (0,319):
            if rangoGraph["parametric"] == lv.STATE.CHECKED:
                Tgraph=rangoGraph['Tmin']+(rangoGraph['Tmax']-rangoGraph['Tmin'])*self.Tpixel/320
                EigenmathCMD = 'eval('+FXT+',t,'+str(Tgraph)+')'
                EigenmathResultXT = eigenmath.run(EigenmathCMD )
                EigenmathCMD = 'eval('+FYT+',t,'+str(Tgraph)+')'
                EigenmathResultYT = eigenmath.run(EigenmathCMD )
                try:
                    #ponemos esto porque a veces eigenmath devuelve algo al estilo 2 * 10^-5, pero lo formatea en dos lineas y no se puede evaluar por `python
                    Xgraph=eval(EigenmathResultXT)
                    Xpixel=(Xgraph-rangoGraph['Xmax'])*320/(rangoGraph['Xmin']-rangoGraph['Xmax'])
                    Ygraph=eval(EigenmathResultYT)
                    Ypixel=(Ygraph-rangoGraph['Ymax'])*218/(rangoGraph['Ymin']-rangoGraph['Ymax'])
                except:
                    print("Exception")
                    Xpixel=0
                    Ypixel=0
            else:
                Xpixel=self.Tpixel
                Xgraph=rangoGraph['Xmin']+(rangoGraph['Xmax']-rangoGraph['Xmin'])*Xpixel/320
                EigenmathCMD = 'eval('+F+',x,'+str(Xgraph)+')'
                EigenmathResult = eigenmath.run(EigenmathCMD )
                try:
                    #ponemos esto porque a veces eigenmath devuelve algo al estilo 2 * 10^-5, pero lo formatea en dos lineas y no se puede evaluar por `python
                    Ygraph=eval(EigenmathResult)
                    Ypixel=(Ygraph-rangoGraph['Ymax'])*218/(rangoGraph['Ymin']-rangoGraph['Ymax'])
                except:
                    Ypixel=0
            
            if Ypixel >0 and Ypixel <=216 and Xpixel >0 and Xpixel <320 :
                pointFuntion = lv.point_t()
                pointFuntion.x=ceil(Xpixel)
                pointFuntion.y=ceil(Ypixel)
                points.append(pointFuntion)
            else :
                if len(points)>0 :
                    self.listPto.append(points)
                    points = []
            if len(points)>0 :
                self.listPto.append(points)
                
    #hace unas sola llamada a eigenmath
    def calcPoints2(self):
        rangoGraph=gal.data
        points =  [ ]
        
        if rangoGraph["parametric"] == lv.STATE.CHECKED:
            FXT=rangoGraph['function_x_t']
            FYT=rangoGraph['function_y_t']
        else:
            F=rangoGraph['function']
        #for(a,1,319,x=-5+10*a/320,print(float(eval(x^2))))
        if rangoGraph["parametric"] == lv.STATE.CHECKED:
            Delta = (rangoGraph['Tmax']-rangoGraph['Tmin'])/320
            EigenmathCMD_X = 'for(a,0,319,print(float(eval('+FXT+',t,'+str(rangoGraph['Tmin'])+'+'+str(Delta)+'*a))))'
            EigenmathCMD_Y = 'for(a,0,319,print(float(eval('+FYT+',t,'+str(rangoGraph['Tmin'])+'+'+str(Delta)+'*a))))'
            EigenmathResultXT = eigenmath.run(EigenmathCMD_X )
            EigenmathResultYT = eigenmath.run(EigenmathCMD_Y )
            XgraphList = eval('['+EigenmathResultXT+']')
            YgraphList = eval('['+EigenmathResultYT+']')
            for self.Tpixel in range (0,319):
                Xgraph=XgraphList[self.Tpixel]
                Xpixel=(Xgraph-rangoGraph['Xmax'])*320/(rangoGraph['Xmin']-rangoGraph['Xmax'])
                Ygraph=YgraphList[self.Tpixel]
                Ypixel=(Ygraph-rangoGraph['Ymax'])*218/(rangoGraph['Ymin']-rangoGraph['Ymax'])
                if Ypixel >0 and Ypixel <=216 and Xpixel >0 and Xpixel <320 :
                    pointFuntion = lv.point_t()
                    pointFuntion.x=ceil(Xpixel)
                    pointFuntion.y=ceil(Ypixel)
                    points.append(pointFuntion)
                else :
                    if len(points)>0 :
                        self.listPto.append(points)
                        points = []
            if len(points)>0 :
                self.listPto.append(points)
        else:
            Delta=(rangoGraph['Xmax']-rangoGraph['Xmin'])/320
            EigenmathCMD = 'for(a,0,319,print(float(eval('+F+',x,'+str(rangoGraph['Xmin'])+'+'+str(Delta)+'*a))))'
            #print(EigenmathCMD)
            EigenmathResultYT = eigenmath.run(EigenmathCMD )
            #print(EigenmathResultXT)
            YgraphList = eval('['+EigenmathResultYT+']')
            #print(YgraphList)
            for self.Tpixel in range (0,319):
                Ygraph=YgraphList[self.Tpixel]
                Ypixel=(Ygraph-rangoGraph['Ymax'])*218/(rangoGraph['Ymin']-rangoGraph['Ymax'])
                Xpixel = self.Tpixel
                if Ypixel >0 and Ypixel <=216 and Xpixel >0 and Xpixel <320 :
                    pointFuntion = lv.point_t()
                    pointFuntion.x=ceil(Xpixel)
                    pointFuntion.y=ceil(Ypixel)
                    points.append(pointFuntion)
                else :
                    if len(points)>0 :
                        self.listPto.append(points)
                        points = []
            if len(points)>0 :
                self.listPto.append(points)
                
                
    def execScreen(self):    
        rangoGraph=gal.data
        pointsY =  []
        pointsX =  []
        
        self.puntoLabel = None
        self.puntoCruz = None
        miTeclado = teclado.teclado()
        miTeclado.graphCursor = self.gestTeclado
        miTeclado.taWidget = None

        
        #Interfaz grafico
        self.miCabecera = guiHeader.guiHeader()
        self.miCabecera.strTitle="Galdeano graphics"
        self.miCabecera.setHeader()
       
        Xpixel0 =  rangoGraph['Xmin']*320/(rangoGraph['Xmin']-rangoGraph['Xmax'])  
        Ypixel0=-rangoGraph['Ymax']*218 / (rangoGraph['Ymin']-rangoGraph['Ymax'])
        
        
        p= lv.point_t()
        p.x=ceil(Xpixel0)
        p.y=0
        pointsY.append(p)
        p= lv.point_t()
        p.x=ceil(Xpixel0)
        p.y=216
        pointsY.append(p)
        
        
        p= lv.point_t()
        p.y=ceil(Ypixel0)
        p.x=0
        pointsX.append(p)
        p= lv.point_t()
        p.y=ceil(Ypixel0)
        p.x=318
        pointsX.append(p)
        
        style_line = lv.style_t()
        style_line.init()
        style_line.set_line_width(2)
        style_line.set_line_color(lv.palette_main(lv.PALETTE.BLUE))

        ejeX = lv.line(lv.scr_act())
        ejeX.set_points(pointsX,2)
        ejeX.align(lv.ALIGN.TOP_LEFT, 0, 22)
        ejeX.add_style(style_line, 0)
        ejeY = lv.line(lv.scr_act())
        ejeY.set_points(pointsY,2)
        ejeY.add_style(style_line, 0)
        ejeY.align(lv.ALIGN.TOP_LEFT, 0, 22)
        
        
        inic=time.time_ns()
        #calculamos los puntos de la grafica
        self.calcPoints2()
        print( time.time_ns() - inic )
        
#         calcPoints2()
#         920778000
#         824597000
#         823171000
#         calcPoints()
#         2274446000
#         2174546000
#         2191135000

        
        
        #ahora pintamos todas las lineas que hay en las listas de puntos
        for points in self.listPto:
            #print( len(points) )
            line1 = lv.line(lv.scr_act())
            line1.set_points(points, len(points) )
            points.clear()
            line1.align(lv.ALIGN.TOP_LEFT, 0, 22)
        
        ejeLabel = lv.label(lv.scr_act())
        ejeLabel.set_text(str(rangoGraph['Xmin']))
        ejeLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 0, ceil(Ypixel0)+22)
        ejeLabel = lv.label(lv.scr_act())
        ejeLabel.set_text(str(rangoGraph['Xmax']))
        ejeLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 300, ceil(Ypixel0)+22)
        ejeLabel = lv.label(lv.scr_act())
        ejeLabel.set_text(str(rangoGraph['Ymax']))
        ejeLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, ceil(Xpixel0) , 22)
        ejeLabel = lv.label(lv.scr_act())
        ejeLabel.set_text(str(rangoGraph['Ymin']))
        ejeLabel.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, ceil(Xpixel0), 216)

#####################################
#
#           Configuracion
#
#####################################

    def setGraph(self,event,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT):
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
        self.clearScreen()
        self.execScreen()


    def saveDataGraf(self,event,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT):
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

    def cb_event_handler(self,e,ta,taXT,taYT):
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


    
    def execScreenConf(self):
        self.miCabecera.strTitle="Galdeano graphics"
        self.miCabecera.setHeader()

        data = gal.data
    
        miTeclado = teclado.teclado()
        miTeclado.graphCursor = None

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
        taXT.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        taXT.set_text( str(data["function_x_t"]) )
        taYT = lv.textarea(lv.scr_act())
        taYT.align(lv.ALIGN.TOP_LEFT, 160, 23)
        taYT.set_one_line(True)
        taYT.set_width(145)
        taYT.set_placeholder_text( "y(t)=")
        taYT.add_style(styleTAInput, 0)
        taYT.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        taYT.set_text( str(data["function_y_t"]) )

        #definimos el interfaz para funciones normales
        
        ta = lv.textarea(lv.scr_act())
        ta.align(lv.ALIGN.TOP_LEFT, 10, 23)
        ta.set_one_line(True)
        ta.set_width(290)
        ta.set_placeholder_text( "f(x)=")
        ta.add_style(styleTAInput, 0)
        ta.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
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
        ta2.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        ta3 = lv.textarea(lv.scr_act())
        ta3.align(lv.ALIGN.TOP_LEFT, 190, 66)
        ta3.set_one_line(True)
        ta3.set_width(100)
        ta3.set_placeholder_text( "Min X")
        ta3.set_text( str(data["Xmin"] ))
        ta3.add_style(styleTAInput, 0)
        ta3.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
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
        ta4.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        ta5 = lv.textarea(lv.scr_act())
        ta5.align(lv.ALIGN.TOP_LEFT, 190, 106)
        ta5.set_one_line(True)
        ta5.set_width(100)
        ta5.set_placeholder_text( "Min Y")
        ta5.set_text( str(data["Ymin"]) )
        ta5.add_style(styleTAInput, 0)
        ta5.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        ta6 = lv.textarea(lv.scr_act())
        ta6.align(lv.ALIGN.TOP_LEFT, 90, 146)
        ta6.set_one_line(True)
        ta6.set_width(100)
        ta6.set_placeholder_text( "Max T")
        ta6.set_text( str(data["Tmax"]) )
        ta6.add_style(styleTAInput, 0)
        ta6.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        ta7 = lv.textarea(lv.scr_act())
        ta7.align(lv.ALIGN.TOP_LEFT, 190, 146)
        ta7.set_one_line(True)
        ta7.set_width(100)
        ta7.set_placeholder_text( "Min T")
        ta7.set_text( str(data["Tmin"]) )
        ta7.add_style(styleTAInput, 0)
        ta7.add_event_cb(lambda e: self.ta_event_cb(e,miTeclado), lv.EVENT.ALL, None)
        
        ta8 = lv.checkbox(lv.scr_act())
        ta8.set_text("Par")
        ta8.add_event_cb(lambda e: self.cb_event_handler(e,ta,taXT,taYT), lv.EVENT.ALL, None)
        ta8.add_state(data["parametric"])
        ta8.align(lv.ALIGN.TOP_LEFT, 10, 146)
        
        btn1 = lv.btn(lv.scr_act())
        btn1.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 1, 212)
        btn1.set_size(75,25)
        label_btn1 = lv.label(btn1)
        label_btn1.align_to(btn1, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn1.set_text("Graph")
        btn1.add_event_cb(lambda e: self.setGraph(e,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT), lv.EVENT.CLICKED, None)
        
        btn2 = lv.btn(lv.scr_act())
        btn2.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 81, 212)
        btn2.set_size(75,25)
        label_btn2 = lv.label(btn2)
        label_btn2.align_to(btn2, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn2.set_text("Funct")
        btn2.add_event_cb(lambda e: self.dic(e,ta,btn2) , lv.EVENT.CLICKED, None)
        
        btn3 = lv.btn(lv.scr_act())
        btn3.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 161, 212)
        btn3.set_size(75,25)
        label_btn3 = lv.label(btn3)
        label_btn3.align_to(btn3, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn3.set_text( "Trigon" )
        btn3.add_event_cb(lambda e: self.trig2(e,ta), lv.EVENT.CLICKED, None)
        
        btn4 = lv.btn(lv.scr_act())
        btn4.align_to(lv.scr_act(), lv.ALIGN.TOP_LEFT, 240, 212)
        btn4.set_size(75,25)
        label_btn4 = lv.label(btn4)
        label_btn4.align_to(btn4, lv.ALIGN.TOP_LEFT, 0, -4)
        label_btn4.set_text("Save")
        btn4.add_event_cb(lambda e: self.saveDataGraf(e,ta,ta2,ta3,ta4,ta5,ta6,ta7,ta8,taXT,taYT), lv.EVENT.CLICKED, None)
