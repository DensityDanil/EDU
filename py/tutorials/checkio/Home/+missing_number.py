#https://py.checkio.org/en/mission/missing-number/

def missing_number(items: list[int]) -> int:
    
    items = sorted(items)
    delta = min([items[idx+1]-items[idx] for idx in range(len(items)-1) ])
    mi,ma = min(items),max(items)
    return list(set(list(range(mi,ma,delta))).difference(set(items)))[0]


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

#6+2=8
#2+4=6
#6+4!=8
#8-6=2
#2+2=4

print("The mission is done! Click 'Check Solution' to earn rewards!")
