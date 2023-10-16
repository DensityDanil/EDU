def rgb(r, g, b):
    
    lst = [r,g,b]
    res = ''
                   
    for i in lst:
        if (i>=0 and i<=255 ):
            print(1)
        elif i<0:
            print(2)
        elif i>255:
            print(3)
            
    return res
rgb(-20, 275, 125)
