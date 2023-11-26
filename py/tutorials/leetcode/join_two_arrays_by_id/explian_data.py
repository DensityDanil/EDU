#https://leetcode.com/problems/join-two-arrays-by-id/?envType=study-plan-v2&envId=30-days-of-javascript
import pandas as pd
test1 = [[
            {"id": 1, "x": 1},
            {"id": 2, "x": 9}
        ],
        [
            {"id": 3, "x": 5}
        ]]

test2 = [
    [
        {"id": 1, "x": 2, "y": 3},
        {"id": 2, "x": 3, "y": 6}
    ]
    ,[
        {"id": 2, "x": 10, "y": 20},
        {"id": 3, "x": 0, "y": 0}
    ]
]


test3 = [
     [{"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}]
    ,[{"id": 1, "b": {"c": 84}, "v": [1, 3]}]
]

#iter thouth list of dicts
#get id key
#comparse both id dicts
#merge if id not exist from one
#if arr2 id present in arr1 then overwrite
#d1.get() == None 

#sql join impl

#list->
# len
# [0]
# for
# append
    #dict->
    #get
    #in


def position(arr1,arr2):
    return sorted([arr1,arr2],key=len,reverse=True)

arr1,arr2 = test2[0],test2[1]
def struct_iter(struct):
    ids = []
    location = []
    for idx,item in enumerate(struct):
        if type(item)==dict:
            if 'id' in item:
                v = item['id']
                row = v
                ids.append(row)
                location.append(idx)
                #print(v)
    return ids,location


#merge array with dicts
#test2[0]+[test2[1][1]] 

# [{'id': 1, 'x': 2, 'y': 3},
#  {'id': 2, 'x': 3, 'y': 6},
#  {'id': 3, 'x': 0, 'y': 0}]

#compare arrays with dicts that have same ids 
#test2[0][1],[test2[1][0]]
#({'id': 2, 'x': 3, 'y': 6}, [{'id': 2, 'x': 10, 'y': 20}])

#
#test2[0][1]['id'], test2[1][0]['id'] #(2,2)


#cross join (cartesian product) is dangerous for sattelite or cosmic programs!
#iterate throuh items from both side with no need to detection which is longer
# for i in test2[0]:
#     for j in test2[0]:
#         print(i,j)

# #detect same id
# for i in test2[1]:
#     for j in test2[0]:
#         print(i,j,i['id'] == j['id'])

# {'id': 2, 'x': 10, 'y': 20} {'id': 1, 'x': 2, 'y': 3} False
# {'id': 2, 'x': 10, 'y': 20} {'id': 2, 'x': 3, 'y': 6} True
# {'id': 3, 'x': 0, 'y': 0} {'id': 1, 'x': 2, 'y': 3} False
# {'id': 3, 'x': 0, 'y': 0} {'id': 2, 'x': 3, 'y': 6} False

#rude variation to merge only unique elems
out = []
for i in test2[1]:
    for j in test2[0]:
        if i['id'] == j['id']:
            j = i
        if "'id': "+str(i['id']) not in str(out):
            out.append(i)
        if "'id': "+str(j['id']) not in str(out):
            out.append(j) 
            

#two lists check + not in variation
out = []
check = []
for i in test2[1]:
    for j in test2[0]:
        if i['id'] == j['id']:
            j = i
        if i['id'] not in check:
            check.append(i['id'])
            out.append(i)
        if j['id'] not in check:
            check.append(j['id'])
            out.append(j) 

#
def append_new(i,j):
    for key_name in i:
        if key_name not in j:
            if len(key_name)!=0:
                j[key_name] = i[key_name]


def join_by_id(arr1,arr2):
    out = []
    check = []
    for i in arr1:
        for j in arr2:
            if i['id'] == j['id']:
                #print([(a2ik,i[a2ik]) if len(a2ik)!=0  else [] for a2ik in i if a2ik not in j])
                #print([arr2_item_key for arr2_item_key in j if arr2_item_key not in i])

                append_new(i,j)
                append_new(j,i)
                i = j

            if i['id'] not in check:
                check.append(i['id'])
                out.append(i)
            if j['id'] not in check:
                check.append(j['id'])
                out.append(j) 
    return out


join_by_id(test1[0],test1[1])
join_by_id(test3[0],test3[1])