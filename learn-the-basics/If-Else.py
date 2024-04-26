# https://www.naukri.com/code360/problems/if-else-decision-making_8357235?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import *
def compareIfElse(a: int, b: int) -> str:
    if a > b:
        return "greater"
    elif a < b:
        return "smaller"
    else:
        return "equal"