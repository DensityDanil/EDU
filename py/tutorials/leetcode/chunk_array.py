tests = [ ([1,9,6,3,2],1)
       ,([1,9,6,3,2],3)
       ,([8,5,3,2,6],6)
       ,([],1)
      ]


def chunk_array(arr,n):
    out = []
    for i in range(0,len(arr),n):
        sublst = arr[i:i+n]
        out.append(sublst)
    return out

for i in tests:
    arr = i[0]
    n = i[1]
    res = chunk_array(arr,n)
    print(res)
#loop
#len
#slice
