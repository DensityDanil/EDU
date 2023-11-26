from duckdb import sql
import os
import pandas as pd

df = pd.DataFrame([ (200)
                   ,(300)])

df.columns = 'col1'.split(',')

sql('''
with df1 as 
(select col1 from df)

,df2 as 
(select 
col1,col2 
from df)

,df3 as (
select col1+col2
from df1
join df2 using col1 using(col1)
)

select *
from df3
''').df()

