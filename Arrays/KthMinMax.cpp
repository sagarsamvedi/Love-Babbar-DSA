// QUESTION LINK
// https://www.codingninjas.com/studio/problems/kth-smallest-and-largest-element-of-array_1115488?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

 vector<int> kthSmallLarge( vector<int>& arr, int n, int k) {
     vector<int> ans;

     sort(arr.begin(), arr.end());

    ans.push_back(arr[k - 1]);
    ans.push_back(arr[n - 1]);

    return ans;
}

int main() {
     vector<int> arr = {12, 3, 5, 7, 19, 0};  // Sample vector, you can modify as needed

    int k;
     cout << "Enter the value of K: ";
     cin >> k;

     vector<int> result = kthSmallLarge(arr, arr.size(), k);

     cout << "Kth Smallest Element: " << result[0] <<  endl;
     cout << "Kth Largest Element: " << result[1] <<  endl;

    return 0;
}
