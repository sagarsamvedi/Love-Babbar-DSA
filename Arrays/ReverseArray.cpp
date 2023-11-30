// Question Link
// https://www.codingninjas.com/studio/problems/reverse-the-array_1262298?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker

#include <iostream>
#include <vector>
using namespace std;

 vector<int> reverseArray( vector<int>& arr, int m) {
    int start = m + 1;
    int end = arr.size() - 1;

    while (start < end) {
         swap(arr[start], arr[end]);
        start++;
        end--;
    }

    return arr;
}

int main() {
    // Example usage
     vector<int> array = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int m = 4;

     vector<int> reversedArray = reverseArray(array, m);

     cout << "Reversed Array: ";
    for (int num : reversedArray) {
         cout << num << " ";
    }

    return 0;
}
