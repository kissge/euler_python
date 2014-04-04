def reversed_number(x):
    n = 0
    while x > 0:
        m = x % 10
        n = n * 10 + m
        x /= 10
    return n

def check(x):
    for i in range(100, 1000):
        if x % i != 0: continue
        if 100 <= x / i < 1000: return True
    return False


def solve():
    i = 999
    while i >= 100:
        n = i * 1000 + reversed_number(i)
        if check(n): return n
        i -= 1

print solve()
