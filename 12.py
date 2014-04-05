from math import sqrt

def divisors(n):
    c = 0
    if sqrt(n) ** 2 == n: c = 1
    for i in range(1, int(sqrt(n) + 0.5)):
        if n % i == 0: c = c + 2
    return c

i = 1
j = 1
while True:
    if divisors(i) > 500: break
    j = j + 1
    i = i + j

print i
