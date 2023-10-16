import random as r
one_game_players = 2
one_game_round = 5
games_count = 0

storage = []

tour=0

while tour!=8:

    p1,p2 = [[r.randint(0,1) for players in  range(one_game_round)] for players in range(one_game_players)]
    s1,s2 = sum(p1),sum(p2)

    sparing_count = 0
    
    row = tour,sparing_count,s1,s2,p1,p2
    storage.append(row)
    
    while s1==s2:
        p1,p2 = [[r.randint(0,1) for players in  range(one_game_round)] for players in range(one_game_players)]
        s1,s2 = sum(p1),sum(p2)
        sparing_count+=1
        row = tour,sparing_count,s1,s2,p1,p2
        storage.append(row)


    tour+=1
    
for i in storage:    
    print(*i)
    
