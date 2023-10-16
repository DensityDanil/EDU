import itertools as it
#https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python

case = []
case.extend(['red']*4)
case.extend(['blue']*6)

r = list(it.combinations(case,3))
