from fractions import Fraction

def rem(a, b):
    if a % 10 == b: return a / 10
    return a % 10

N = D = 1
for a in range(1, 10):
    for b in range(1, 10):
        if a >= b: continue
        for c in range(1, 10):
            numerator = filter(lambda x: 10 <= x < 100, [a * 10 + c, c * 10 + a])
            denominator = filter(lambda x: 10 <= x < 100, [b * 10 + c, c * 10 + b])
            for n in numerator:
                for d in denominator:
                    if n * rem(d, c) == rem(n, c) * d:
                        N *= n
                        D *= d

print Fraction(N, D)
