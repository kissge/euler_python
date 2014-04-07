n = 1001
s = 1
c = 1
d = 2
while c < n * n:
    s += (c + d) + (c + 2 * d) + (c + 3 * d) + (c + 4 * d)
    c += 4 * d
    d += 2
print s
