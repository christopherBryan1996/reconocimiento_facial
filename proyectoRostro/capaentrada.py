from turtle import width
import cv2 as cv
import os 
import imutils

modelo='fotosElon'
ruta1='C:/Users/manci/Documents/reconocimiento_facial/proyectoRostro'
rutacompleta=ruta1 +'/'+modelo

if not os.path.exists(rutacompleta):
    os.makedirs(rutacompleta)

ruidos= cv.CascadeClassifier('C:/Users/manci/Documents/reconocimiento_facial/opencv-master/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
camara=cv.VideoCapture('C:/Users/manci/Documents/reconocimiento_facial/proye1/ElonMusk.mp4')

id=0
while True:
    respuesta,captura=camara.read()

    if respuesta==False:break
    captura=imutils.resize(captura,width=640)
    grises=cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    idcaptura=captura.copy()
    cara=ruidos.detectMultiScale(grises,1.3,5) 

    for (x,y,e1,e2) in cara: 
        cv.rectangle(captura,(x,y),(x+e1,y+e2),(255,0,0),2)
        rostrocapturado= idcaptura[y:y+e2,x:x+e1]
        rostrocapturado=cv.resize(rostrocapturado,(160,160),interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutacompleta+'/imagen_{}.jpg'.format(id),rostrocapturado)
        id=id+1
    
    cv.imshow('resultado rostro',captura)

    if id==351:
        break
camara.release()
cv.destroyAllWindows()