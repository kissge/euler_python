from array import array

m = 1000000

t = array('B', [1] * m)
for i in range(2, m):
    if t[i] == 1:
        for j in range(2, m / i):
            t[j * i] = 0

c = 0
i = 1
while c < 10001:
    i = i + 1
    if t[i] == 1: c = c + 1

print i
