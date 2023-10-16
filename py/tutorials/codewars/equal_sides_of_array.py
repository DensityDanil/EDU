def find_even_index(arr):
    
    for i in range(len(arr)):
        sum_right = sum(arr[:i])
        for i2 in range(len(arr)):
            sum_left = sum(arr[-i::-1])
            if sum_right==sum_left:
                print(i)
