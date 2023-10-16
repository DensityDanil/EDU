n = 10
while n > 0: #note(1)
    n -= 1
    if n == 2: #this skip two
        continue
    print(n, end='*') #note(2) there will be 0 as last element event if (1)
