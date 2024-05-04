# https://www.naukri.com/code360/problems/bubble-sort_624380?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# You are given an integer array 'arr' of size 'N'.

# You must sort this array using 'Bubble Sort'.

from typing import List

def bubbleSort(arr: List[int], n: int):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            arr[i] , arr[i + 1] = arr[i+1], arr[i]
    bubbleSort(arr,n-1)\
        
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
bubbleSort(arr, n)
print("Sorted array is:", arr)
        
