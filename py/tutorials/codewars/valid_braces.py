left_side = '([{'
right_side = ')]}'


arg='[]'
arg = '{}({})[]'
arg = '())({}}{()][]['
ls = [arg.count(i) for i in left_side]
rs = [arg.count(i) for i in right_side]

res = ls==rs
