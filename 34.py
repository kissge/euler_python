from math import factorial

print sum(filter(lambda n: n == reduce(lambda a, b: a + factorial(int(b)), str(n), 0), range(3, 99999)))
