

import cv2 
import numpy as np
import imutils
from cv2 import INTER_CUBIC, COLOR_RGB2GRAY
from numpy import shape
image=cv2.imread('img/img_p_n/15.jpg')
#print('image.shape=',image.shape) #las dimensiones de la imagen
'''ancho=image.shape[1] # columnas
alto=image.shape[0] #filas

#traslacion
M=np.float32([[1,0,100],[0,1,100]])

imageOut=cv2.warpAffine(image,M,(ancho,alto))


M=cv2.getRotationMatrix2D((ancho//2,alto//2),15,1) #15 grados, 1 escala


imageOut=cv2.warpAffine(image,M,(ancho,alto))

#redimensionar 

#imageOut=cv2.resize(image,(600,300),interpolation=cv2.INTER_CUBIC)

#imutils
imageOut=imutils.resize(image,width=300)#reescala la imagen con un ancho de 300'''

imageY=image[700:2000,1500:2500]
imaa=cv2.cvtColor(imageY,cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen moneda',image)
cv2.imshow('imagen de salida',imaa)
cv2.waitKey(0)
cv2.destroyAllWindows()