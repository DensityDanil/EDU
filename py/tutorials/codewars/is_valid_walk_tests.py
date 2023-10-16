tests = [['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['s', 'e', 'w', 'n', 'n', 's', 's', 'w', 'n', 'e'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['n', 's', 's', 'w', 'n', 's', 'e', 'e', 'n', 'w'],['s', 'e', 'n', 'n', 'e', 'w', 'w', 's', 'w', 'e'],['s', 'e', 'n', 'n', 's', 'n', 'w', 's', 's', 'n'],['e', 'w', 's', 's', 'n', 'w', 'e', 'n', 'n', 's'],['s', 'e', 'w', 'e', 'e', 'n', 'w', 'e', 'w', 'w'],['n', 'w', 'n', 's', 'e', 's', 'e', 's', 'n', 'w'],['w', 's', 'n', 'e', 'w', 'e', 'n', 's', 'w', 'e'],['s', 'w', 'n', 'w', 's', 'n', 'e', 's', 'e', 'n'],['s', 'w', 'w', 'w', 'w', 'n', 'e', 'e', 'e', 'e'],['e', 'w', 's', 'w', 's', 'w', 'e', 'n', 'e', 'n'],['s', 'e', 'e', 's', 'w', 'n', 'w', 'w', 'n', 'e'],['w', 'n', 'e', 'w', 's', 'e', 's', 'w', 'e', 'n'],['e', 's', 'w', 's', 'n', 'w', 'n', 'e', 'n', 's'],['w', 'w', 'e', 's', 'w', 'e', 'e', 'w', 'n', 'e'],['w', 'w', 'n', 'n', 'w', 'e', 'e', 's', 's', 'e'],['w', 's', 's', 's', 'w', 'e', 'n', 'n', 'n', 'e'],['w', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'e', 'w'],['s', 's', 'w', 'n', 'w', 'n', 'n', 'e', 's', 'e'],['s', 'e', 'w', 'n', 'n', 'n', 'w', 'e', 's', 's'],['w', 's', 's', 'n', 'e', 'e', 'n', 'n', 's', 'w'],['n', 'w', 'n', 's', 'w', 's', 'e', 's', 'n', 'e'],['e', 'e', 'e', 'n', 's', 'w', 'w', 'w', 's', 'n'],['s', 'n', 'e', 'w', 'n', 'n', 's', 'w', 'e', 's']]



def pivot(test1):
    return list((test1.count(i),i) for i in set(test1))


def combinations(walk):
    comb_lst = []
    for i in range(0,len(walk),2):
        comb = ''.join(sorted(walk[i:i+2]))
        comb_lst.append(comb)
        #print(comb)
    return comb_lst


seen = []
for i in tests:
    r = combinations(i)
    for k in r:
        if k not in seen:
            seen.append(k)
            print(k)


