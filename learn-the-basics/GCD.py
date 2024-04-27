def calcGCD(n,m):
    while (n > 0 and m > 0):
        if n >= m :
            n = n%m
        elif m > n:
            m = m%n
    if n == 0:
        return m
    return n