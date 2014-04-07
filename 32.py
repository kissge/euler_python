from itertools import permutations

ans = set()
for perm in list(permutations(range(1, 10))):
    for i in range(1, 9):
        for j in range(i + 1, 10):
            x = reduce(lambda x, y: x * 10 + y, perm[0:i], 0)
            y = reduce(lambda x, y: x * 10 + y, perm[i:j], 0)
            z = reduce(lambda x, y: x * 10 + y, perm[j:], 0)
            if x * y == z: ans.add(z)

print sum(ans)
