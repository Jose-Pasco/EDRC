'''
Created on 23 ago. 2020

@author: ACER
'''
import cv2
from matplotlib import pyplot as plt

j=cv2.imread('img_Canica.jpg')
k=[[1,0],[0,2]]


def imagen_GRAY(num):
    imgRead=cv2.cvtColor(num,cv2.COLOR_BAYER_BG2GRAY)
    plt.imshow(imgRead)
    #gray=cv.cvtColor(imgRead,cv.COLOR_BGR2GRAY) #BGR a escala de gris
    return imgRead