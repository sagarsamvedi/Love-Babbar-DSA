def countDigits(n):
    temp = n
    count = 0 
    while temp != 0:
        digit = temp%10
        if digit != 0 and n%digit == 0:
            count += 1
        temp //= 10
    return count

        