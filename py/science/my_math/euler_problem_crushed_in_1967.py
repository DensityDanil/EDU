
limit = 151


for a in range(1,limit):
    for b in range(1,limit):
        for c in range(1,limit):
            for d in range(1,limit):
                for e in range(1,limit):
                    if (a**5+b**5+c**5+e**5+d**5)==e**5:
                        print(a**5,b**5,c**5,e**5,d**5,e**5)
    
