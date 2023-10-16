#https://www.codewars.com/kata/592b1e4c96cc12de1e0000b1
data = [ [[1,2,3],[4,5,6]]
         ,[['a','b','c'],['d','e','f']]
        ]

#  {{1,4},{2,5},{3,6}}
#  {{a,d},{b,e},{c,f}}

for row in data:
    r = [(k1,k2) for k1,k2 in zip(row[0],row[1]) ]
    print(r)