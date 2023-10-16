# put your python code here
n = int(input())

#constaints = list(map(list,[[range(5,10)],[range(17,38)],[range(78,88)] ])) #note incorrect case range nested
constaints = list(map(list,[range(5,10),range(17,38),range(78,88)] ))


for num in range(1,n+1):
    if (num in constaints[0] or num in constaints[1] or num in constaints[2] ):
        continue
    print(num)

#print(constaints)
