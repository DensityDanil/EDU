import os
import pandas as pd
data = []

for i in os.listdir():
    if '.tsv' in i:
        df = pd.read_csv(i,sep='\t')
        data.append(df)
        print(i,len(df))
        #df.info()
        print(i.replace('.tsv',''),end=', ')


actor, film, film_actor, inventory, rental = data
