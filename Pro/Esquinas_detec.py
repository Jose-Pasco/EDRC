#############################Imagen
import numpy as np
import cv2 
import math
import pandas as pd
from matplotlib import pyplot as plt


img=cv2.imread('img/img_c_ilu_c/30_c.jpg')
#imgR=img[700:200,1500:2500]
#cv2.imwrite('imagen.jpg',imgR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR a escala de gris
corners = cv2.goodFeaturesToTrack(gray,15,0.01,10)
cornersIn = np.int0(corners)

imgIlu=cv2.imread('img/img_b_ilu_c/30_c.jpg')

grayIlu=cv2.cvtColor(imgIlu,cv2.COLOR_BGR2GRAY) 
cornersIlu= cv2.goodFeaturesToTrack(grayIlu,15,0.01,10)
cornersInIlu = np.int0(cornersIlu)

xAlmI=[]
yAlmI=[]

for k in cornersInIlu:
    i,j = k.ravel()
    xAlmI.append(i)
    yAlmI.append(j)
    m=cv2.circle(imgIlu,(i,j),15,255,-1)

xAlm=[]
yAlm=[]

for i in cornersIn:
    x,y = i.ravel()
    xAlm.append(x)
    yAlm.append(y)
    n=cv2.circle(img,(x,y),15,255,-1)    



figura=plt.figure(figsize=(30,30))
figura.tight_layout()
figura.suptitle('Comparación de imágenes', fontsize=16)

plt.subplot(2,2,1)
plt.title('Cilindro')
plt.imshow(cv2.imread('img/img_c_ilu_c/30_c.jpg'))

plt.subplot(2,2,2)
plt.title('Cilindro KP')
plt.imshow(n)

plt.subplot(2,2,3)
plt.title('Prisma Rectangular')
plt.imshow(cv2.imread('img/img_b_ilu_c/30_c.jpg')) 

plt.subplot(2,2,4)
plt.title('Prisma RectangularKP')


####################Muestrad de datos

puntos=np.transpose([xAlm,yAlm,xAlmI,yAlmI])

strPo=['x1','y1','x2','y2']
k=pd.DataFrame(data=puntos,columns=strPo)


#k.to_excel(r'E:/2020_1/Metodologia de la investigacion/Datos/datos_20_Rec_Cir.xlsx',index=True,header=True)


print(k)


plt.imshow(m)
plt.show()














####################funciones
def imprimir(direc):
    rea=cv2.imread(direc)
    im=cv2.imshow('img',rea)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rea
def distancia(p0,p1):
    x0=p0[0]
    y0=p0[1]
    
    x1=p1[0]
    y1=p1[1]
    
    sum2=(x1-x0)**2 +(y1-y0)**2
    
    d=math.sqrt(sum2)
    return d
def imagen_GRAY(num):
    imgRead=cv2.cvtColor(num,cv2.COLOR_BAYER_BG2GRAY)
    plt.imshow(imgRead)
    #gray=cv.cvtColor(imgRead,cv.COLOR_BGR2GRAY) #BGR a escala de gris
    return imgRead
def recorte(inImage):
    imageOut=inImage[700:200,1500:2500]
    return imageOut
    
    
