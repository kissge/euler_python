from math import sqrt

def d(x):
    s = 1
    if int(sqrt(x)) ** 2 == x: s -= int(sqrt(x))
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0: s += i + x / i
    return s

amicable = set()
for i in range(2, 10000):
    if i in amicable: continue
    if d(i) != i and d(d(i)) == i:
        amicable.add(i)
        amicable.add(d(i))

print sum(amicable)
