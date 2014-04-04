a = b = 0
for i in range(1, 101):
    a += i * i
    b += i
print b * b - a
