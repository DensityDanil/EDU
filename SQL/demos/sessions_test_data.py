from pandas import DataFrame

session = [1,1,2,3,3,4]
page = 'A,A,B,C,D,D'.split(',')
user = [100]*len(session)
date = [12]*len(session)
dt_timestamp = list(range(len(session)))

user = [100,100,100,100]
session = [1,1,2,2]
date = [12,12,12,12]
page = 'A,B,A,B'.split(',')
dt_timestamp = [1,2,3,4]

def gen_df(user,session,date,page,dt_timestamp):
    df = pd.DataFrame({"user":user
                   ,"session":session
                   ,"date":date
                   ,"page":page
                   ,"dt_timestamp":dt_timestamp})

    return df
