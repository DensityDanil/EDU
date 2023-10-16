def f1(a):
    return 1/a
def f2(a):
    return 1/a**2
    


funcs = [f1,f2,f1]

data = [1,0,1]
for fun,dat in zip(funcs,data):
    try:
        res = fun(dat)
        print(res)
    except Exception as e:
        print(e)
        
    
