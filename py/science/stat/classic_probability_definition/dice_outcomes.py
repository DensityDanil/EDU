import itertools as it
#http://localhost:8888/notebooks/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D0%92%D0%B5%D1%80%D0%BE%D1%8F%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8.ipynb
edges = 6
dices = 2
goal_points = 7

def roll_dice_to_reach_goal( dices
                            ,edges
                            ,goal_points
                            ,return_type='prob'):
    
    sCharacters = [i for i in range(1,edges+1)]
    
    only_needed = []
    not_fit_cases = []
    for iCombinationLength in range(0, len(sCharacters)+1):
      for aCombination in it.product(sCharacters, repeat=dices):
          
        comb = aCombination
        if comb not in only_needed and sum(comb)==goal_points:#note this part may be changes
            only_needed.append(comb)
            #print(comb)
            
        elif comb not in not_fit_cases and comb not in only_needed:
            not_fit_cases.append(comb)
            
    bernoulli_formula = len(only_needed)/(len(not_fit_cases)+len(only_needed))
    storage = {  'prob':bernoulli_formula
                ,'only_needed':only_needed
                ,'not_fit_cases':not_fit_cases
                ,'len(only_needed)': len(only_needed)
                ,'len(not_fit_cases)': len(not_fit_cases)
                ,'total_space':(len(not_fit_cases)+len(only_needed))
               }
    
    out = str(round(bernoulli_formula*100,1))+'%'if return_type=='prob' else storage
    return out


r = roll_dice_to_reach_goal(
                         dices=2
                        ,edges=6
                        ,goal_points=7
                        ,return_type='prob')

##r = roll_dice_to_reach_goal(
##                         dices=3
##                        ,edges=4
##                        ,goal_points=6)
