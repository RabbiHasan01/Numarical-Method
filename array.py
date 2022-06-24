

import numpy as np 

a=np.array([1,2,3,4,5,6,7])
print(a)
b=np.array([1,2,3,4])
print(b)
print(b.ndim) #dimension
print(b.shape);
print(len(a))

#2d arr

c=np.array([[1,2,3,4,5],[2,5,7,8,7]])
print(c)
print(len(c))
print(c.shape)
print(c.ndim)

#ones
one=np.ones((3,3)) #row,col;one matrix
print(one)
print(len(one))

print(2*one)
print(one/3)
#zeros

z=np.zeros((3,4))
print(z)
print(z-3)

#identity

i=np.eye(3)
print(i)

# diagonal....
m=np.diag(np.array([2,3,-4,6,8]))
print(m)
print(m.max())
x=np.linspace(1,10) #first,last
print(x)

x=np.linspace(1,10,5)
print(x)

p=np.array(x)
print(x)