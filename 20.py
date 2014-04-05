from math import factorial

print reduce(lambda x, y: x + int(y) , str(factorial(100)), 0)
