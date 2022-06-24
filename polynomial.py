

#3x**2+2x-1

import numpy as np 

p=np.poly1d([3,2,-1])
#p = np.poly1d([3, 2, -1])

print(p)
print(p(0))
print(p(2)) # when x=2,p(x)=15

print(p.roots)
print(p(-1))

print(p.order)
