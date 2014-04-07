from itertools import permutations

print reduce(lambda a, b: a + str(b), list(permutations(range(0, 10)))[999999], '')
