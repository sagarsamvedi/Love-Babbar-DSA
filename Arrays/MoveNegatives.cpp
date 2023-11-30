// QUESTION LINK
// https://www.codingninjas.com/studio/problems/move-all-negative-numbers-to-beginning-and-positive-to-end_1112620?topList=love-babbar-dsa-sheet-problems&utm_source=website&utm_medium=affiliate&utm_campaign=450dsatracker&leftPanelTabValue=SUBMISSION

#include <iostream>
#include <vector>
using namespace std;

  vector<int> separateNegativeAndPositive(  vector<int>& nums) {
    int i = 0;
    int j = 0;
    int size = nums.size();

    while (j < size) {
        if (nums[j] < 0) {
              swap(nums[i], nums[j]);
            i++;
        }
        j++;
    }

    return nums;
}

int main() {
      vector<int> nums = {-1, 2, -3, 4, 5, -6, -7, 8, 9};
    
      cout << "Original Array: ";
    for (int num : nums) {
          cout << num << " ";
    }
      cout <<   endl;

      vector<int> result = separateNegativeAndPositive(nums);

      cout << "Separated Array: ";
    for (int num : result) {
          cout << num << " ";
    }
      cout <<   endl;

    return 0;
}
