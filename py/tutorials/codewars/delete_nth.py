def delete_nth(order,max_e):
    #pivot = [(idx,val,order.count(val)) for idx,val in enumerate(order) if idx<max_e-1]

    book = {}
    order_updated = []
    for val in order:
        book[val] = book.get(val,0)+1
        if book.get(val,0)<=max_e:
            order_updated.append(val)
    return order_updated

    
test1 = [1,2,3,1,2,1,2,3]
r1 = delete_nth(test1,2)
print(r1)