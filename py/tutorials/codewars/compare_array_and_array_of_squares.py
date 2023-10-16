def comp(array1, array2):
    
    res1 = [i**2 for i in array1 if i**2 in array2]
    res2 = [i for i in array2 if i in res1]       
                
    return len(res1)==len(array1) and len(res2)==len(array1)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

res = comp(a1,a2)
