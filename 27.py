sieve = [False, False] + [True] * 1000000
for i in range(2, len(sieve)):
    if sieve[i]:
        j = i * 2
        while j < len(sieve):
            sieve[j] = False
            j = j + i

def is_prime(n):
    return sieve[n]

def cnt(a, b):
    i = 0
    while is_prime(i * i + a * i + b):
        i = i + 1
    return i

m = ma = mb = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        if cnt(a, b) > m:
            m = cnt(a, b)
            ma = a
            mb = b

print ma * mb
