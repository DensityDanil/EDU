

criteria = [1,1,2,3,4,5,6,55,7,8,9,10,11,12]
#related_field =

struct=[1,2,2,3,3,3]

book = {}

for elem in struct:
    book[elem] = book.get(elem,0)+1
    
print(book)    
    
