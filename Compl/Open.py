import cv2
import numpy
from matplotlib import pyplot as plt

def main():
    img=cv2.imread('moneda.jpg')
    img=cv2.imread('moneda.jpg',cv2.IMREAD_GRAYSCALE)
    
    cv2.imwrite('imagen_moneda.jpg',img)
    
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    matplotlib()
    
    return
def matplotlib():
    img=cv2.imread('moneda.jpg')
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.show()
    return
if __name__=='__main__':
    main()
    