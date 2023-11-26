sample_space = {'H','T'}

def is_heads_or_tails(outcome):
    return outcome in sample_space
    
def is_neihter(outcome):
    return not is_heads_or_tails(outcome)
    
def is_heads(outcome):
    return outcome == 'H'
    
def is_tails(outcome):
    return outcome == 't'
    
def get_matching_event(event_condition,sample_space):
    return set([outcome for outcome in sample_space if event_condition(outcome)])

event_conditions = [is_heads_or_tails,is_neihter,is_heads,is_tails]

for event_condition in event_conditions:
    #print(event_condition.name)
    event = get_matching_event(event_condition,sample_space)
    print(event)