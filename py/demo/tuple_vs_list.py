rng = range(1,10**6)
lst=list(rng)
t = tuple(rng)
print(lst.__sizeof__())
print(t.__sizeof__())

#8000040
#8000016