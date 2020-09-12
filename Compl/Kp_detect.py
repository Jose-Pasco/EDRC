import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

img = cv2.imread('img/fotosDePrueba/15.jpg',cv2.IMREAD_GRAYSCALE)

#img2_rec=imutils.resize(img,width=300)

detector = cv2.FastFeatureDetector_create(25)   #detectar puntos

kp = detector.detect(img, None) #inicializando objeto

corners = np.int0(kp)
print(corners)
'''for i in corners:
    x,y = i.ravel()
    print(x,y)
    cv2.circle(img2_rec,(x,y),3,255,-1)'''

img2RecDraw=cv2.drawKeypoints(img, kp, None,flags=0)


plt.imshow(img2RecDraw)
plt.show()
imgSave=cv2.imwrite('15_kp.jpg',img2RecDraw)
cv2.waitKey(0)

'''
star = cv2.xfeatures2d.StarDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp1 = star.detect(img,None)

kp1, des = brief.compute(img, kp)
print( brief.descriptorSize() ) #32 bits
#print( des.shape ) #cantidad de puntos
#plt.imshow(l)
#plt.show() 
'''

    