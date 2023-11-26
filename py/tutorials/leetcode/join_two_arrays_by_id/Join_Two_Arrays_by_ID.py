arr1 = [
    {"id": 1, "x": 1},
    {"id": 2, "x": 9}
]

arr2 = [
     {"id": 3, "x": 5}
    ,{"id": 2, "x": 9}
]

#zip
#items
#set list
#two sided



dicts = [[len(arr1),arr1],[len(arr2),arr2]]


for i in arr1:
    keys_list = list(i.items())
    for key1 in keys_list:
        k = key1[0]
        v = key1[1]
        
        r = [j for j in arr2 if j.get(k)==v and j['id']==k]
        print(k,v,r)
