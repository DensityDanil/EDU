import numpy as np

s = np.random.normal(loc=60,scale=5,size=10**3)
res = [np.mean(s[:i]) for i in range(1,len(s)+1)]


#https://stackoverflow.com/questions/21142149/calculate-an-incremental-mean-using-python-pandas

