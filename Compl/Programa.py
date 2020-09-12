#HARRIS corner
#
import cv2
import numpy as np


img = cv2.imread('vs_wapp.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)  #Harris works on float32 images. 

#Input parameters
# image, block size (size of neighborhood considered), ksize (aperture parameter for Sobel), k
harris = cv2.cornerHarris(gray,2,3,0.04)  

# Threshold for an optimal value, it may vary depending on the image.
img[harris>0.01*harris.max()]=[255,0,0]    # replace these pixels with blue

cv2.imshow('Harris Corners',img)
cv2.waitKey(0)