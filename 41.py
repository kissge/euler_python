from itertools import permutations

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5 + 0.5) + 1):
        if n % i == 0: return False
    return True

def solve():
    for i in [10, 9, 8, 7, 6, 5, 4, 3, 2]:
        for perm in permutations(reversed(range(1, i))):
            n = reduce(lambda x, y: x * 10 + y, perm, 0)
            if is_prime(n):
                return n

print solve()
# well, quite sophisticated code :(
