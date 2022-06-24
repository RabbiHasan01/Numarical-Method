

import numpy as np 

a=np.array([1,2,3,4,4,5])
b=np.array([1,2,3,4,5,6])

#a==b # num wise copm...
print(a==b)
print(a+1)
print(a+b)
print((a+b).max())
print(a*b)
print(a/b)
#array_equal()-array wise comp....
print(np.array_equal(a,b))

#logical......op

a=np.array([0,0,1,1,0],dtype=bool)
b=np.array([1,0,0,1,1],dtype=bool)

print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.logical_not(a,b))
print(np.logical_xor(a,b))

x=np.arange(0,361,30)
print(x)
print(np.sin(x*np.pi/180))
print(np.cos(x*np.pi/180))
print(np.sin(x*np.pi/180)+np.cos(x*np.pi/180))

