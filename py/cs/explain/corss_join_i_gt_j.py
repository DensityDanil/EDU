lst = [1,2,3,4]
for i in lst:
  for j in lst:
    if i!=j and i>j: #note when i then each j will be less then i till maximum i not be reached
      print(i,j)
# 2 1
# 3 1
# 3 2
# 4 1
# 4 2
# 4 3