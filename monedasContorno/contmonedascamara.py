import cv2 as cv
import numpy as np
from numpy.lib.function_base import append

def ordenarpuntos(puntos):
    #tendremos cuatro puntos del objeto que en este caso sera un circulo
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
    y_order= sorted(n_puntos,key=lambda n_puntos: n_puntos[1])
    x1_order= y_order[:2]
    x1_order=sorted(x1_order,key=lambda x1_order:x1_order[0])
    x2_order= y_order[2:4]
    x2_order= sorted(x2_order,key=lambda x2_order:x2_order[0])
    return[x1_order[0],x1_order[1],x2_order[0],x2_order[1]]

def alineamiento(imagen,ancho,alto):
    imagen_alineada= None
    grises=cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    tipoumbral,umbral=cv.threshold(grises,150,255,cv.THRESH_BINARY)
    cv.imshow('Umbral',umbral)
    contorno=cv.findContours(umbral,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contorno= sorted(contorno,key=cv.contourArea,reverse=True)[:1]
    for c in contorno:
        epsilon=0.01*cv.arcLength(c, True)
        aproximacion=cv.approxPolyDP(c,epsilon,True)
        if len(aproximacion)==4:
            puntos=ordenarpuntos(aproximacion)
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            M=cv.getPerspectiveTransform(puntos1,puntos2)#nos ayuda para cuando la camara este en movimiento
            imagen_alineada=cv.warpPerspective(imagen,M,(ancho,alto))
    return imagen_alineada

capturavideo= cv.VideoCapture(1)
while True:
    tipocamara, camara=capturavideo.read()
    if tipocamara == False:
        break
    imagen_A6=alineamiento(camara,ancho=480,alto=677)
    if imagen_A6 is not None:
        puntos=[]
        gris=cv.cvtColor(imagen_A6,cv.COLOR_BGR2GRAY)
        cv.blur=cv.GaussianBlur(gris,(5,5),1)
        _,umbral2=cv.threshold(cv.blur,0,255,cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
        cv.imshow('Umbral', umbral2)
        contorno2=cv.findContours(umbral2, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(imagen_A6,contorno2,-1,(195, 125, 245),2)
        suma1=0.0
        suma2=0.0
        for c_2 in contorno2:
            area=cv.contourArea(c_2)
            Momentos = cv.moments(c_2)
            if Momentos["m00"]==0:
                Momentos['m00']=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])

            #moneda de 2=415.4756*10.5/480=9.08*1000=9080

            #moneda de 10=706.8583*10.5/480=15.46*1000=15460
            if area<15500 and area>15300:
                font =cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$10",(x,y),font,0.75,(0,255,0),2)
                suma1= suma1+0.2

            if area<9150 and area>8999:
                font =cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6,"$2",(x,y),font,0.75,(0,255,0),2)
                suma2= suma2+0.1
        total = suma1+ suma2
        print('el total es: ', round(total,2))
        cv.imshow('imagen A6',imagen_A6)
        cv.imshow('camara', camara)
    if cv.waitKey(1) == ord('s'):
        break
capturavideo.release()
cv.destroyAllWindows()