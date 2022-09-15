import lvgl as lv
import os
import eigenmath
from math import ceil,sin,cos,tan,log,sqrt,exp,pi
import random
import teclado
import galdeanolib as gal
import json
import guiHeader

Tpixel=0
puntoLabel = None
puntoCruz = None
def gestTeclado(key):
    global Tpixel,puntoLabel,puntoCruz
    
    line_points = [ {"x":0, "y":0}, 
                {"x":0, "y":4}, 
                {"x":4, "y":4}, 
                {"x":4, "y":0}, 
                {"x":0, "y":0}]
    
    if(key=="del"):
        puntoLabel.delete()
        puntoCruz.delete()
        puntoLabel = None
        return
    if(key=="left"):
        Tpixel=Tpixel-1
        if Tpixel<=0:
            Tpixel=0
    elif(key=="rigth"):
        Tpixel=Tpixel+1
        if Tpixel>=320:
            Tpixel=320
    if puntoLabel == None:
        #puntoLabel.delete()
        puntoLabel = lv.label(lv.scr_act())
        puntoLabel.set_recolor(True)
        puntoCruz = lv.line(lv.scr_act())
        puntoCruz.set_points(line_points, 5)
    rangoGraph=gal.data
    if rangoGraph["parametric"] == lv.STATE.CHECKED:
        FXT=rangoGraph['function_x_t']
        FYT=rangoGraph['function_y_t']
    else:
        F=rangoGraph['function']
    if rangoGraph["parametric"] == lv.STATE.CHECKED:
        Tgraph=rangoGraph['Tmin']+(rangoGraph['Tmax']-rangoGraph['Tmin'])*Tpixel/320
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
        Xpixel=Tpixel
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
    puntoLabel.set_pos(ceil(Xpixel+Xoffset), ceil(Ypixel+Yoffset))
    puntoCruz.set_pos(ceil(Xpixel)-2, ceil(Ypixel)+20)
    print("Set text : "+str(Xpixel)+","+str(Ypixel) + "T:"+ str(Tpixel))
    puntoLabel.set_text("#ff0000 ("+str( Xgraph )+","+str( Ygraph )+")#")


#####################################
#
#           GRAFICOS
#
#####################################

def execScreen():
    global puntoLabel,puntoCruz
    
    rangoGraph=gal.data
    points =  [ ]
    pointsY =  []
    pointsX =  []
    puntoLabel = None
    puntoCruz = None
    miTeclado = teclado.teclado()
    miTeclado.graphCursor = gestTeclado
    miTeclado.taWidget = None
    #Interfaz grafico
    miCabecera = guiHeader.guiHeader()
    miCabecera.strTitle="Galdeano graphics"
    miCabecera.setHeader()
   
    Xpixel0 =  rangoGraph['Xmin']*320/(rangoGraph['Xmin']-rangoGraph['Xmax'])  
    print( Xpixel0 )

    Ypixel0=-rangoGraph['Ymax']*218 / (rangoGraph['Ymin']-rangoGraph['Ymax'])
    print( Ypixel0 )
    
    
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
    
    if rangoGraph["parametric"] == lv.STATE.CHECKED:
        FXT=rangoGraph['function_x_t']
        FYT=rangoGraph['function_y_t']
    else:
        F=rangoGraph['function']
#        print(F)
    #definimos la funcion a graficar
#     EigenmathCMD='F(x)='+rangoGraph['function']
#     EigenmathResult = eigenmath.run(EigenmathCMD )
#     print(EigenmathResult )
    numPoints=0
    for Tpixel in range (0,319):
        if rangoGraph["parametric"] == lv.STATE.CHECKED:
            Tgraph=rangoGraph['Tmin']+(rangoGraph['Tmax']-rangoGraph['Tmin'])*Tpixel/320
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
            Xpixel=Tpixel
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
                line1 = lv.line(lv.scr_act())
                line1.set_points(points, len(points) )
                points.clear()
                line1.align(lv.ALIGN.TOP_LEFT, 0, 22)
    #si hay algun punto ... hay que dibujarlo
    if len(points)>0 :
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
