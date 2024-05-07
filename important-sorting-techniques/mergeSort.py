# https://www.naukri.com/code360/problems/merge-sort_5846?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# You are given the starting 'l' and the ending 'r' positions of the array 'ARR'.
# You must sort the elements between 'l' and 'r'.


def mergeSort(arr,l,r):
    if l < r:
        mid = l + (r- l)//2
        mergeSort(arr,0,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)

def merge(arr,left,mid,right):
    i = j = 0
    k = left
    n1 = mid - left + 1
    n2 = right - mid

    left_half = [arr[left + i] for i in range(n1)]
    right_half = [arr[mid + i + 1] for i in range(n2)]

    while (i < n1 and j < n2):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1
    

        

