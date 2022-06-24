
#t
#y

import numpy as np 
from numpy import linalg

#b=np.array(np.random.rand(9))
#print(b.reshape(3,3))

a=np.array([[.25,.25,.75],[.10,.10,.80],[.20,.20,.60]])

print(a.dot(a))
for i in range(10):
	a=a.dot(a)	 	  


print(a)	