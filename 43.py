from itertools import permutations

def conv(l, i):
    return reduce(lambda x, y: x * 10 + y, l[i - 1:i + 2], 0)

pr = [2, 3, 5, 7, 11, 13, 17]

print sum(map(lambda l: reduce(lambda a, b: a * 10 + b, l, 0), filter(lambda l: reduce(lambda a, b: a and conv(l, b + 2) % pr[b] == 0, range(0, 7), True), permutations(range(0, 10)))))
