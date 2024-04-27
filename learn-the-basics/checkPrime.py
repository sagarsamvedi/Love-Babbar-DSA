from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
flag = True
if n < 2:
        print("NO")
        flag = False
sqrt_n = int(sqrt(n))

for i in range(2, sqrt_n + 1):
    
    if n % i == 0:
        print("NO")
        flag = False
        break
if flag:
    print("YES")