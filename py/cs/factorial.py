def factorial(n):
    if n>=2:
        res = 0
        for i in range(n-1,1,-1):
            n = n*i
            res = n
    return res

factorial(4)