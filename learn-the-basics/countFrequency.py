# https://www.naukri.com/code360/problems/count-frequency-in-a-range_8365446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


# Problem statement
# You are given an array 'arr' of length 'n' containing integers within the range '1' to 'x'.
# Your task is to count the frequency of all elements from 1 to n.
# Note:
# You do not need to print anything. Return a frequency array as an array in the function such that index 0 represents the frequency of 1, index 1 represents the frequency of 2, and so on.


# Example:
# Input: ‘n’ = 6 ‘x’ = 9 ‘arr’ = [1, 3, 1, 9, 2, 7]    
# Output: [2, 1, 1, 0, 0, 0]
from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    lookUp = {}

    # storing frequency of each element
    for num in edges:
        if num in lookUp:
            lookUp[num] += 1
        else:
            lookUp[num] = 1
    
    # Construct the frequency array
    freq_array = [0]*n
    for i in range(1,n+1):
        freq_array[i-1] = lookUp.get(i,0)
    return freq_array
    