#https://stepik.org/lesson/311433/step/4?unit=293861

count = 0
p = 1 #(2)

test = '''-2
-4
-1
4
0
6
7
8
9
10'''.split('\n')

mx = 0
s = 0
limit = -10**6

for i in range(10):
    x = int(test[i])
    #print(x,x >= limit)
    if x >= limit and x<0:
        s += x
        
        if x > s: #(1)
            mx = x
            
print(s)
print(mx)

##############################################################################
mx = 0
s = 0

limit = -10**6
neg_values = []
for i in range(10):
    x = int(test[i])
    if x >= limit and x<0:
        s += x
        neg_values.append(x)

if len(neg_values)>0:
    print(s)
    print(max(neg_values))
else:
    print('NO')
)

##############################################################################
mx = 0
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        if mx == 0 or x > mx:
            mx = x
if s:            
    print(s)
    print(mx)
else:
    print('NO')

