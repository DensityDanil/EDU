from pandasql import sqldf
import pandas as pd


data = [ (500,300,3)
        ,(500,400,2)
        ,(600,700,1)
        ,(600,800,4)
         ]

data = [ (500,300,3)
        ,(500,400,3)
         
        ,(600,700,1)
        ,(600,800,1)
         ]

df = pd.DataFrame(data)
df.columns = 'team_id,member_id,member_score'.split(',')

q=f'''
select
     df.*
    --
    ,row_number()
    over(partition by team_id
    order by member_score desc, team_id asc) rn
from df
'''
r = sqldf(q)

data = [ (500,'a',300,3)
        ,(500,'a',400,3)
         
        ,(600,'b',700,1)
        ,(600,'b',800,1)
         ]

df = pd.DataFrame(data)
df.columns = 'team_id,team_name,member_id,member_score'.split(',')

q=f'''
select
     df.*
    --
    ,row_number()
    over(partition by team_id,team_name
    order by member_score desc, team_id asc) rn
from df
'''
r1 = sqldf(q)
