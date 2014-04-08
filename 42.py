import csv

def is_square(n):
    return int(n ** 0.5) ** 2 == n

def calc(x0, hd):
    return x0 + ord(hd) - 64

with open('words.txt', 'r') as f:
    s = csv.reader(f).next()

print len(filter(lambda n: is_square(8 * n + 1), map(lambda s: reduce(calc, s, 0), s)))
