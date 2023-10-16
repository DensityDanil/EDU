def max_df(a_n: int) -> int:
    step_rng = list(range(1,a_n+1))


    for start in step_rng:
        for step in step_rng:
            
            r = [num for num in range(start,a_n+1,step)]
            if r!=[] and len(r)>1:
                print(r)
            
        
        


test1 = max_df(7)
