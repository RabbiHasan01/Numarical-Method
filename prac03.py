
import numpy as np
import scipy as sc
import matplotlib as plt
x=5
print(np.linspace(0,10,11))

functions = [np.sin(x), np.cos(x), np.exp(x), np.log(x)]
titles = ['Sine function', 'Cosine function', 'Exponential function', 'Logarithmic function']
    
for i in functions:
	print(i)
x = np.array([0.5])
print(x)
x = np.array([0.5])
bins = np.array([0,1,2,3])
x = np.array([-0.5,1,3.5])
np.digitize(x,bins)
print(bins)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()