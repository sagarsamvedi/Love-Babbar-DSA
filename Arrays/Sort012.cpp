// QUESTION LINK
// https://www.codingninjas.com/studio/problems/sort-0-1-2_631055?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker


#include <iostream>
#include <vector>
using namespace std;

  vector<int> dnfSort(  vector<int>& arr) {
    int low = 0, mid = 0, high = arr.size() - 1;

    while (mid <= high) {
        if (arr[mid] == 0) {
              swap(arr[low], arr[mid]);
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            mid++;
        } else {
              swap(arr[mid], arr[high]);
            high--;
        }
    }

    return arr;
}

int main() {
      vector<int> arr = {2, 0, 1, 0, 2, 0, 2, 0, 1, 2, 2, 2};

      vector<int> result = dnfSort(arr);

      cout << "Sorted Array: ";
    for (int num : result) {
          cout << num << " ";
    }
      cout <<   endl;

    return 0;
}
