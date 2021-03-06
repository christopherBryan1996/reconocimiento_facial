import cv2 as cv
import os 
#import imutils

modelo='/fotosElon'
ruta1='reconocimiento_facial/proye1'
rutacomple=ruta1+modelo
if not os.path.exists(rutacomple):
    os.makedirs(rutacomple)

camara = cv.VideoCapture('reconocimiento_facial\proye1\ElonMusk.mp4')
ruidos=cv.CascadeClassifier('reconocimiento_facial\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')

id=0
while True:
    respuesta,captura=camara.read()
    if respuesta==False:print('dd') ;break
    #captura=imutils.resize(captura,width=640)
    gris=cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    idcaptura=captura.copy()

    cara=ruidos.detectMultiScale(gris,1.2,5)

    for (x,y,e1,e2) in cara:
        cv.rectangle(captura,(x,y),(x+e1,y+e2),(220, 79, 27),2)
        rostrocapturado=idcaptura[y:y+e2,x:x+e1]
        rostrocapturado=cv.resize(rostrocapturado,(160,160),interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutacomple+'/imagen_{}.jpg'.format(id),rostrocapturado)
        id=id+1
    cv.imshow('Resuktado de retro', captura)

    if id==351:
        break
camara.release()
cv.destroyAllWindows()