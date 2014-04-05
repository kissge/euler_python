days = { False: [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ],
         True: [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] }
m = [2]
for y in range(1901, 2001):
    m += days[y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)]
for i in range(1, len(m)):
    m[i] = (m[i - 1] + m[i]) % 7

print m.count(0)
