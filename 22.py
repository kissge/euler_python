import csv

def calc(x0, hd):
    return x0 + ord(hd) - 64

with open('names.txt', 'r') as f:
    s = csv.reader(f).next()
s.sort()

n = 0
for i in range(0, len(s)):
    n += (i + 1) * reduce(calc, s[i], 0)

print n
