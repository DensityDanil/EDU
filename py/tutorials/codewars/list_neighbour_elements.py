def list_neighbour_elements( lst
             ,revese_neighbors_pos=False
             ,step=False):
    
    first_idx,next_idx = [0,1] if revese_neighbors_pos==False else [1,0]
    #print(first_idx,next_idx)
    step = 1 if step==False else step

    pairs_amount = len(lst)-step
    print(f"{pairs_amount} pairs was build")
    return [(lst[i+first_idx],lst[i+next_idx]) for i in range(0,len(lst)-1,step)]

exp = ["23:00","04:22","18:05","06:24"]



r1 = next_cur(exp)

r2 = next_cur(exp
             ,revese_neighbors_pos=False
             ,step=2)

r3 = next_cur(exp
             ,revese_neighbors_pos=False
             ,step=3)
