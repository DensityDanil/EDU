import random


tag_limit = random.randint(1,10)

def rand_tag():
    return [chr(random.randint(1,26)+96) for k in range(tag_limit)]

products = { 'a': rand_tag()
            ,'b': rand_tag()
            ,'c': rand_tag()
            ,'d': rand_tag()}


user_input = input()
while user_input!='0':
    user_input = input()
    res = products.get(user_input)
    if res!=None:
        for tag in res:
            with open('log.txt','a+') as f:
                row = f"{user_input}\t{tag}\t{res}\n"
                f.write(row)
                
            #print(tag)
    else:
        print('no mice spot in the garden, you"re blind')
        user_input = input()

    del products[user_input]
    
    if len(products)==0:
        with open('log.txt','a+') as f:
                row = f"No any mice in the garden\n"
                f.write(tag)
        


#usage:
#not correct answer for lovely teacher then -1 vehicle for crazy machine
#

