import pandas as pd



data = [(None,None),(1,0),(0,0),(0,1),(0,0),(1,1)]
data = [(None,1)]
df = pd.DataFrame(data)

struct = df.values



comb = 0
for row in struct:
    row = [0 if (k==None or str(k)=='nan') else 1 for k in row]
    row_lst = list(map(str,row))
    comb = ''.join(row_lst)
    print(comb)
    
    
        
        
bool_consts = [0,1,None]
##0 0
##0 1
##0 None
##1 0
##1 1
##1 None
#None 0
#None 1
#None None

#bool_consts = [0,1]
##0 0  'followers_count', 'view_count' 
##0 1  'view_count' 
##1 0  'followers_count'
##1 1
for i in bool_consts:
    for j in bool_consts:
        print(i,j)
