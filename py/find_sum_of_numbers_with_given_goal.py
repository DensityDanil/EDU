
lst = [0,1,3,5,6]

k=7

for i in range(len(lst)):
    
    a,b = i,-(i+1)
    s = lst[a]+lst[b]
    if s==k:
        print(a,b)
    elif s<k:
        a = lst[a+1]
        b = -i
    elif s>k:
        a = i
        b = lst[b-1]
