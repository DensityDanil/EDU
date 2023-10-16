import pandas as pd
from pandasql import sqldf

session = [1,1,1,3,3,4]
page = 'A,A,B,C,D,D'.split(',')
user = [100]*len(session)
date = [12]*len(session)
dt_timestamp = list(range(len(session)))


df = pd.DataFrame({"user":user
                   ,"session":session
                   ,"date":date
                   ,"page":page
                   ,"dt_timestamp":dt_timestamp})

#note problem to solve
partition_list = 'partition by user,session,date order by dt_timestamp asc'
q = f'''
with
tmp as
(select
 df.*
,lead(page,1) over({partition_list}) as shft
from df)

select *
from tmp
'''
r = sqldf(q)
