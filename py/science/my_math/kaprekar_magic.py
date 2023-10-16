def numerics(n):
    return [int(i) for i in sorted(str(n)) ]


def kaprekar_step(L):
    s = lambda lst,dtype:[dtype(i) for i in lst]
    tranform = numerics(L)
 
    values = sorted([int(''.join(s(tranform,str) )), int(''.join(s(tranform[::-1],str) ) )])
    res = values[1] - values[0] 
    
    return res

def kaprekar_loop(n):
    const = 6174

    c = 0
    res = 0
    
    storage = []
    while res!=const:
        
        if c==0:
            res = kaprekar_step(n)
            storage.append(res)
        else:
            res = kaprekar_step(storage[-1])
            storage.append(res)
            
        #print(res)
        c+=1
    return res
     

kaprekar_loop(8654)
