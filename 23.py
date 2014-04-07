from math import sqrt
from itertools import combinations

def d(x):
    s = 1
    if int(sqrt(x)) ** 2 == x: s -= int(sqrt(x))
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0: s += i + x / i
    return s

abundant = []
for i in range(1, 28124):
    if d(i) > i:
        abundant.append(i)

st = set(map(lambda x: x * 2, abundant))
reduce(lambda _, (h, d): st.add(h + d), list(combinations(abundant, 2)), 0)

print reduce(lambda sc, x: sc if x in st else sc + x, range(1, 28124), 0)

