import itertools
##Пример. В чемпионате мира участвуют 
##15 команд, среди которых есть команда Англии.
##С помощью жребия их нужно разделить на пять групп по три команды в каждой.
##В ящике вперемешку лежат карточки с номерами групп:
##Капитаны команд тянут по одной карточке.
##Какова вероятность того, что команда Англии окажется в третьей группе?


#is there same prob for all tems to be in group in first permutations round?


lst = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]

groups = 2
groups_divisions = 5
players = groups*groups_divisions#15


group_rng = list(range(1,groups+1))


combinations = []
for i in group_rng:
        generate = [i for k in range(groups_divisions)]
        #print()
        combinations.extend(generate)


a = 1
r = combinations.count(a)/len(combinations)
