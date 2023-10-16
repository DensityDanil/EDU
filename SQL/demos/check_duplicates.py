from pandasql import sqldf
from pandas import DataFrame

data = [(None,None,None),(None,None,None)]

df = DataFrame(data)

query = f'''
select *
from df
'''
pds_out = sqldf(query)
print(pds_out )
