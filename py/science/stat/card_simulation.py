#file:///W:/Games/Леонард%20Апельцин%20%20-%20Data_Science.pdf
import random
import itertools as it
import numpy as np
import pandas as pd
import time





##c = 0
##game_choise = []
##while total_cards:
##    print(c,random.choice(game))
##    time.sleep(1)
##    total_cards-=1
##    c+=1

def rand_sample(total_cards):
    #total_cards = 52
    half_cards = total_cards//2
    card_colors = ['red','black']
    #game = [random.choice() for i in range(total_cards)]
    #f = pd.Series(game).value_counts()
    game_sample = ['red']*half_cards+['black']*half_cards
    random.shuffle(game_sample)
    return game_sample


def game(when_stop_idx,game_sample):
    
    for idx,game_card in enumerate(game_sample):
        if idx==when_stop_idx and idx!=len(game_sample)-1:
            #print(game_card[idx+1])
            
            return game_card
            break
            
game_sample = rand_sample(52)


storage = []
for _ in range(10**5):
    player_solution = random.randint(0,52)
    player_expect = random.choice(['red','black'])
    
    r = game(player_solution,game_sample)
    res = r==player_expect
    
    storage.append(res)

f = pd.Series(storage).value_counts()
