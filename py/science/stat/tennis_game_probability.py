import random as r
from faker import Faker

fake = Faker()
total_players = 16
one_game_players = 2
one_game_round = 5


player_first_char = [chr(96+players) for players in  range(total_players)]
random.shuffle(mylist)

game = []


print(*'tour,sparing_count,s1,s2,p1,p2'.split(','),sep='  ')


storage = []
for tour in range(1,total_players//2+1):
    
    pn1,pn2 = [r.choice(player_first_char) for _ in range(one_game_players)]
    
    p1,p2 = [[r.randint(0,1) for players in  range(one_game_round)] for players in range(one_game_players)]
    s1,s2 = sum(p1),sum(p2)

    sparing_count = 0
    
    row = tour,sparing_count,s1,s2,pn1,pn2,p1,p2
    storage.append(row)
    
    while s1==s2:
        p1,p2 = [[r.randint(0,1) for players in  range(one_game_round)] for players in range(one_game_players)]
        s1,s2 = sum(p1),sum(p2)
        sparing_count+=1
        #one_game = 
        #points = sum(one_game)
        
        row = tour,sparing_count,s1,s2,pn1,pn2,p1,p2
        #print(row)
        storage.append(row)
        

c=0
for i in storage:    
    print(*i)
    c+=1
                    



#while !=
#sum==sum
#0==0
#id 1...8 OR anna,beth,thom,damon,robert,poul -> random.choise
#
    



