def d(n):
    if n < 10: return n
    l = 1
    d = 1
    d2 = 9
    while not l <= n < l + d * d2:
        l += d * d2
        d += 1
        d2 *= 10
    d2 = d2 / 9
    while not l <= n < l + d:
        l += d
        d2 += 1
    return int(str(d2)[n - l])

print reduce(lambda a, b: a * d(int(10 ** b)), range(0, 7), 1)
