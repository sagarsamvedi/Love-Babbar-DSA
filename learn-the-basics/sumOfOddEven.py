
number = int(input())
evenSum = 0
oddSum = 0
while number != 0:
    lastDigit  = number%10
    if lastDigit%2 == 0:
        evenSum += lastDigit
    else:
        oddSum += lastDigit
    number //= 10
print(evenSum," ",oddSum)