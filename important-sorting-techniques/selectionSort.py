# https://www.naukri.com/code360/problems/selection-sort_624469?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.


def selectionSort(arr: List[int]) -> None: 
    
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Sorted array is:", arr)
