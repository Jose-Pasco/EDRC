'''
Created on 6 set. 2020

@author: ACER
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt

datos=pd.read_csv('area.csv',sep=';')
df=pd.DataFrame(datos)
x=df['lg']
y=df['ds']

x1=df['lg']
y1=df['ds']

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
X_train=X_train.values.reshape([X_train.values.shape[0],1])
X_test=X_test.values.reshape([X_test.values.shape[0],1])


titles=['Grado 0','Grado 1','Grado 2','Grado3','Grado 4','Grado 5','Grado 6']
colors=['darkred','orange','darkorchid','orchid','aqua','green','blue']

for i in range (1,7):
    poly_features=PolynomialFeatures(degree=i)
    X_poly=poly_features.fit_transform(X_train)
    Xt_poly=poly_features.fit_transform(X_test)
    poly_model=LinearRegression()
    poly_model.fit(X_poly,y_train)
    pred=poly_model.predict(X_poly)
    pred2=poly_model.predict(Xt_poly)
    xt,yt=zip(*sorted(zip(X_test,pred2)))
    X,y=zip(*sorted(zip(X_train,pred)))
    plt.subplot(2,3,i)
    print('a:'+str(i))
    print (poly_model.coef_)
    print('b:')
    print(poly_model.intercept_)
    plt.plot(X,y,'-',color=colors[i],label=titles[i],markersize=3)
    plt.plot(xt,yt,'+',color='turquoise',markersize=5)
    plt.plot(x1,y1,'*',color='crimson',markersize=3)
    plt.legend(loc=2)
    plt.xlabel('Log(P)')
    plt.ylabel('Distancia(cm)')
plt.show()

    
            