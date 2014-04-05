from array import array

m = 2000000

t = array('B', [1] * (m + 1))
for i in range(2, m):
    if t[i] == 1:
        for j in range(2, m / i + 1):
            t[j * i] = 0

s = 0
for i in range(2, m):
    if t[i] == 1: s += i

print s
