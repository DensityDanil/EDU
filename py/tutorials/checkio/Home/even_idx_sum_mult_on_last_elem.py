def checkio(array: list[int]) -> int:
    
    return sum([val for idx,val in enumerate(array) if idx%2==0])*array[-1] if len(array)>0 else 0


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
