import itertools as it

a='198400'
b=list(a)
c=4
f=len(a)-c

e=0
g=set()

hole = [
        int(''.join(i1))
        for i1 in it.permutations(b,f)
        if len(str(int(''.join(i1))))==f
        ]

print( min(hole) )


##побачивши код
##піти заховатися за діван
##щоб у всіх страшних снах
##помінятися місцями з страховищами тіми


##for i1 in it.permutations(b,f):
##    k = ''.join(i1)
##    if not k.startswith('0'): #and len(k)>1
##        d = int(''.join(i1))
##        print(k)
####        print(d)
##        e+=1
##        g.add(d)
##    elif int(k)==0:
##        print(k)
##        g.add(int(k))
##        e+=1
##    
##h = len(g)
##
##i=min(g)
##print(f,e,h,i)
##
###
##j = min(list('12340'),key=lambda x:int(x))

#
