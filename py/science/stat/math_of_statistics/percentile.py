import random as r
import numpy as np
#https://stackoverflow.com/questions/2374640/how-do-i-calculate-percentiles-with-python-numpy
#Boris Gorelik
import matplotlib.pyplot as plt


lst = [i+10 for i in range(10)]
#[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

percentiles = list(range(100,49,-1))

out = []

c=0
for i in percentiles:
    p = np.percentile(lst,i)
    out.append(p)
    if c!=0:
        print( i,p
              #,out[-2]
              #,out[-1]
               )
    c+=1


x = out
y = percentiles

plt.plot(x)
plt.show()
