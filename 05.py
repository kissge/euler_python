def sub(p, q):
    if p % q == 0: return sub(p / q, q) + 1
    return 0


n = {}
for i in range(2, 21):
    for j in range(2, i + 1):
        if i % j == 0:
            s = sub(i, j)
            if j in n:
                n[j] = max(n[j], s)
            else:
                n[j] = s
            i /= j ** s
i = 1
for p, q in n.items():
    i *= p ** q
print i

