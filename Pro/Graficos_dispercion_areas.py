
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

datos=pd.read_csv('area.csv',sep=';')

df=pd.DataFrame(datos)
x=df['px']
y=df['ds']

plt.plot(x,y,'gs',color='g')

plt.xlabel("Pixel", size = 14)
plt.ylabel("Distancia", size = 14)

plt.title('Grafica de dispersión')

#plt.legend(('Prisma Rectangular','Cilindro'),loc='lower right')
plt.grid()
plt.show()


