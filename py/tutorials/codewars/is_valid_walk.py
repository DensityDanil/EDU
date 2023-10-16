import itertools as it

def is_valid_walk(walk):
    res = set(walk.count(i) for i in set(walk))
    
    pair1,pair2 = list('ns'),list('ew')
    
    for p1,p2 in zip(pair1,pair2):
        c1 = walk.count(p1)==walk.count(p1)
        c2 = walk.count(p2)==walk.count(p2)
        #print(c1,c2)
        
    c3 = len(walk)==10
    
    c4 = c1+c2+c3
    
    out=False
    if c4:
        out=True
    return out


test1 = ['n','n','n','s','n','s','n','s','n','s']
test1 = ['n','s','n','s','n','s','n','s','n','s']
test1 = ['e', 'w', 's', 'w', 'n', 's', 'n', 's', 'e', 'w']
test1= ['e', 'w', 's', 'w', 'n', 's', 'n', 's', 'e', 'w']


def is_valid_walk(walk):
    c = 0
    for i in range(0,len(walk),2):
        comb = ''.join(sorted(walk[i:i+2]))
        print(comb)
        if comb in ['ew', 'es', 'en', 'sw', 'nw', 'ns']:
            c+=1
    return len(walk)==10 and c==5

validation1 = is_valid_walk(test1)
print(validation1)
