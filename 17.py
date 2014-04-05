dict = { 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
         10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
         20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 1000: 11 }
def word_len(n):
    if n in dict: return dict[n]
    if n < 100: return dict[n / 10 * 10] + dict[n % 10]
    if n % 100 == 0: return dict[n / 100] + len('hundred')
    return dict[n / 100] + len('hundred') + len('and') + word_len(n % 100)

m = 0
for i in range(1, 1001):
    m = m + word_len(i)
print m

