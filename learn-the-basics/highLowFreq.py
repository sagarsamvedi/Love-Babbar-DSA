from typing import List
from collections import Counter

def getFrequencies(v: List[int]) -> List[int]: 

    # store frequency of each element
    lookUp = Counter(v)

    #get max and min frequency
    max_freq = max(lookUp.values())

    min_freq = min(lookUp.values())

    # get elements with max and min freq

    max_freq_elements = [element for element,freq in lookUp.items() if freq == max_freq]

    min_freq_elements = [element for element,freq in lookUp.items() if freq == min_freq]

    return [min(max_freq_elements),min(min_freq_elements)]

