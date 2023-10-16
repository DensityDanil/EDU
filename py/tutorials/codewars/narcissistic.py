def narcissistic( value ):
    value_own_nubers = list(map(int,list(str(value))))
    
    
    power_range = list(range(1,100))
    
    answer = False
    
    for power in power_range:
        value_own_nubers_pows = [num**power for num in value_own_nubers]
        
        if sum(value_own_nubers_pows)==value:
            answer = True
            break
        else:
            continue
        
    return answer # Code away


narcissistic( 371 )
