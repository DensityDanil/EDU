import random as r
import pandas as pd
import numpy





storage = []


step=10

for i in range(1,1001,step):
    
    row = step,[r.uniform(50,200+step) for i in range(10**6)]
    


check_bins = pd.Series(storage).value_counts(bins=5)


