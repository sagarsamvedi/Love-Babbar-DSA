# https://www.naukri.com/code360/problems/quick-sort_5844?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# Given the 'start' and the 'end'' positions of the array 'input'. Your task is to sort the elements between 'start' and 'end' using quick sort.
# Note :
# Make changes in the input array itself.

def quickSort(arr, start, end):
    # base case
    if start >= end:
        return arr
    
    p = partition(arr,start,end)

    quickSort(arr,start,p-1)
    quickSort(arr,p+1,end)

    return arr

def partition(arr,start,end):
    # if start >= end:
    #     return start  # Return any index within the range
    pivot = arr[start]
    count = 0
    for i in range(start+1,end+1):
        if arr[i] <= pivot:
            count += 1
    pivotIndex = start+count
    arr[start], arr[pivotIndex] = arr[pivotIndex], arr[start]

    i,j = start,end
    while i < pivotIndex and j > pivotIndex:
        while arr[i] < pivot :
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < pivotIndex and j > pivotIndex:
            arr[i],arr[j] = arr[j],arr[i]

    return pivotIndex

def test_recursive_quick_sort():
    # Test Case 1
    input_arr1 = [5, 3, 8, 1, 2]
    expected_output1 = [1, 2, 3, 5, 8]
    output1 = quickSort(input_arr1,0,len(input_arr1)-1)
    assert output1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {output1}"

    # Test Case 2
    input_arr2 = [9, 7, 5, 3, 1]
    expected_output2 = [1, 3, 5, 7, 9]
    output2 = quickSort(input_arr2,0,len(input_arr2)-1)
    assert output2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {output2}"

    # Test Case 3
    input_arr3 = [1, 2, 3, 4, 5]
    expected_output3 = [1, 2, 3, 4, 5]
    output3 = quickSort(input_arr3,0,len(input_arr3)-1)
    assert output3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {output3}"

    # Test Case 4
    input_arr4 = []
    expected_output4 = []
    output4 = quickSort(input_arr4,0,len(input_arr4)-1)
    assert output4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {output4}"

    # Test Case 5
    input_arr5 = [5, 5, 3, 2, 1]
    expected_output5 = [1, 2, 3, 5, 5]
    output5 = quickSort(input_arr5,0,len(input_arr5)-1)
    assert output5 == expected_output5, f"Test case 5 failed: Expected {expected_output5}, got {output5}"

    print("All test cases passed successfully!")

# Run the test cases
test_recursive_quick_sort()