#https://py.checkio.org/en/mission/nearest-value/

def nearest_value(values: set[int], one: int) -> int:
    d = [(k,abs(one-k)) for k in values]
    man = [k[0] for k in d if k[1]==min([k[1] for k in d])]
    
    return man[0] if len(man)==1 else min(man)




print("Example:")
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

# print("The mission is done! Click 'Check Solution' to earn rewards!")
