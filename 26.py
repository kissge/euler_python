def cycle(n):
    def f(a, b):
        if a % b == 0: return 1 + f(a / b, b)
        return 0
    a = f(n, 2)
    b = f(n, 5)
    n2 = n / (2 ** a) / (5 ** b)
    if n2 == 1: return False
    c = 1
    d = 10 % n2
    while d != 1:
        c = c + 1
        d = (d * 10) % n2
    return c

m = n = 0
for i in range(2, 1000):
    if cycle(i) > m:
        m = cycle(i)
        n = i

print n

