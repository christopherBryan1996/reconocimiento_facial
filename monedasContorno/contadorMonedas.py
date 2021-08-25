import cv2
import numpy as np
valorGauss=3
valorKernel=3
original = cv2.imread('reconocimiento_facial\monedasContorno\monedas.jpg')

if original is None:
    print('Error')
else:
    gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)#se creala imagen en gris 
    gauss=cv2.GaussianBlur(gris,(valorGauss,valorKernel),0)#primera eliminacion de ruidos
    canny=cv2.Canny(gauss,60,100)#seginda eliminacion de ruido
    kernel=np.ones((valorKernel,valorKernel), np.uint8)#le damos el tamaño de la matriz
    cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)#le quitamos el ruido de adentro del contorno
    contornos, jerarquia= cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print('monedas encontradas: {}'.format(len(contornos)))
    cv2.drawContours(original,contornos,-1,(0,0,255),2)
    #mostrar
    cv2.imshow('imagen gris',gris)
    cv2.imshow('imagen de Gauss', gauss)
    cv2.imshow('imagen de canny',canny)
    cv2.imshow('cierre',cierre)
    cv2.imshow('resultado',original)
    cv2.waitKey(0)