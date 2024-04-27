def reverseBits(n):
    reversed_number = 0
    for _ in range(32):
        reversed_number <<= 1
        reversed_number |= n & 1
        n >>= 1
    return reversed_number
    