from duckdb import sql
import pandas as pd

df1 = pd.DataFrame([(1),(2)])
df2 = pd.DataFrame([(1),(3)])

df1.columns = ['id']
df2.columns = df1.columns

sql('''
select df2.id
from df2 left join df1 using(id)
where df2.id is null
''').df()

#>>>NULL