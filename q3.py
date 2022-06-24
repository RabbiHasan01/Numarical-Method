
#t
#y

import numpy as np 
from numpy import linalg
#a=np.array(np.random.rand(9))
#b=np.array(np.random.rand(9))
#c=np.array(np.random.rand(9))
#a.reshape(3,3)
#b.reshape(3,3)
#c.reshape(3,3)
a=np.array([[1,2,3],[5,3,2],[2, 1 ,5]])
b=np.array([[2,3,5],[1,4,4],[7,6,2]])
c=np.array([[3,4,5],[1,3,2],[4,3,5]])

print(a.dot(b+c)) 

print((a.dot(b)+a.dot(c)))

print((a.dot(b+c))==(a.dot(b)+a.dot(c)))

