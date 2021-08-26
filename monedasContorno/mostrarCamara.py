import cv2 as cv
#buscamos una camara 
capturaVideo = cv.VideoCapture(1)#0nos da la camara de la lap y 1 para externas 

if not capturaVideo.isOpened():
    print('No se encontro una camara')
    exit()
while True:
    tipocamara,camara=capturaVideo.read()
    gris=cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
    cv.imshow('en vivo', gris)
    if cv.waitKey(1)==ord('q'):
        break
capturaVideo.release()
cv.destroyAllWindows()
