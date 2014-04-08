sieve = [False, False] + [True] * 1000000
for i in range(2, len(sieve)):
    if sieve[i]:
        j = i * 2
        while j < len(sieve):
            sieve[j] = False
            j = j + i

def is_prime(n):
    return sieve[n]

def truncate(n):
    return map(lambda i: int(n[i:]), range(0, len(n))) + map(lambda i: int(n[:i]), range(1, len(n) + 1))

print sum(filter(lambda n: reduce(lambda a, b: a and is_prime(b), truncate(str(n)), True), range(8, 999999)))
