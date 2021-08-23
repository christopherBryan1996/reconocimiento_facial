import cv2

PATH = 'reconocimiento_facial\monedasContorno\contorno.jpg'
image = cv2.imread(PATH)#colocamos la imagen para ver

if image is None:#si la variable image no tiene una imagen imprimira lo siguiente
    print('Error durante la lectura de la imagen')
else:# si no tiene error ejecutara lo siguiente 
    grises=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#trasformamps la imagen en grises
    tipo,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)#esta fincion nos arroja dos valores una el tipo y el otro el umbral por eso
    #se declaran dos variables pero si no quieres poner un nombre solo con poner un _,umbral te lo toma como correcto
    contornos,jerarquias= cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)#le indicamos como detectara el contorno de la imagen
    cv2.drawContours(image,contornos,-1,(195, 125, 245),3)#nos dibuja todos los contornos con -1 y si queremos señalar uno se puede poner la posicion
    cv2.imshow('Imagen original', image)#la mostramos
    cv2.imshow('imagen en grises', grises)
    cv2.imshow('umbral',umbral)
    cv2.waitKey(0)#nos ayudara a detener la imagen con 0 y se puede poner 1 para videos
    cv2.destroyAllWindows()#nos ayuda destuir varias ventanas
