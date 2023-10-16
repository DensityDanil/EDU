import pandas as pd
import numpy as np


df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                   'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                   'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
                   'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                   'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']})

index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

filter_names = ["animal", "age"]
filter_values = ["cat", 3]


f1,f2 = filter_names 
v1,v2 = filter_values 

#df[f2].dropna()
print(df[ (df[f1]==v1 & df[f2]<v2 ) ])




