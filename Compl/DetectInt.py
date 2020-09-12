
#Deteccion de puntos caracteristicos con el metodo SIFT

import numpy as np
import cv2
from matplotlib import pyplot as plt
from cv2 import waitKey

img=cv2.imread("img/img_p_ilu/15.jpg",cv2.IMREAD_GRAYSCALE)

sift=cv2.xfeatures2d.SIFT_create()

keypoints, descriptors=sift.detectAndCompute(img,None)

img_kp=cv2.drawKeypoints(img,keypoints,None)

plt.imshow(img_kp)
plt.show()

