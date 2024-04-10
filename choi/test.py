from itertools import combinations

li = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
comb = combinations(li, 2)
print(list(comb))
print(len(list(comb)))