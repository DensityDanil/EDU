import matplotlib.pyplot as plt
import numpy as np


def check_func(func,start=-100,stop=100):
    res = []
    for i in range(start,stop,1):
        try:
            val = i,func(i)    
            res.append(val)
        except Exception as e:
            print(e)
            res.append((i,None))

    res = np.array(res)
    x,y = res[:,0],res[:,1]
    
    plt.plot(x,y)
    plt.show()

def hyperbola_func(x):
    #https://stepik.org/lesson/255839/step/6?unit=236112
    y = (2/(x-1))+3
    return y
    


check_func(hyperbola_func)
