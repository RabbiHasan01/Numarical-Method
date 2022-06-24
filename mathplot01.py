
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2, 4, 20)
y=np.linspace(0,56,20)
plt.plot(x,y)
plt.plot(x,y,'o')
plt.show()

X = np.linspace(-np.pi, np.pi, 556)
C, S ,T,s,c,ct= np.cos(X), np.sin(X),np.tan(X),1/np.cos(X),1/np.sin(X),1/np.tan(X)
plt.plot(X, C)
plt.show()
plt.plot(X, S)
plt.show()
plt.plot(X,T)
plt.show()
plt.plot(X,ct)
plt.show()
plt.plot(X,c)
plt.show()
plt.plot(X,s) 
plt.show()
