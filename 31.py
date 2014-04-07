coins = [200, 100, 50, 20, 10, 5, 2, 1]

memo = { }
def dp(x, n):
    if x < 0: return 0
    if x < 2: return 1
    if not (x, n) in memo:
        available = filter(lambda m: m <= n, coins)
        memo[x, n] = sum(map(lambda n: dp(x - n, n), available))
    return memo[x, n]

print dp(200, coins[0])
