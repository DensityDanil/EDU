# Import your libraries
# ref https://platform.stratascratch.com/coding/9633-city-with-most-amenities?code_type=2
import pandas as pd
import re
# Start writing code
airbnb_search_details.head()

out = {  'l':[]
        ,'l_set':[]
        ,'lst':[]
        ,'lst_set':[]
    }
c=0
for i in airbnb_search_details['amenities']:
    lst = i.split(',')
    #lst = i.replace('{','').replace('}','').split(',')
    
    lst = [k.strip() for k in lst]
    dup = [(k,lst.count(k)) for k in set(lst) if lst.count(k)>1]

    lst = sorted(lst)
    l = len(lst)
    lst_set = set(lst)
    l_set = len(lst_set)
    row = l,l_set,lst
    out['l'].append(l)
    out['l_set'].append(l_set)
    out['lst'].append(lst)
    out['l_set'].append(l_set)
    c+=1
    if len(dup)!=0:
        print(c,*dup)
    


airbnb_search_details['amenities_l'] = l
airbnb_search_details['amenities_total'] = airbnb_search_details['amenities_l'] + airbnb_search_details['cleaning_fee']+airbnb_search_details['bedrooms']+airbnb_search_details['beds']

airbnb_search_details.sort_values(by='cleaning_fee',ascending=False)

gb = airbnb_search_details.groupby('city')['cleaning_fee'].sum().reset_index().sort_values(by='cleaning_fee',ascending=False)

gb