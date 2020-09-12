'''
Created on 27 jul. 2020

@author: ACER
'''
import cv2
import xlrd
import pandas as pd
'''imagen=cv2.imread('moneda.jpg')
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(grises,240,255,cv2.THRESH_BINARY_INV)
_,cnts,_=cv2.findContours(th, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen,cnts,-1,(255,0,0),2)

cv2.imshow('imagen',imagen)
cv2.imshow('th',th)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
datos=pd.read_csv('DatosDePrueba.csv')