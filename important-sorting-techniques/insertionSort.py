# https://www.naukri.com/code360/problems/insertion-sort_624381?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

# Problem statement
# You are given an integer array 'arr' of size 'N'.
# You must sort this array using 'Insertion Sort' recursively.

def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr

    arr = recursive_insertion_sort(arr,n-1)

    last_element = arr[n-1]
    j = n-2
    while j >= 0 and last_element < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last_element

    return arr


def test_recursive_insertion_sort():
    # Test Case 1
    input_arr1 = [5, 3, 8, 1, 2]
    expected_output1 = [1, 2, 3, 5, 8]
    output1 = recursive_insertion_sort(input_arr1)
    assert output1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {output1}"

    # Test Case 2
    input_arr2 = [9, 7, 5, 3, 1]
    expected_output2 = [1, 3, 5, 7, 9]
    output2 = recursive_insertion_sort(input_arr2)
    assert output2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {output2}"

    # Test Case 3
    input_arr3 = [1, 2, 3, 4, 5]
    expected_output3 = [1, 2, 3, 4, 5]
    output3 = recursive_insertion_sort(input_arr3)
    assert output3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {output3}"

    # Test Case 4
    input_arr4 = []
    expected_output4 = []
    output4 = recursive_insertion_sort(input_arr4)
    assert output4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {output4}"

    # Test Case 5
    input_arr5 = [5, 5, 3, 2, 1]
    expected_output5 = [1, 2, 3, 5, 5]
    output5 = recursive_insertion_sort(input_arr5)
    assert output5 == expected_output5, f"Test case 5 failed: Expected {expected_output5}, got {output5}"

    print("All test cases passed successfully!")

# Run the test cases
test_recursive_insertion_sort()