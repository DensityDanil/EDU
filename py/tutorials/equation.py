
base = 10**3
left_edge=-base
limit=0#base#//10**1
solutions = []


#def equation():
    

for n in range(left_edge,limit):
    for k in range(left_edge,limit):
        for m in range(left_edge,limit):
            if (28*n)+(30*k)+(31*m)==365:
                row = n,k,m
                solutions.append(row)
                #print(n,m,k)
                break
