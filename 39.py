m = i = 0
for n in range(1, 1001):
    s = set()
    for a in range(1, n - 1):
        for b in range(a, n):
            c = n - a - b
            if a * a + b * b == c * c:
                p = [a, b, c]
                p.sort()
                s.add((p[0], p[1], p[2]))
    if m < len(s):
        m = len(s)
        i = n
print i
