# https://www.naukri.com/code360/problems/k-most-occurrent-numbers_625382?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# Given an array 'v' of 'n' numbers.
# Your task is to find and return the highest and lowest frequency elements.
# If there are multiple elements that have the highest frequency or lowest frequency, pick the smallest element.

# Example:
# Input: ‘n' = 6, 'v' = [1, 2, 3, 1, 1, 4]
# Output: 1 2

from collections import Counter

def getFrequencies(v):
    # store frequency of each element
    lookUp = Counter(v)
    # get max and min frequency
    max_freq = max(lookUp.values())
    min_freq = min(lookUp.values())
    # get elements with max and min freq
    max_freq_elements = [element for element,freq in lookUp.items() if freq == max_freq]
    min_freq_elements = [element for element,freq in lookUp.items() if freq == min_freq]
    return [min(max_freq_elements),min(min_freq_elements)]