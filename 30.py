print sum(filter(lambda i: i == reduce(lambda s, c: s + int(c) ** 5, str(i), 0), range(2, 999999)))
