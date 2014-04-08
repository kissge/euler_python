def is_palindrome(l):
    return l == ''.join(list(reversed(l)))

print sum(filter(lambda i: is_palindrome(str(i)) and is_palindrome(bin(i)[2:]), range(1, 1000000)))
