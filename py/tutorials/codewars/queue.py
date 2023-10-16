import time


waiting_line = [2,3,10]
dimensions = 2

for i in range(0,len(waiting_line),dimensions):
    sublst = waiting_line[i:i+dimensions]
    print(sublst)
