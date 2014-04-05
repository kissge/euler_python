memo = { 1: 1 }
def count_chain(n):
    if not n in memo:
        if n % 2 == 0:
            memo[n] = 1 + count_chain(n / 2)
        else:
            memo[n] = 1 + count_chain(3 * n + 1)
    return memo[n]

m = 0
for i in range(1, 1000000):
    c = count_chain(i)
    if c > m:
        m = c
        n = i

print n
