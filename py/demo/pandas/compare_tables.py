import pandas as pd

def compare_df(df1,df2,to_compare=None):

    common_cols = list(set(df1.columns)&set(df2.columns))

    union_samples = pd.concat([ df1.assign(table_suffix='left')
                               ,df2.assign(table_suffix='right')])
    
    for i in common_cols:
        group_cols = [k for k in common_cols if k!=i]
        pivot = pd.pivot_table( data=union_samples
                            ,index=group_cols
                            ,columns = 'table_suffix'
                            ,values = i
                            
                            ,aggfunc = lambda x: len(x.unique()) if dtype() #note(1) count unique
                                
                            ).reset_index()
        print(pivot)
    
    return union_samples


df1 = pd.DataFrame({'name' : ["Alex", "Bob", "Carmen", "Diaz", "Ella","Forman", "Glen"],
                   'age' : [20, 27, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]})


df2 = pd.DataFrame({'name' : ["AlEx", "Bob", "Carmen", "Diaz", "Ella","Forman", "Glen"],
                   'age' : [20, 29, 35, 55, 18, 21, 35],
                   'designation': ["VP", "CEO", "CHMO", "VP", "VP", "CEO", "MD"]})



df = compare_df(df1,df2)
