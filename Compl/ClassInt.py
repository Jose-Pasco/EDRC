'''
Created on 30 ago. 2020

@author: ACER
'''
#Intento de abrir imagenes con python
import cv2 
from matplotlib import pyplot as plt




def imprimir(direc):
    rea=cv2.imread(direc)
    im=cv2.imshow('img',rea)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rea

def corn(ka):
    xAlm=[]
    yAlm=[]
    i=0
    for i in cornersIn:
        x,y = i.ravel()
        xAlm.append(x)
        yAlm.append(y)
        n=cv2.circle(ka,(x,y),15,255,-1)
        
'''k=cv2.imread('img/img_prueba/imagen_moneda.jpg')
j=imprimir(k)
z=cv2.cvtColor(j,cv2.COLOR_BGR2GRAY)
cv2.imshow('k',z)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

m=imprimir('img/img_prueba/imagen_moneda.jpg')


gray=cv2.cvtColor(m,cv2.COLOR_BGR2GRAY) #BGR a escala de gris
corners = cv2.goodFeaturesToTrack(gray,15,0.01,10)
#cornersIn = np.int0(corners)



        
        