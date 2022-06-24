

#y
#t
import numpy as np 
from numpy import linalg
import scipy as np 
from scipy import linalg

A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4,
8]])
b = np.array([1, 1, 1, 1])
lu, piv = linalg.lu_factor(A)
x = linalg.lu_solve((lu, piv), b)
print(x)
