def pandigital(i, n):
    a = reduce(lambda a, b: a + list(str(i * b)), range(1, n + 1), [])
    if len(a) != 9: return False
    b = list(a)
    b.sort()
    if b == list(str(123456789)): return reduce(lambda a, b: a * 10 + int(b), a, 0)

m = 0
for n in range(2, 10):
    for i in range(1, int(10 ** (10 - n))):
        m = max(m, pandigital(i, n))
print m
