def group_by(array,s):
    dimension = s(array)
    group = set(dimension)
    vectror = list(zip(dimension,array))

    out = dict()
    for k in group:
        out[k] = [o[1] for o in vectror if o[0]==k]
    
    return out

s = lambda lst,gt_then:[1 if i>gt_then else 0 for i in lst]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r = group_by(array,s(array,5))
