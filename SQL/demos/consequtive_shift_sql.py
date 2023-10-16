import pandas as pd
from pandasql import sqldf

session = [1,2,3,5,6,7]

session = [1,2,3,4,5,6,55,7,8,9,10,11,12]
df = pd.DataFrame({"session":session})

partition_list = 'partition by session'
q = f'''
with
tmp as
(select
 df.*
,lead(session,1) over() as shft
,lead(session,1) over()-session as diff
,case when lead(session,1) over()-session=1
then
row_number() over() end as rn

from df
)

,un as
(
select session
from tmp
union
select shft
from tmp
)

select *
from tmp
'''
r = sqldf(q)
