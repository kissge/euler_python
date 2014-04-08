sieve = [False, False] + [True] * 1000000
for i in range(2, len(sieve)):
    if sieve[i]:
        j = i * 2
        while j < len(sieve):
            sieve[j] = False
            j = j + i

def is_prime(n):
    return sieve[n]

def rotation(l):
    return map(lambda i: l[i:] + l[:i], range(0, len(l)))

print len(filter(lambda n: reduce(lambda a, b: a and is_prime(reduce(lambda a, b: a * 10 + int(b), b, 0)), rotation(str(n)), True), range(2, 1000000)))
