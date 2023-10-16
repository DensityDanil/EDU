from collections.abc import Iterable


#https://py.checkio.org/en/mission/duplicate-zeros/
def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    
    out=[]
    for i in donuts:
        if i==0:
            out.append(0)
            out.append(0)
        else:
            out.append(i)
            
    return out


print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")
