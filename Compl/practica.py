#############################Imagen
import numpy as np
import cv2 
import math
import pandas as pd
from matplotlib import pyplot as plt
'''
v=np.arange(10)
x=np.matrix(len(v),)
for i in v:  
    img=cv2.imread('img/img_p_n/v.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR a escala de gris
    corners = cv2.goodFeaturesToTrack(gray,15,0.01,10)
    cornersIn = np.int0(corners)'''


img=cv2.imread('img/img_p_n/15.jpg')
imgR=img[700:200,1500:2500]
cv2.imwrite('imagen.jpg',imgR)
k=cv2.imread('imagen.jpg')
cv2.imshow('th',k)
cv2.waitKey(0)
cv2.destroyAllWindows()