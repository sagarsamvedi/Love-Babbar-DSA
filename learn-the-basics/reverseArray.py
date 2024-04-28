from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    def fRecursion(i,n,nums):
        if i >= n//2:
            return nums
        nums[i],nums[n-i-1] = nums[n-i-1],nums[i]
        return fRecursion(i+1,n,nums)
    return fRecursion(0,n,nums)       