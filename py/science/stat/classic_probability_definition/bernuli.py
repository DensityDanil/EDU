import itertools

#series = list(it.combinations(['win','loss'],2))


def roll_it_catch_it_n_times( games_count
         ,state
         ,repeat_times
         ,return_type='prob'
          ):
	'''
	Перед началом футбольного матча судья бросает монетку,
	чтобы определить, какая из команд будет владеть мячом в начале матча. 
	Команда «Физик» играет два матча с разными командами. Найдите вероятность того, 
	что «Физик» хотя бы один раз выиграет мяч.
	'''
    only_needed = []
    not_fit_cases = []
    sCharacters = '1,0'.split(',')
    #https://stackoverflow.com/questions/37669869/python-itertools-combinations-with-replacement-not-returning-all-combinations
    for iCombinationLength in range(0, len(sCharacters)+1):
      for aCombination in itertools.product(sCharacters, repeat=games_count):
          
        comb = aCombination
        
        if comb.count(state)==repeat_times and comb not in only_needed:
            only_needed.append(comb)
        elif comb not in not_fit_cases and comb not in only_needed:
            not_fit_cases.append(comb)


    bernoulli_formula = len(only_needed)/(len(not_fit_cases)+len(only_needed))
    storage = {  'prob':bernoulli_formula
                ,'only_needed':only_needed
                ,'not_fit_cases':not_fit_cases
               }
    out = bernoulli_formula if return_type=='prob' else storage
    return out

r = roll_it_catch_it_n_times(2,'1',1,0)
