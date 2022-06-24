

import numpy as np 

a=np.diag(np.arange(5))
print(a)

a[1,2]=10 #2nd row,3rd col is changed....
print(a)

print(a[1]) # output=2nd row 

b=np.arange(10) #0 to 6
print(b)

print(b[2:5]) # 2=start, end before 5 - 2,3,4

print(b[:7:2])


print(b[:7:2].min())
print(b[:7:2].max())

print(b.min())

#reverse
print(b[::-1]) # -1 reverse array

c=np.arange(1,100,10) # start , end , range
print(c)
print(len(c))

print(b*c)


