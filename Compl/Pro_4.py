import cv2

imagen=cv2.imread('15.jpg')

grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
bordes=cv2.Canny(grises,100,200)

ctns,_=cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, ctns,-1,(0,0,255),2)
print('Numero de contornos encontrados:',len(ctns))
texto='Contornos encontrados: '+str(len(ctns))

cv2.putText(imagen,texto,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),1)


cv2.imshow('Bordes',bordes)
cv2.imwrite('Img.jpg',imagen)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()