def frac(n):
    if n == 1: return 1
    return n * frac(n - 1)

print frac(40) / frac(20) / frac(20)
