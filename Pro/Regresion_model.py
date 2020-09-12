from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(4.77,6,0.01)
y1=x*(-39.96)+244.02
y2=22.29*(x**2)-271.94*x +845.45
y3=-6.06*(x**3)+117.55*x**2 - 770.17*x + 1712.21
plt.title('Grafica de los polinomios')
plt.plot(x,y1,linewidth=0.8,color='g')
plt.plot(x,y2,linewidth=0.8,color='r')
plt.plot(x,y3,linewidth=0.8,color='y')
plt.xlabel('Log(P)')
plt.ylabel('Distancia(cm)')
plt.legend(('p1','p2','p3'),loc=2)
plt.grid()
plt.show()