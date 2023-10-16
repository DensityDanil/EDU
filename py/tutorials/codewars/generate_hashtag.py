def generate_hashtag(s):
    out=False
    if len(s)>=1 and len(s)<=139:
        if ' ' in s:
            out = '#'+''.join([k.strip().title() for k in s.split(' ')])
        elif len(s)==1:
            out = '#'+s.upper()
        else:
            out = '#'+s
    
    return out

test = 'ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'
#test = 'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'
test_assert='#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'

res = generate_hashtag(test)
validation1 = res==test_assert
validation2 = len(res)==len(test_assert)
validation3 = set(res).symmetric_difference(set(test_assert))

def check_token_by_token(string1,string2):
    c=0
    for t1,t2 in zip(string1,string2):
        row = c,t1==t2,t1,t2
        if t1!=t2:
            print(row)
        c+=1
        
validation4 = check_token_by_token(res,test_assert)
