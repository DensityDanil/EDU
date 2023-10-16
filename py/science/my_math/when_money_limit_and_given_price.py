limit = 10**3
for x in range(0,limit):
    for y in range(0,limit):
        for z in range(0,limit):
            if 10*x+5*y+0.5*z==100: #[sum]==100 #sum->price*cost
                r = f"{x}\t{y}\t{z}"
                print(r)
    
