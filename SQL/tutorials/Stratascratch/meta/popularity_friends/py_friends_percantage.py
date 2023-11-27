#https://docs.google.com/spreadsheets/d/1bBpmZ13eEL54n03JRaQv7FY6WVcP7yeip_rC-rcEIeU/edit#gid=0
import seaborn as sns

#tabulated data (columns are tab separated)
data = '''user1	user2
2	1
1	3
4	1
1	5
1	6
2	6
7	2
8	3
3	9'''

data_splitted = data.split('\n') #to_experiment what about 10**6 size table?

#build relational table slice headers
data_struct = tuple(row.split('\t') for row in data_splitted[1:])

#explain data
data_converted_struct = []
for i in data_struct:
    #convert types to make able plot numeric data
    data_converted_struct.append([int(j) for j in i]) #to_review how to append values to dataframe col?

sns.heatmap(pd.DataFrame(data_converted_struct))

#create list with all users 
au = tuple(row.split('\t')[0] for row in data_splitted[1:]) + tuple(row.split('\t')[1] for row in data_splitted[1:]) #to_review is there a way to filter with less steps?
audc = set(au)

#pemutate the pairs (reverse columns and concat both samples)
#u12c - user1 user2 concat
u12c = tuple((i[1],i[0]) for i in data_struct) + data_struct

#groupping
for user in sorted(set(tuple(i[0] for i in u12c) )):
    friend = tuple((i[1]) for i in u12c if i[0]==user)
    print(user,round(len(friend)/len(audc),3),sep='\t')
