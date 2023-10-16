import pandas as pd


data = [(None)]

df = pd.DataFrame(data)

df.columns = ['Followers']


struct = df.iloc[0][0]#.tolist()[0][0]
#df
#struct==None #True
