i = a = b = 1
while a < 10 ** 999:
    (i, a, b) = (i + 1, b, a + b)
print i
