def dice(side_amount):
    import random
    dice = list(range(side_amount))
    results = [random.choice(dice) for i in range(1_000_000 )]
    
    return round(results.count(1)/len(results)*100,1)


r = dice(4)
