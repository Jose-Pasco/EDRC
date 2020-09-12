
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('moneda.jpg',0)

# Iniciar objeto FAST con valores propuestos
fast = cv2.FastFeatureDetector_create()

# encontrar y dibujar los puntos clave
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp,img)

cv2.imwrite('moneda_nueva.jpg',img2)

# desactiva nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)