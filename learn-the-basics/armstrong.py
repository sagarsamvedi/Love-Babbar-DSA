import math

def check_armstrong(n):
    count = int(math.log10(n) + 1)
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10
    if sum == n:
        return True
    return False
